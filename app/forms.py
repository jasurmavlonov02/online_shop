from django import forms
from app.models import Product, Comment


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
