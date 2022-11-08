from django.contrib.admin.forms import AdminPasswordChangeForm
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from Profile.models import *
from Regiony.models import *
from django.core import validators
from django.forms import CharField
from bootstrap_modal_forms.forms import BSModalModelForm
class SlugField(CharField):
    default_validators = [validators.validate_slug]


class AddNewUserPERSON(forms.ModelForm):
    pesel = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control"}), label="Pesel", required=False,)
    npwz = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control"}), label="Numer prawa wykonywania zawodu")
    phone = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control"}), label="Telefon komórkowy", )
    date_brith = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control"}), label="Data Urodzenia")
    regional_woj = forms.ModelChoiceField(queryset=Regional.objects.all() ,widget=forms.Select(attrs={"class": "form-control"}), label="Województwo", required=False,)
    regional_city = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label="Miasto", required=False,)
    str_number = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label="Numer budynku", required=False,)
    str_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label="Nazwa ulicy", required=False,)
    str_number_one = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label="Numer pomieszczenia",required=False, )
    groupadd = forms.ModelChoiceField(queryset=Group.objects.all() ,widget=forms.Select(attrs={"class": "form-control"}), label="Grupa")
    class Meta:
        model = Personal_med
        fields = '__all__'
class AddNewUser(UserCreationForm):
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label="Nazwisko")
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label="Imię")
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label="Nazwa użytkownika")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Hasło")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Potwierdz hasło")
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}), label="E-mail")

    class Meta:
        model = User
        fields = ("username", 'last_name', 'first_name', 'email', 'password1' ,'password2', 'groups')


class PersonForms(forms.ModelForm):
    PESELANS = (
        ('0', ('TAK')),
        ('1', ('NIE')),
    )
    NAMEID = (
        ('0', ("Brak")),
        ('1', ("EKUZ")),
        ('2', ("Dowód osobisty")),
        ('3', ("Paszport")),

    )

    peselN = forms.ChoiceField(widget=forms.Select(
        attrs={"class": "form-control", "onchange": "show(this.value)", "id": "click", "name": "radioSelect"}),
                               label="Czy posiadasz PESEL?", initial=0, choices=PESELANS, )

    pesel = forms.CharField(validators=[validators.validate_slug], widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": 'Twój pesel', 'oninput': 'limit_input()',
               'id': 'pesel_field', }), required=False, label="Wprowadź swój Pesel:", max_length=11)
    IDname = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "form-control", "placeholder": "Wybierz dokument uprawniający"}),
        required=False, choices=NAMEID, label="Wybierz dokument uprawniający(opcjonalne w razie braku numeru PESEL)")
    IDnumber = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Wprowadz numer dokumentu(opcjonalne)"}),
        required=False, label="Wpisz numer dokumentu uprawniającego (opcjonalne w razie braku numeru PESEL)")
    phone = forms.CharField(widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": 'Telefon', 'oninput': 'limit_input()', 'id': 'phone_field', }),
                            label="Numer Telefonu:")
    date_brith = forms.DateField(widget=forms.NumberInput(attrs={"class": "form-control", 'type': 'date'}),
                                 label="Data Urodzin:")
    regional_woj = forms.ModelChoiceField(queryset=Regional.objects.all(), initial=0,
                                          widget=forms.Select(attrs={"class": "form-control"}),
                                          label="Wybierz Województwo")
    regional_city = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "np. Wrocław", "class": "form-control"}), label="Miasto:")
    post = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "00-000", "class": "form-control"}),
                           label="Kod pocztowy:")
    str_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "np. 3-maja", "class": "form-control"}),
                               label="Ulica:")
    str_number = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "np. 14a", "class": "form-control"}),
                                 label="Numer budynku:")
    str_number_one = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "np. 33", "class": "form-control"}),
                                     label="Numer mieszkania:")
    doc = forms.FileField(widget=forms.FileInput(attrs={"class": "form-control"}), label="Skan dokumentu:")

    class Meta:
        model = Personal
        fields = (
        'date_brith', 'pesel', 'peselN', 'IDname', 'IDnumber', 'phone', 'regional_woj', 'regional_city', 'post',
        'str_name', 'str_number', 'str_number_one', 'doc')

    def __init__(self, pk, *args, **kwargs):
        super(PersonForms, self).__init__(*args, **kwargs)
        self.fields['first_name'].queryset = User.objects.filter(id=pk)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].queryset = User.objects.filter(id=pk)
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['iduser'].queryset = User.objects.filter(id=pk)
        self.fields['iduser'].widget.attrs['class'] = 'form-control'
    def clean(self):
        super(PersonForms, self).clean()

        pesel = self.cleaned_data.get('pesel')
        phone = self.cleaned_data.get('phone')
        IDnumber = self.cleaned_data.get('IDnumber')
        try:
            if (len(pesel) < 11 and len(pesel) != 0):
                self._errors['pesel'] = self.error_class([
                    'Pesel pownien składać się z 11 cyfr!'
                ])
        except:
            if len(IDnumber) > 1:
                self._errors['IDnumber'] = self.error_class([
                    'Wprowadź poprawne dane'
                ])
            return self.cleaned_data
        if len(phone) < 9:
            self._errors['phone'] = self.error_class([
                'Błędy numer telefonu'
            ])
        return self.cleaned_data
