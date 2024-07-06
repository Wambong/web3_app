from django import forms

class AddressForm(forms.Form):
    address = forms.CharField(label='введите адрес', max_length=182)

class AddressesForm(forms.Form):
    addresses = forms.CharField(label='введите несколько  адресов, каждый с новой строки ', widget=forms.Textarea)

class TopNForm(forms.Form):
    n = forms.IntegerField(label='введите целое число', min_value=1)

class TopNFormInfo(forms.Form):
    n = forms.IntegerField(label='введите целое число', min_value=1)

class TokenAddressForm(forms.Form):
    token_address = forms.CharField(label='введите адрес токена', max_length=432)
