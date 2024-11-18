# from django.forms import ModelForm, forms
from django import forms
from .models import RequestData
class RequestForm(forms.ModelForm):
    class Meta:
        model = RequestData
        fields = ["category","item_name","request_num","stock_num", "address", "name"]
        widgets = {
            'category': forms.RadioSelect(choices=[
                ('食品', '食品'),
                ('日用品', '日用品'),
                ('医療品', '医療品'),
                ('子供用品', '子供用品'),
                ('女性用品', '女性用品'),
                ('高齢者用品', '高齢者用品')
            ]),
            'item_name': forms.Select(choices=[
                ('選択肢1', '選択肢1'),
                ('選択肢2', '選択肢2'),
                ('選択肢3', '選択肢3'),
                ('選択肢4', '選択肢4'),
                ('選択肢5', '選択肢5')
            ]),
            'request_num': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_num': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
