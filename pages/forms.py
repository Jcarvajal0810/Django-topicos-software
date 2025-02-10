from django import forms
from django.core.exceptions import ValidationError

class ProductForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    price = forms.DecimalField(
        required=True, 
        min_value=0.01, 
        error_messages={"min_value": "Invalid price, please enter another price."}
    )
    description = forms.CharField(widget=forms.Textarea, required=False)

    def clean_price(self):
        price = self.cleaned_data.get("price")

        if price is None:
            raise ValidationError("The price field is required.", code="required")

        if price <= 0:
            raise ValidationError("Invalid price, please enter another price.", code="invalid")

        return price
