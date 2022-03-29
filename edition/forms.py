from dataclasses import field
from statistics import mode
from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), label="Titulo")
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}), label="Contenido")
    status = forms.BooleanField(
        widget=forms.CheckboxInput(), required=False, label="Estatus")
    author = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), label="Autor")

    class Meta:
        model = Blog
        fields = ['title', 'content', 'status', 'author']
