__author__ = 'dev'
from django import forms



class ShoppingCartForm(forms.Form):
    cartitems = forms.Textarea()
    def __init__(self, request=None, *args, **kwargs):
        """ override the default so we can set the request """
        self.request = request
        super(ShoppingCartForm, self).__init__(*args, **kwargs)

class RequestForQuoteForm(forms.Form):
    FirstName = forms.CharField(widget=forms.TextInput)
    LastName = forms.CharField(widget=forms.TextInput)
    Address1 = forms.CharField(widget=forms.TextInput)
    Address2 = forms.CharField(widget=forms.TextInput)
    City = forms.CharField(widget=forms.TextInput)
    Zip = forms.CharField(widget=forms.TextInput)
    Org = forms.CharField(widget=forms.TextInput)
    fipsorder = forms.CharField(widget=forms.Textarea)
    Contact = forms.ChoiceField(widget=forms.RadioSelect)

    Country = forms.ChoiceField(widget=forms.Select)
    #State = forms.TextInput()
    State = forms.ChoiceField(widget=forms.Select)
    # state = forms.ChoiceInput()
    Email = forms.EmailField(widget=forms.EmailInput)
    Phone = forms.CharField(widget=forms.TextInput)
    #order = forms.Textarea()
    def __init__(self, request=None, *args, **kwargs):
        """ override the default so we can set the request """
        self.request = request
        super(RequestForQuoteForm, self).__init__(*args, **kwargs)


class BuyForm(forms.Form):
    FirstName = forms.CharField(widget=forms.TextInput)
    LastName = forms.CharField(widget=forms.TextInput)
    Address1 = forms.CharField(widget=forms.TextInput)
    Address2 = forms.CharField(widget=forms.TextInput)
    City = forms.CharField(widget=forms.TextInput)
    Org = forms.CharField(widget=forms.TextInput)
    fipsorder = forms.CharField(widget=forms.Textarea)
    Country = forms.MultipleChoiceField(widget=forms.Select)
    #State = forms.TextInput()
    State = forms.MultipleChoiceField(widget=forms.Select)
    # state = forms.ChoiceInput()
    Email = forms.EmailField(widget=forms.EmailInput)
    Phone = forms.CharField(widget=forms.TextInput)
    #order = forms.Textarea()
    def __init__(self, request=None, *args, **kwargs):
        """ override the default so we can set the request """
        self.request = request
        super(RequestForQuoteForm, self).__init__(*args, **kwargs)


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()