from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Corrected queryset here
        self.fields['categories'].queryset = Category.objects.all()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput)

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        # You can remove this queryset definition since it's overridden in
        # __init__
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def clean(self):
        cleaned_data = super().clean()
        is_shoe = cleaned_data.get("is_shoe")
        has_sizes = cleaned_data.get("has_sizes")

        if is_shoe and has_sizes:
            raise ValidationError(
                "A product cannot have both types of sizes at the same time.")

        return cleaned_data
