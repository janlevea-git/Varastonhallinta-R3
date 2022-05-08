from django.db import models

from kayttajat.models import Kayttaja

class Tuoteryhma(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nimi = models.CharField(max_length=50, null=False, verbose_name="Nimi")
    lisaaja = models.ForeignKey(
        Kayttaja, null=False, on_delete=models.PROTECT, verbose_name="Lisääjä"
    )
    lisaysaika = models.DateTimeField(auto_now_add=True, null=False, editable=False, verbose_name="Lisäysaika")
    class Meta:
        verbose_name = "Tuoteryhmä"
        verbose_name_plural = "Tuoteryhmät"
    def __str__(self):
        return f"id({self.id}) {self.nimi}"

# TODO: Viivakoodit kuvana tietokantaan - svg järkevin? - CODE 128 - Tai tiedostona? ImageField
# TODO: Tuotekuvat ImageField
# TODO: viivakoodi(_img) toiminnallisuus - python barcode
class TuoteBase(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    
    tuoteryhma = models.ForeignKey(
        Tuoteryhma, null=False, on_delete=models.PROTECT, verbose_name="Tuoteryhmä")
    nimike = models.CharField(
        max_length=50, null=False, verbose_name="Nimike")

    maara = models.IntegerField(verbose_name="Määrä")

    hankintapaikka = models.CharField(max_length=50, null=False, verbose_name="Hankintapaikka")
    kustannuspaikka = models.CharField(max_length=10, null=False, verbose_name="Kustannuspaikka")

    tuotekuva = models.BinaryField(null=False, verbose_name="Tuotekuva")

    viivakoodi_string = models.CharField(max_length=30, null=False, verbose_name="Viivakoodi")
    viivakoodi_img = models.BinaryField(null=False, verbose_name="Viivakoodi") # TODO: ImageField?

    lisaaja = models.ForeignKey(
        Kayttaja, null=False, on_delete=models.PROTECT, verbose_name="Lisääjä"
    )
    lisaysaika = models.DateTimeField(auto_now_add=True, null=False, editable=False, verbose_name="Lisäysaika")
    class Meta:
        verbose_name = "Tuote"
        verbose_name_plural = "Tuotteet"
        abstract = True
        ordering = ['tuoteryhma', 'nimike']

    def __str__(self):
        return f"id({self.id}) {self.tuoteryhma.nimi}/{self.nimike}"

class Tuote(TuoteBase):
    pass

class TuoteOld(TuoteBase):
    tuoteryhma = models.ForeignKey(
        Tuoteryhma, null=False, on_delete=models.PROTECT, verbose_name="Tuoteryhmä",
        related_name="tuoteryhma_oli")
    
    lisaaja = models.ForeignKey(
        Kayttaja, null=False, on_delete=models.PROTECT, verbose_name="Lisääjä",
        related_name="lisaaja_oli")

    poistaja = models.ForeignKey(
        Kayttaja, null=False, on_delete=models.PROTECT, verbose_name="Poistaja")

    poistettu = models.DateTimeField(
        blank=True, null=True, editable=False, verbose_name="Poistettu")

    class Meta(TuoteBase.Meta):
        verbose_name = "Vanha tuote"
        verbose_name_plural = "Vanhat tuotteet"