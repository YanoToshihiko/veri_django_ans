from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='名前', max_length=100)
    email = forms.EmailField(label='メール')
    message = forms.CharField(label='内容', widget=forms.Textarea)
