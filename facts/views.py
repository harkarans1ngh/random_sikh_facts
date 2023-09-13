from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from datetime import datetime, timedelta
from random import choice

from facts.models import Fact, ActiveFact
from facts.serializers import ActiveFactSerializer, FactSerializer

from django.db.models import Q


class FactViewSet(ViewSet):
    queryset = Fact.objects.all()
    permission_classes = [IsAuthenticated]

    # GET FACT
    def list(self, request):
        """
        This view would return the fact of the day based on the following:
        - If there is one fact in the Active Fact Table, return it; Else
            - Query the Facts table and check for:
                - The Fact is Enabled, i.e has been validated
                - The Fact's retrieved date is more than 24 hours ago
            - If Found add an entry in the Active Fact table.
        """
        active_fact_count = ActiveFact.objects.all().count()

        if active_fact_count < 1:
            # Fetch a random fact
            twenty_four_hours_ago = datetime.now() - timedelta(hours=24)
            # Get all objects from the model where the updated field is older than 24 hours ago
            eligible_facts = Fact.objects.filter(
                Q(retrieved_at__lt=twenty_four_hours_ago)
                | Q(retrieved_at__isnull=True),
                fact_validated=True,
            )

            if not eligible_facts:
                return Response(status.HTTP_404_NOT_FOUND)

            # Choose a random object from the eligible Facts
            fact_to_retrieve = choice(eligible_facts)

            fact_to_retrieve.retrieved_at = datetime.now()
            fact_to_retrieve.save()

            # Add to ActiveFact Table
            active_fact = ActiveFact.objects.create(retrieved_fact=fact_to_retrieve)
            # Save to DB
            active_fact.save()

        else:
            # Fetch the fact
            active_fact = ActiveFact.objects.first()

        if active_fact:
            return Response(ActiveFactSerializer(active_fact).data)
        else:
            return Response(status.HTTP_404_NOT_FOUND)

    # Post a Fact
    def create(self, request):
        serializer = FactSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
