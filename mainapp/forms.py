from django import forms
from captcha.widgets import ReCaptchaV2Checkbox
from captcha.fields import ReCaptchaField

class CaptchaForm(forms.Form):
    text = forms.CharField()
    #captcha field ... 
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)