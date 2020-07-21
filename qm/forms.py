from django import forms

class spreadForm(forms.Form):
    SHEET_CHOICES = [('Master_qm', 'Master'), ('Tent_db', 'Tent')]
    sheet = forms.ChoiceField(widget=forms.RadioSelect, choices=SHEET_CHOICES)

    ACTION_CHOICES = [('get_row', 'Search for item'), 
                    ('update_cell', 'Change item\'s attributes'),
                    ('insert_row', 'New item'),]
    action = forms.ChoiceField(widget=forms.RadioSelect, choices=ACTION_CHOICES)

    Item = forms.CharField()
    Attribute = forms.CharField()
    Value = forms.CharField()


    def clean(self):
        cleaned_data = super(spreadForm, self).clean()
        sheet = cleaned_data.get('sheet')
        if not sheet:
            raise forms.ValidationError('You have to write something!')