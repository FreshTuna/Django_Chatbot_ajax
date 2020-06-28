from django import forms


class NewForm(forms.Form):
    question = forms.CharField(
        error_messages={
            'required': 'Add your question.'
        },
        max_length=100, label="Question")
    answer = forms.CharField(
        error_messages={
            'required': 'Add your answer.'
        },
        widget=forms.Textarea, label="Answer")