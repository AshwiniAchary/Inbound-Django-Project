from django import forms
from .models import Pallet, ProductionLine, MaterialMaster

# class ReceiptForm(forms.ModelForm):
#     production_line = forms.ModelChoiceField(queryset=ProductionLine.objects.all())
#     process_order_number = forms.IntegerField()
#     date = forms.DateField(widget=forms.SelectDateWidget())
#     sku_code = forms.ModelChoiceField(queryset=MaterialMaster.objects.all())
#     batch_number = forms.CharField(max_length=100)
#     process_order_qty = forms.IntegerField()
    
#     class Meta:
#         model = Pallet
#         fields = ['production_line', 'process_order_number', 'date', 'sku_code', 'batch_number', 'process_order_qty']

class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Pallet
        fields = '__all__'  # Or explicitly list the fields including 'pallet_qty'
