from django import forms

class ChatForm(forms.Form):
    message = forms.CharField(label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Type your message...',
            'rows': 1
        })
    )

