from django import forms
from .models import Employees


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = "__all__"

        # def __init__(self, *args, **kwargs):
        #     super(EmployeeForm, self).__init__(*args, **kwargs)
        #     self.fields['age'].required = False
