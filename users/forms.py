from allauth.account.forms import SignupForm
from django import forms
from users.models import User


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=50, label='First Name')
    last_name = forms.CharField(max_length=50, label='Last Name')
    social_security_no = forms.CharField(max_length=20, label='Social Security Number')
    phone_no = forms.CharField(max_length=15, label='Phone Number')
    address = forms.CharField(max_length=255, label='Address')
    post_code = forms.CharField(max_length=10, label='Post Code')
    city = forms.CharField(max_length=50, label='City')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name',
                  'last_name', 'social_security_no', 'phone_no', 'address',
                  'post_code', 'city')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.social_security_no = self.cleaned_data['social_security_no']
        user.phone_no = self.cleaned_data['phone_no']
        user.address = self.cleaned_data['address']
        user.post_code = self.cleaned_data['post_code']
        user.city = self.cleaned_data['city']
        user.save()
        return user
