from django import forms


class NicknameForm(forms.Form):
    nickname = forms.CharField(
            max_length=30,
            initial="Stranger",
            widget=forms.TextInput(attrs={"placeholder": "nickname"}),
        )