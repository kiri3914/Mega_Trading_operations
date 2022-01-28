from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    home_number = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адресa'

    def __str__(self):
        return self.country


class Director(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Директор'
        verbose_name_plural = 'Директора'

    def __str__(self):
        return self.last_name


class PaymentAccount(models.Model):
    title = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        verbose_name = 'Расчетный счет'
        verbose_name_plural = 'Расчетные счета'

    def __str__(self):
        return self.title


class ClientCompany(models.Model):
    title = models.CharField(max_length=100)
    director = models.OneToOneField(Director, on_delete=models.CASCADE)
    payment_account = models.ForeignKey(PaymentAccount, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Копании'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(ClientCompany, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class UnitOfMeasurement(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        verbose_name = 'Единица Измерения'
        verbose_name_plural = 'Единицы Измерения'

    def __str__(self):
        return self.title


class Sale(models.Model):
    client_company = models.ForeignKey(ClientCompany, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)
    sale_date = models.DateField(auto_now_add=False)
    unit_of_measurement = models.ForeignKey(UnitOfMeasurement, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'

    def __str__(self):
        return f"Продажа {self.product} от {self.client_company.title}"
