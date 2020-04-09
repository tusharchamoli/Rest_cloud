from django.db import models


class housingsociety(models.Model):
    societyname = models.CharField(max_length=10)
    address = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    housingid = models.IntegerField()
    noofcitizens = models.IntegerField()

    def __str__(self):
        return self.societyname


class blocks(models.Model):
    blockname = models.CharField(max_length=10)
    citizens = models.IntegerField()
    apartments = models.IntegerField()

    def __str__(self):
        return self.blockname


class apartment(models.Model):
    apartmentno = models.CharField(max_length=10)
    nameofowner = models.CharField(max_length=30)
    sizeoftheapartment = models.CharField(max_length=10)

    def __str__(self):
        return self.nameofowner


class citizens(models.Model):
    citizenname = models.CharField(max_length=30)
    citizenage = models.IntegerField()
    citizenIDtype = models.CharField(max_length=20)
    citizenID = models.CharField(max_length=20)

    def __str__(self):
        return self.citizenname


