from django import forms
from .models import *

class get_data_chartForm(forms.ModelForm):

	class get_data_chart:
		model = DataSet
		exclude = [""]
			
