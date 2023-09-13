from rest_framework import serializers
from facts.models import Fact,ActiveFact

class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact
        fields = '__all__'

class ActiveFactSerializer(serializers.ModelSerializer):
    retrieved_fact = FactSerializer()

    class Meta:
        model = ActiveFact 
        fields = ('retrieved_fact',)