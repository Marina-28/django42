from django import forms

class RemoveMoveForm(forms.Form):
    title = forms.ChoiceField()

    def __init__(self, choices, *args, **kwargs):
        super(RemoveMoveForm, self).__init__(*args, **kwargs)
        self.fields['title'].choices = choices