from django import forms# создаем , импортируем
# это формы для HTML

class OrderForm(forms.Form):# создаем класс, импортируем в views
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form_control'}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form_control'}))
