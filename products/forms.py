from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput)
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

    def clean(self):
        cleaned_data = super().clean()
        is_shoe = cleaned_data.get("is_shoe")
        has_sizes = cleaned_data.get("has_sizes")

        if is_shoe and has_sizes:
            raise ValidationError(
                "product cannot have 2 types of sizes at the same time.")

        return cleaned_data
