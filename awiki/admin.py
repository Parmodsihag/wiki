from django.contrib import admin
from .models import Unit, Weapon , UpgradeLevel1, UnitUpgrade1

admin.site.register(Unit)
admin.site.register(Weapon)
# admin.site.register(Upgrade)
admin.site.register(UpgradeLevel1)
admin.site.register(UnitUpgrade1)