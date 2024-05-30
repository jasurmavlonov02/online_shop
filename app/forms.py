from django import forms
from app.models import Product, Comment, Order

from phonenumber_field.formfields import PhoneNumberField


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField()
    image = forms.ImageField()
    rating = forms.ChoiceField(choices=Product.RatingChoices.choices)
    discount = forms.IntegerField()


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ['name', 'description', 'price', 'image', 'rating', 'discount']
        exclude = ()


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['full_name', 'email', 'message']


class OrderModelForm(forms.ModelForm):
    phone_number = PhoneNumberField(region='UZ')

    class Meta:
        model = Order
        fields = ['name', 'phone_number']
