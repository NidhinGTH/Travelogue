from django.contrib import admin

# Register your models here.
from travelapp.models import Place
from travelapp.models import Team
admin.site.register(Place)
admin.site.register(Team)