class CreateUserForms(UserCreationForm):
   class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email', 'password1')

class DocUSER(forms.ModelForm):
    doc = forms.FileField(widget=forms.FileInput(attrs={"class": "form-control"}), label="Skan dokumentu:")
    class Meta:
        model = Personal
        fields = ['doc']

class CreatePersonalForms(forms.ModelForm):
    PESELANS = (
        ('0', ('TAK')),
        ('1', ('NIE')),
    )
    NAMEID = (
        ('0', ("Brak")),
        ('1', ("EKUZ")),
        ('2', ("Dowód osobisty")),
        ('3', ("Paszport")),

              )


    peselN = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control","onchange": "show(this.value)"  ,"id": "click" , "name": "radioSelect"}), label="Czy posiadasz PESEL?", initial=0 , choices=PESELANS,)

    pesel = forms.CharField(validators=[validators.validate_slug], widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": 'Twój pesel', 'oninput': 'limit_input()', 'id': 'pesel_field',  }),required=False,  label="Wprowadź swój Pesel:", max_length=11)
    IDname = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control", "placeholder": "Wybierz dokument uprawniający"}),required=False,  choices=NAMEID, label="Wybierz dokument uprawniający(opcjonalne w razie braku numeru PESEL)" )
    IDnumber = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Wprowadz numer dokumentu(opcjonalne)"}),required=False, label="Wpisz numer dokumentu uprawniającego (opcjonalne w razie braku numeru PESEL)" )
    phone = forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder": 'Telefon','oninput':'limit_input()', 'id': 'phone_field', }), label="Numer Telefonu:")
    date_brith = forms.DateField(widget=forms.NumberInput(attrs={"class":"form-control",'type': 'date'}), label="Data Urodzin:")
    regional_woj = forms.ModelChoiceField(queryset=Regional.objects.all(), initial=0, widget=forms.Select(attrs={"class":"form-control"}), label="Wybierz Województwo" )
    regional_city = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "np. Wrocław", "class":"form-control"}), label="Miasto:")
    post = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "00-000", "class":"form-control"}), label="Kod pocztowy:")
    str_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "np. 3-maja", "class":"form-control"}), label="Ulica:")
    str_number = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "np. 14a", "class":"form-control"}), label="Numer budynku:")
    str_number_one = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "np. 33", "class":"form-control"}), label="Numer mieszkania:")
    doc = forms.FileField(widget=forms.FileInput(attrs={"class":"form-control"}), label="Skan dokumentu:")
    class Meta:
        model= Personal
        fields = ('date_brith' ,'pesel', 'peselN', 'IDname', 'IDnumber', 'phone', 'regional_woj', 'regional_city', 'post' , 'str_name' ,'str_number', 'str_number_one', 'doc')
    def clean(self):
        super(CreatePersonalForms, self).clean()

        pesel = self.cleaned_data.get('pesel')
        phone = self.cleaned_data.get('phone')
        IDnumber = self.cleaned_data.get('IDnumber')
        try:
            if (len(pesel) < 11 and len(pesel) != 0):
                self._errors['pesel']= self.error_class([
                'Pesel pownien składać się z 11 cyfr!'
            ])
        except:
            if len(IDnumber) > 1:
                self._errors['IDnumber'] = self.error_class([
                    'Wprowadź poprawne dane'
                ])
            return self.cleaned_data
        if len(phone) < 9:
            self._errors['phone'] = self.error_class([
                'Błędy numer telefonu'
            ])
        return self.cleaned_data


