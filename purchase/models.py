from django.db import models


class Purchase(models.Model):
    """ Model by save data from a purchase """

    class Meta:
        app_label = 'purchase'
        ordering = ('pk', )

    begin_date = models.DateField()
    end_date = models.DateField()
    destination = models.CharField(max_length=50)
    product_id = models.PositiveIntegerField()
    insured_cpf = models.CharField(max_length=14)
    insured_name = models.CharField(max_length=100)
    insured_birth = models.DateField()
    card_name = models.CharField(max_length=100)
    card_cpf = models.CharField(max_length=14)
    card_number = models.CharField(max_length=16)
    card_mouth = models.CharField(max_length=2)
    card_year = models.CharField(max_length=4)
    card_cvv = models.CharField(max_length=4)
    buy_name = models.CharField(max_length=100)
    buy_email = models.CharField(max_length=100)
    buy_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.insured_name
