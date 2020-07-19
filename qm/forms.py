from django import forms

class spreadForm(forms.Form):
    SHEET_CHOICES = [('Master_qm', 'Master'), ('Tent_db', 'Tent')]
    sheet = forms.ChoiceField(widget=forms.RadioSelect, choices=SHEET_CHOICES)

    ACTION_CHOICES = [('get_cell', 'SEARCH for cell'), 
                    ('get_row', 'SEARCH for row'), 
                    ('update_cell', 'EDIT cell'),
                    ('insert_row', 'EDIT row'),]
    action = forms.ChoiceField(widget=forms.RadioSelect, choices=ACTION_CHOICES)

    row = forms.CharField()
    col = forms.CharField()
    new = forms.CharField()
    search_value = forms.CharField()


    def clean(self):
        cleaned_data = super(spreadForm, self).clean()
        sheet = cleaned_data.get('sheet')
        if not sheet:
            raise forms.ValidationError('You have to write something!')