class EditPersonalForms(forms.ModelForm):
    PESELANS = (
        ('0', ('TAK')),
        ('1', ('NIE')),
    )
    NAMEID = (
        ('0', ("Brak")),
        ('1', ("EKUZ")),
        ('2', ("Dowód osobisty")),
        ('3', ("Paszport")),

              )



    pesel = forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": 'Twój pesel', 'id': 'disabledNumberInput'}), label="Wprowadź swój Pesel:", max_length=11)
    peselN = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control", "name": "radioSelect"}), label="Czy posiadasz PESEL?", initial=0 , choices=PESELANS,)
    IDname = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control", "placeholder": "Wybierz dokument uprawniający"}),required=False,  choices=NAMEID, label="Wybierz dokument uprawniający(opcjonalne w razie braku numeru PESEL)" )
    IDnumber = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Wprowadz numer dokumentu(opcjonalne)"}),required=False, label="Wpisz numer dokumentu uprawniającego (opcjonalne w razie braku numeru PESEL)" )
    phone = forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder": 'Telefon'}), label="Numer Telefonu:")
    date_brith = forms.DateField(widget=forms.NumberInput(attrs={"class":"form-control",'type': 'date'}), label="Data Urodzin:")
    regional_woj = forms.ModelChoiceField(queryset=Regional.objects.all(), initial=0, widget=forms.Select(attrs={"class":"form-control"}), label="Wybierz Województwo" )
    regional_city = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "np. Wrocław", "class":"form-control"}), label="Miasto:")
    post = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "00-000", "class":"form-control"}), label="Kod pocztowy:")
    str_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "np. 3-maja", "class":"form-control"}), label="Ulica:")
    str_number = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "np. 14a", "class":"form-control"}), label="Numer budynku:")
    str_number_one = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "np. 33", "class":"form-control"}), label="Numer mieszkania:")
    doc = forms.FileField(widget=forms.FileInput(attrs={"class":"form-control"}), label="Skan dokumentu:")
    class Meta:
        model= Personal
        fields = ('date_brith' ,'pesel', 'peselN', 'IDname', 'IDnumber', 'phone', 'regional_woj', 'regional_city', 'post' , 'str_name' ,'str_number', 'str_number_one', 'doc')
class AdressForm(forms.ModelForm):
    id_reg = forms.ModelChoiceField(queryset=Regional.objects.all(), initial=0, widget=forms.Select(attrs={"class":"form-control"}), label="Wybierz Województwo" )
    name_city = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "np. Wrocław", "class":"form-control"}), label="Miasto:")

    class Meta:
        model = City
        fields = ('id_reg', 'name_city')



class CreatePersonalMedForms(forms.ModelForm):
    class Meta:
        model= Personal_med
        fields = ('pesel', 'npwz' , 'phone', 'regional_woj', 'regional_city','str_name' ,'str_number', 'str_number_one')

