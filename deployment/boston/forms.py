from django import forms

class VariableForm(forms.Form):
    CRIM = forms.CharField(max_length=200)
    zn = forms.CharField(max_length=200)
    INDUS = forms.CharField(max_length=200)
    CHAS = forms.CharField(max_length=200)
    NOX = forms.CharField(max_length=200)
    RM = forms.CharField(max_length=200)
    AGE = forms.CharField(max_length=200)
    DIS = forms.CharField(max_length=200)
    RAD = forms.CharField(max_length=200)
    TAX = forms.CharField(max_length=200)
    PTRATIO = forms.CharField(max_length=200)
    B = forms.CharField(max_length=200)
    LSTAT = forms.CharField(max_length=200)
