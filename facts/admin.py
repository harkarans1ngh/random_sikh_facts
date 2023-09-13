from django.contrib import admin
from facts.models import Fact,ActiveFact

# Register your models here.
admin.site.register(Fact)
admin.site.register(ActiveFact)