from django.db import models


class Staff(models.Model):
    idnumber = models.CharField('Tабельный номер', max_length=5)
    email = models.EmailField('E-mail')
    name = models.CharField('ФИО', max_length=50)
    number = models.CharField('Номер', max_length=12)
    major = models.CharField('Должность', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
