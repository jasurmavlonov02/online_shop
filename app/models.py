from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Kategoriyalar'


class Product(models.Model):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')
    rating = models.PositiveIntegerField(choices=RatingChoices.choices, default=RatingChoices.zero)
    discount = models.IntegerField(default=0)
    category = models.ManyToManyField(Category, default=None)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    @property
    def discount_priced(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    class Meta:
        verbose_name_plural = 'Mahsulotlar'
        verbose_name = 'Mahsulot'


class Comment(models.Model):
    full_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.full_name} => by comment'

    class Meta:
        verbose_name_plural = 'Izohlar'


class Order(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, related_name='orders', null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.phone_number
