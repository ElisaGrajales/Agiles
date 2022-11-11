from django import forms
class FormularioMedico(forms.Form):

    TIPOAFILIADOS=(
        (1,'Cotizante'),
        (2,'Beneficiario'),
    )
    REGIMEN=(
        (1,'Contributivo'),
        (2,'Subsidiado'),
        (3,'Excepción'),
        (4, 'Especial'),
        (5, 'No asegurado'), 
        (6, 'Indeterminado'),
        (7, 'Póliza')
    )
    GRUPOSINGRESOS=(
        (1,'CATEGORÍA A'),
        (2,'CATEGORÍA B'),
        (3,'CATEGORÍA C')
    )

    nombre=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=15

    ) 
    apellidos=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=35
    )
    cedula=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=10
    )
    
    tipoafiliado=forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices=TIPOAFILIADOS
    )
    regimen=forms.ChoiceField(
       widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices=REGIMEN
    )

    grupoingreso =forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices=GRUPOSINGRESOS
    ) 