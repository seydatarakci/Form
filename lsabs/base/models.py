from django.db import models

#Choices
CATEGORY_CHOICES = [
        ('İnşaat işleri', (
            (16, 'Kazı-dolgu'),
            (11, 'Kaba beton'),
            (12, 'Mimari işler'),
            (13, 'Fore Kazık'),
            (14, 'Dikey sondaj '),
            (15, 'Yatay sondaj'),
            (18, 'Enjeksiyon işleri'),
            (18, 'Kazık işleri'),
            (18, 'Kırma-eleme işleri'),

        )),
        ('Metal işleri', (
            (21, 'Kalıp imalat'),
            (22, 'Çelik konstrüksiyon'),
        )),
        ('Mekanik sistem', (
            (31, 'Groceries'),
            (32, 'Restaurants'),
        )),
        ('Elektrik sistem', (
            (41, 'Groceries'),
            (52, 'Restaurants'),
        )),
        ('ISG işleri', (
            (61, 'OSGB'),
            (62, 'Yüksekte imalat (iple erşim, güvanlik ağı vs'),
        )),
        ('Mal ', (
            (61, 'OSGB'),
            (62, 'Yüksekte imalat (iple erşim, güvanlik ağı vs'),
        )),
         ('Filo', (
             (10,'Araç Filo'),
         )),
    ]

# Create your models here.

class Firm(models.Model):
    title = models.CharField(max_length=200)
    category = models.SmallIntegerField(choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title
    
   
class Subsidiary(Firm):
    axcode = models.CharField(max_length=3)

    def __str__(self):
        return self.axcode
    

class Project(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(Subsidiary, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
