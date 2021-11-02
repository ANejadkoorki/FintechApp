from django import forms
from django.core.validators import FileExtensionValidator

file_format_validator = FileExtensionValidator(
    allowed_extensions=['csv', 'xlsx', 'xlsm', 'xls', 'xml'],
    message='please import files with these formats : .csv, .xls, .xlsx, .xlsm, .xml',
)


class ExcellFileForm(forms.Form):
    # just get Excel file formats : .csv, .xls, .xlsx, .xlsm, .xml'
    excel_file = forms.FileField(
        required=True,
        validators=[file_format_validator],
        )
