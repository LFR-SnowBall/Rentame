from django import forms

class ContactoForm(forms.Form):
    persona=forms.CharField(label="Persona",
    required=True,widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':'Ingresa un Correo o Telefono'}),max_length=200)

    comentario=forms.CharField(label="mensaje",
    required=True,widget=forms.Textarea(attrs={
        'class':'form-control','placeholder':'Ingresa un Comentario'}),max_length=200)