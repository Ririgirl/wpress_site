from django import forms
from .models import Category, News

# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=200, label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     content = forms.CharField(label='Описание', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
#     is_published = forms.BooleanField(label='Опубликовать?', initial=True, widget= forms.CheckboxInput(attrs={'class': 'form-check-label'}))
#     create = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Выберите категорию', widget=forms.Select(attrs={'class': 'form-control'}))

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'create']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-label'}),
            'create': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
		    super().__init__(*args, **kwargs)
		    self.fields['create'].empty_label = 'Выберите категорию'