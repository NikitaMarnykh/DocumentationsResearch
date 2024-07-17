from django.db import models

# Create your models here.


# Модель котировок
class Quote(models.Model):
    name: str = models.CharField(null=False, blank=False, max_length=50)
    nominal: int = models.IntegerField(null=False, blank=False)
    num_code: int = models.CharField(null=False, blank=False, max_length=5)
    char_code: int = models.CharField(null=False, blank=False, max_length=5)
    vunit_rate: float = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name, self.nominal, self.num_code, self.char_code, self.vunit_rate
