from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Fact(models.Model):
    category = models.CharField("Category", max_length=100)
    fact_string = models.CharField("Description",max_length=2000)
    fact_validated = models.BooleanField(default=False)
    retrieved_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.fact_string
    
    def has_add_permission(self, request):
        return not Fact.objects.exists()
    
class ActiveFact(models.Model):
    retrieved_fact = models.ForeignKey(Fact,on_delete=models.CASCADE)

    def __str__(self):
        return self.retrieved_fact.fact_string

    class Meta:
        ordering = ["retrieved_fact"]

