from django.db import models

   


class Weapon(models.Model):
    weapon_id = models.AutoField
    name = models.CharField(max_length=100)
    can_attack = models.CharField(max_length=200)

    # Stats
    damage1 = models.IntegerField(default=0)
    damage2 = models.IntegerField(default=0)
    damage3 = models.IntegerField(default=0)
    firing_range = models.FloatField(default=0)
    accuracy_moving = models.FloatField(default=0)
    accuracy_stationary = models.FloatField(default=0)
    explosive_radius = models.FloatField(default=0)

    def __str__(self):
        return self.name
    

class UpgradeLevel1(models.Model):
    upgrade_name = models.CharField(max_length=100, default="?")
    level = models.IntegerField()
    benefit = models.CharField(max_length=300, default='?')
    requirement = models.CharField(max_length=100, default='?')
    cost = models.IntegerField(default=1)
    time = models.CharField(max_length=100, default='?')

    def __str__(self):
        return f"{self.upgrade_name} {self.level}"

class UnitUpgrade1(models.Model):
    name = models.CharField(max_length=50)
    unit_name = models.CharField(max_length=50, default="?")
    total_levels = models.IntegerField()
    levels = models.ManyToManyField(UpgradeLevel1)

    def __str__(self):
        # return f"{self.unit_name} {self.name} - Total Levels: {self.total_levels}"
        return self.name

# Create your models here.
class Unit(models.Model):
    unit_id = models.AutoField
    unit_name = models.CharField(max_length=20)
    unit_faction = models.CharField(max_length=20)
    category = models.CharField(max_length=25, default="?")
    unit_type = models.CharField(max_length=20, default="?")
    unit_trained_in = models.CharField(max_length=50, default="?")
    unit_discription = models.CharField(max_length=500, default="?")
    unit_discription2 = models.CharField(max_length=500, default="?")
    image = models.ImageField(upload_to='awiki/images', default="")

    avialable_from_rank = models.CharField(max_length=2, default="?")

    stat_hp = models.CharField(max_length=7, default="?")
    stat_armor = models.CharField(max_length=3, default="?")
    stat_armor_type = models.CharField(max_length=1, default="?")
    stat_speed = models.CharField(max_length=5, default="?")
    stat_view = models.CharField(max_length=7, default="?")
    # stat_view_siege_mode = models.CharField(max_length=3, default="?")
    stat_cost = models.CharField(max_length=7, default="?")
    stat_time = models.CharField(max_length=7, default="?")
    stat_cp = models.CharField(max_length=7, default="?")

    # Relationships
    # Weapons
    primary_weapon = models.OneToOneField('Weapon', related_name='primary_weapon', null=True, blank=True, on_delete=models.SET_NULL)
    secondary_weapon = models.OneToOneField('Weapon', related_name='secondary_weapon', null=True, blank=True, on_delete=models.SET_NULL)

    # Upgrades
    upgrades = models.ManyToManyField(UnitUpgrade1)




    def __str__(self):
        return self.unit_name
 