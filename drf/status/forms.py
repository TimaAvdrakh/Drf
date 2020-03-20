from django import forms

from .models import Status

class StatusFrom(forms.ModelForm):
    class Meta:
        model = Status
        fields = [
            'users',
            'content',
            'image',
        ]
    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content =  data.get('content',None)
        if content == "":
            content = None
        image = data.get('image',None)
        if content is None or image is None:
            raise forms.ValidationError('Content or Image error')
        return super().clean(*args,**kwargs)


