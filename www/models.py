from django.db import models

class Typo(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Denomination(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DateReference(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class site(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class sportSite(models.Model):
    departement = models.IntegerField()
    commune = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    code_postal = models.CharField(max_length=10)
    longitude = models.FloatField()
    latitude = models.FloatField()
    informations_d_acces_en_transport_en_commun = models.TextField(
        null=True,
        blank=True
    )
    appellation = models.CharField(max_length=200)
    typologie = models.ManyToManyField(Typo, blank=True)
    denomination = models.ManyToManyField(Denomination, blank=True)
    date_s_de_reference = models.ManyToManyField(DateReference, blank=True)
    datation = models.CharField(max_length=100)
    periode_de_construction = models.CharField(max_length=100)
    historique_et_description = models.TextField()
    credits = models.CharField(max_length=200)
    url_image = models.URLField()
    adresse_com = models.CharField(max_length=200)
    site_olympique = models.ForeignKey(
        site,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
    
    
class Meta:
    verbose_name = "Site sportif emblématique"
    verbose_name_plural = "Sites sportifs emblématiques"

def __str__(self):
    return self.appellation
