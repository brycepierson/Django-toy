# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Monster(models.Model):
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    size = models.TextField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    tag = models.TextField(db_column='Tag', blank=True, null=True)  # Field name made lowercase.
    alignment = models.TextField(db_column='Alignment', blank=True, null=True)  # Field name made lowercase.
    cr = models.TextField(db_column='CR', blank=True, null=True)  # Field name made lowercase.
    spellcaster = models.TextField(db_column='Spellcaster', blank=True, null=True)  # Field name made lowercase.
    legendary = models.TextField(db_column='Legendary', blank=True, null=True)  # Field name made lowercase.
    lair = models.TextField(db_column='Lair', blank=True, null=True)  # Field name made lowercase.
    unique = models.TextField(db_column='Unique', blank=True, null=True)  # Field name made lowercase.
    familiar = models.TextField(db_column='Familiar', blank=True, null=True)  # Field name made lowercase.
    template = models.TextField(db_column='Template', blank=True, null=True)  # Field name made lowercase.
    arctic = models.TextField(db_column='Arctic', blank=True, null=True)  # Field name made lowercase.
    coastal = models.TextField(db_column='Coastal', blank=True, null=True)  # Field name made lowercase.
    desert = models.TextField(db_column='Desert', blank=True, null=True)  # Field name made lowercase.
    forest = models.TextField(db_column='Forest', blank=True, null=True)  # Field name made lowercase.
    grassland = models.TextField(db_column='Grassland', blank=True, null=True)  # Field name made lowercase.
    hill = models.TextField(db_column='Hill', blank=True, null=True)  # Field name made lowercase.
    mountain = models.TextField(db_column='Mountain', blank=True, null=True)  # Field name made lowercase.
    swamp = models.TextField(db_column='Swamp', blank=True, null=True)  # Field name made lowercase.
    underdark = models.TextField(db_column='Underdark', blank=True, null=True)  # Field name made lowercase.
    underwater = models.TextField(db_column='Underwater', blank=True, null=True)  # Field name made lowercase.
    urban = models.TextField(db_column='Urban', blank=True, null=True)  # Field name made lowercase.
    other_plane = models.TextField(db_column='Other Plane', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    page = models.TextField(db_column='Page', blank=True, null=True)  # Field name made lowercase.

    def livesInEnvironment(self, environment_name: str):
        match environment_name.lower().strip():
            case "arctic":
                return True if self.arctic else False
            case "coastal":
                return True if self.coastal else False
            case "desert":
                return True if self.desert else False
            case "forest":
                return True if self.forest else False
            case "grassland":
                return True if self.grassland else False
            case "hill":
                return True if self.hill else False
            case "mountain":
                return True if self.mountain else False
            case "swamp":
                return True if self.swamp else False
            case "underdark":
                return True if self.underdark else False
            case "underwater":
                return True if self.underwater else False
            case "urban":
                return True if self.urban else False
            case "other_plane":
                return True if self.other_plane else False
            
    def __str__(self):
        return self.name