class EditUserForms(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", 'id': 'disabledTextInput'}), label="Imię")
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}), label="Nazwisko")
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}), label="Email")
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email']
class EditUserFormsADMIN(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", 'id': 'disabledTextInput'}), label="Nazwa użytkownika")
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", 'id': 'disabledTextInput'}), label="Imię")
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}), label="Nazwisko")
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
class EditPersonalFormsDATA(forms.ModelForm):
    PESELANS = (
        ('0', ('TAK')),
        ('1', ('NIE')),
    )
    NAMEID = (
        ('0', ("Brak")),
        ('1', ("EKUZ")),
        ('2', ("Dowód osobisty")),
        ('3', ("Paszport")),

              )



    pesel = forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": 'Twój pesel', 'id': 'disabledNumberInput'}), label="PESEL:", max_length=11)
    peselN = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control", "name": "radioSelect"}), label="Status PESEL", initial=0 , choices=PESELANS,)
    IDname = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control", "placeholder": "Wybierz dokument uprawniający"}),required=False,  choices=NAMEID, label="Wybierz dokument uprawniający(opcjonalne w razie braku numeru PESEL)" )
    IDnumber = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Wprowadz numer dokumentu(opcjonalne)"}),required=False, label="Wpisz numer dokumentu uprawniającego (opcjonalne w razie braku numeru PESEL)" )
    date_brith = forms.DateField(widget=forms.NumberInput(attrs={"class":"form-control",'type': 'date'}), label="Data Urodzin:")
    class Meta:
        model= Personal
        fields = ('date_brith' ,'pesel', 'peselN', 'IDname', 'IDnumber')

class EditPersonalFormsADRES(forms.ModelForm):


    regional_woj = forms.ModelChoiceField(queryset=Regional.objects.all(), initial=0, widget=forms.Select(attrs={"class":"form-control"}), label="Wybierz Województwo" )
    regional_city = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "np. Wrocław", "class":"form-control"}), label="Miasto:")
    post = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "00-000", "class":"form-control"}), label="Kod pocztowy:")
    str_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "np. 3-maja", "class":"form-control"}), label="Ulica:")
    str_number = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "np. 14a", "class":"form-control"}), label="Numer budynku:")
    str_number_one = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "np. 33", "class":"form-control"}), label="Numer mieszkania:")
    class Meta:
        model= Personal
        fields = ('regional_woj', 'regional_city', 'post' , 'str_name' ,'str_number', 'str_number_one')

class EditPersonalFormsCON(forms.ModelForm):

    phone = forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder": 'Telefon'}), label="Numer Telefonu:")


    class Meta:
        model= Personal
        fields = ('phone',)


class EditEmail(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}), label="Email")

    class Meta:
        model = User
        fields = ('email',)
class EditPERSONELFormsCON(forms.ModelForm):

    phone = forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder": 'Telefon'}), label="Numer Telefonu:")


    class Meta:
        model= Personal_med
        fields = ('phone',)
class EditPERSONELFormsDATA(forms.ModelForm):

    pesel = forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": 'Twój pesel', 'id': 'disabledNumberInput'}), label="PESEL:", max_length=11)
    npwz = forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": 'Twój pesel', 'id': 'disabledNumberInput'}), label="Numer prawa wykonywania zawodu:", max_length=11)
    date_brith = forms.DateField(widget=forms.NumberInput(attrs={"class":"form-control",'type': 'date'}), label="Data Urodzin:")
    class Meta:
        model= Personal_med
        fields = ('date_brith' ,'pesel', 'npwz')


class EditPERSONELFormsADRES(forms.ModelForm):
    regional_woj = forms.ModelChoiceField(queryset=Regional.objects.all(), initial=0,
                                          widget=forms.Select(attrs={"class": "form-control"}),
                                          label="Wybierz Województwo")
    regional_city = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "np. Wrocław", "class": "form-control"}), label="Miasto:")
    post = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "00-000", "class": "form-control"}),
                           label="Kod pocztowy:")
    str_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "np. 3-maja", "class": "form-control"}),
                               label="Ulica:")
    str_number = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "np. 14a", "class": "form-control"}),
                                 label="Numer budynku:")
    str_number_one = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "np. 33", "class": "form-control"}),
                                     label="Numer mieszkania:")

    class Meta:
        model = Personal_med
        fields = ('regional_woj', 'regional_city', 'post', 'str_name', 'str_number', 'str_number_one')



