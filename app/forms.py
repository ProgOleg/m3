from app.models import Orders, Comments
from django import forms


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['name', 't_number']


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["name", "description", "photo", "rating"]

    def clean_rating(self):
        if self.cleaned_data['rating']:
            self.cleaned_data['rating'] = int(self.cleaned_data['rating'])
        return self.cleaned_data['rating']
