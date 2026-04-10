from django.db import models

class Pizza(models.Model):
    name = models.CharField(
        "Название пиццы",
        help_text="Указывайте корректное и уникальное название!",
        max_length=100
    )
    description = models.TextField("Описание пиццы", blank=True, null=True)
    price = models.DecimalField("Цена", max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = "Пицца"
        verbose_name_plural = "Пиццы"

    def __str__(self):
        return self.name