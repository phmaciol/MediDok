from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import Group

from Personel.filters import Visit_filters
from Profile.models import *
from Regiony.models import *
from Pacjent.models import *
from Personel.models import *
from Personel.forms import *
from Profile.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from Profile.decorators import unauth_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm, AdminPasswordChangeForm, SetPasswordForm
from django.views.generic import UpdateView
from django.core.paginator import Paginator
# Create your views here.
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['personel'])
def deklPERS(request):

    show = Form_user.objects.all()
    context = {

        "show": show,

    }

    return render(request, '../templates/Worker/dekl.html', context)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['personel'])
def deklPERSone(request, pk):
    FormEditStatus =  modelformset_factory(Form_user, fields=('status',), extra=0)
    FormEditArea =  modelformset_factory(Form_user, fields=('remarks_person',), extra=0)
    form = FormEditStatus(queryset=Form_user.objects.filter(id=pk))
    forms = FormEditArea(queryset=Form_user.objects.filter(id=pk))
    show = Form_user.objects.filter(id=pk)
    if 'one' in request.POST:
        form=FormEditStatus(request.POST)
        form.save()
    if 'two' in request.POST:
        forms=FormEditArea(request.POST)
        forms.save()
    context = {

        "show": show,
        "form": form,
        "forms": forms,

    }

    return render(request, '../templates/Worker/deklone.html', context)
def formsPERS(request, pk):

    show = Form_user.objects.filter(patient_person_id=pk)

    context = {

        "show": show,


    }

    return render(request, '../templates/Worker/dekl.html', context)
def docPERS(request, pk):

    show = Document.objects.filter(author_person=pk)

    context = {

        "show": show,


    }

    return render(request, '../templates/Worker/dekl.html', context)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['personel'])
def deklREJ(request, pk, pi):
    test = dekl.objects.filter(idpac=pk).count()
    if test != 0:
        messages.info(request, "Ta deklaracja do tego pacjenta została już zarejestrowana usuń aby wprowadzić nową ")
        return redirect('showdekl')
    elif test == 0:
        idPACER = Personal.objects.get(id=pk)
        print(idPACER)
        idform = Form_user.objects.get(id=pi)
        print(idform)
        form = DEKLFORMS()
        if request.method == 'POST':
            form = DEKLFORMS(request.POST)
            forms = form.save(commit=False)
            forms.idfield = idform
            forms.idpac = idPACER
            forms = form.save()
            pk = forms.id
            return redirect('deklREJlek', pk)
        context = {

            "form": form,

        }

        return render(request, '../templates/Worker/deklrej.html', context)
@login_required(login_url='loginPage')  # blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['personel'])
def add_form(request):
    show=Form_all.objects.all()
    form = FORM_PERS()
    if request.method == 'POST':
        form = FORM_PERS(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formularz został dodany')
        else:
            messages.error(request, 'Formularz nie został zapisany')
    context = {
        'show': show,
        'form': form,
    }
    return render(request, '../templates/Worker/add_form.html', context)
def doc_show(request):
    show=Document.objects.all()

    context = {
        'show': show,

    }
    return render(request, '../templates/Worker/docshow.html', context)


@login_required(login_url='loginPage')  # blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['personel'])
def deklREJlek(request, pk):
    show = dekl.objects.get(id=pk)
    print(show.iddoc)
    if show.iddoc == None:
        place = doctor.objects.filter(unit=show.idunit)
        # print(place.name.id)
        form = EDITDEKLFORMS(instance=show)
        if request.method == 'POST':
            form = EDITDEKLFORMS(request.POST, instance=show)
            if form.is_valid():
                form.save()
                messages.info(request, "Lekarz został przypisany")
                return redirect('showdekl')
        context = {

            'form': form,
            'place': place,
            'show': show,

        }

        return render(request, '../templates/Worker/deklrejlek.html', context)
    elif show.iddoc != None:
        messages.info(request, "Lekarz został przypisany")
        return redirect('showdekl')
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['personel'])
def showdekl(request):
    show = dekl.objects.all()
    context = {
        'show': show,
    }
    return render(request, '../templates/Worker/deklshow.html', context)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['personel'])
def home_per(request):

    show = Personal.objects.filter(check=False).count()


    context = {
        "show": show,

    }

    return render(request, '../templates/Worker/home.html', context)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['personel'])
def visit_per(request):


    show = Visit.objects.all()
    context = {

        "show": show
    }

    return render(request, '../templates/Worker/visit_check.html', context)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['personel'])
def visit_one(request, pk):
    CHECKFORM = modelformset_factory(Visit, fields=('confirmation',), extra=0,)
    STATUSFORM = modelformset_factory(Visit, fields=('status',), extra=0,)
    TYPEFORM = modelformset_factory(Visit, fields=('type_visit',), extra=0,)
    TERMFORM = modelformset_factory(Visit, fields=('term',), extra=0,)

    show = Visit.objects.get(id=pk)
    term = Term_day.objects.filter(Q(work_place=show.organization) and Q(work_person=show.term.work_person))
    form= CHECKFORM(queryset=Visit.objects.filter(id=pk))
    forms= STATUSFORM(queryset=Visit.objects.filter(id=pk))
    formset = TERMFORM(queryset=Visit.objects.filter(id=pk))
    formtype = TYPEFORM(queryset=Visit.objects.filter(id=pk))
    vis = Visit.objects.filter(term__work_place=show.unity_id)

    terms = [show.term]
    actualy_date = timezone.now()
    for x in term:
        for y in vis:
            xy = True
            if y.term.id == x.id:
                print(x.work_date, x.work_time, "Zajęte")
                xy = False
                break
        if x.work_date > actualy_date.date() and xy:
            terms.append(x)
        if request.method == "POST":
            form = CHECKFORM(request.POST)
            forms = STATUSFORM(request.POST)
            formset = TERMFORM(request.POST)
            formtype = TYPEFORM(request.POST)
            if form.is_valid():
                form.save()
            if forms.is_valid():
                forms.save()
            if formset.is_valid():
                formset.save()
            if formtype.is_valid():
                formtype.save()
            return redirect('visit_one_PERS', pk)
        context={
            "show": show,
            "form": form,
            "forms": forms,
            "formset": formset,
            "formtype": formtype,
            "terms": terms,
    }

    return render(request, '../templates/Worker/visit_one.html', context)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['personel'])
def place(request):


    form = FORM_PLACE()
    if 'one' in request.POST:
        form = FORM_PLACE(request.POST)

        tests = form.save(commit=False)

        pk = tests.unity.id
        return redirect('lekvis', pk)
        # print(test)
        # show = doctor.objects.filter(unit=test)
        # forms = TERM_VISIT()
        # # forms = PERS_VISIT()
        # patient = Personal.objects.all()

        # context = {
        #
        #     'show': show,
        #     # 'forms': forms,
        #     # 'patient': patient,
        #
        # }
        # return render(request, '../templates/Worker/Visit_place.html', context)


    context = {

        'form': form,

    }
    return render(request, '../templates/Worker/Visit_place.html', context)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['personel'])
def lekvis(request, pk):
            show = doctor.objects.filter(unit=pk)
            forms = TERM_VISIT()
            if "two" in request.POST:

                forms = TERM_VISIT(request.POST)
                # if forms.is_valid():
                form=forms.save(commit=False)
                pi = form.name.id
                return redirect('regvis', pk, pi)

            context = {
                'show': show,
                'forms': forms,
            }
            return render(request, '../templates/Worker/Visit_person.html', context)

@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['personel'])
def regvis(request, pk, pi):
            show = Term_day.objects.filter(Q(work_place=pi) and Q(work_person=pi))
            form = REST_VISIT(pk, pi)
            if "two" in request.POST:
                form = REST_VISIT(pk, pi, request.POST)
                if form.is_valid():
                    forms = form.save(commit=False)

                    struct = Unit.objects.get(id=forms.unity.id)
                    user = forms.patient_person
                    print(user.iduser)
                    forms.patient_user = user.iduser
                    forms.struct = struct.organization
                    forms.organization = struct.organization.organization
                    print(forms.struct)
                    print(forms.organization)
                    forms.save()
                    messages.success(request, "Wizyta zarejestrowana")
                    return redirect('visit_per')
                else:
                    messages.error(request, "Wizyta nie zarejestrowana")
            context = {
                'form': form,
                'show': show,

            }
            return render(request, '../templates/Worker/Visit_reg.html', context)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['personel'])
def check_per(request):
    show = Personal.objects.filter(check=False)
    context = {
        "show": show,
    }
    return render(request, '../templates/Worker/check.html', context)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['personel'])
def delete_per(request, pk):
        Per = Personal.objects.get(id=pk)
        txt_user = Per.id
        Per.delete()

        messages.success(request, 'Obiekt został usunięty')
        return redirect('check_per')

@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['personel'])
def check(request, pk):
    show = Personal.objects.get(id=pk)
    show.check = True
    show.save()
    messages.success(request, 'Pacjent' + show.first_name + show.last_name + 'został autoryzowany')
    return redirect('check_per')

@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['lekarz'])

def home_lek(request):
    return render(request, '../templates/LEKARZ/home.html', )
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['lekarz'])

def placeform(request):
    show = doctor.objects.filter(name__iduser=request.user)
    try:
        if request.method == "GET":
            pk = request.GET['place']
            return redirect('showvisit', pk)
    except:
        messages.info(request, "Wybierz placówkę")
    context = {
        'show': show,
    }
    return render(request, '../templates/LEKARZ/placeform.html', context )
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['lekarz'])

def showvisit(request, pk):
    place = Unit.objects.get(id=pk)
    os = Personal_med.objects.get(iduser=request.user)
    show = Visit.objects.filter(Q(term__work_place = place) and Q(term__work_person=os) )
    dat = timezone.now()
    print(dat)
    try:
        test = request.GET['data']
        show = Visit.objects.filter(Q(term__work_place=place) and Q(term__work_person=os) and Q(term__work_date=test))
    except:
        show = Visit.objects.filter(Q(term__work_place=place) and Q(term__work_person=os) and Q(term__work_date=dat))
    context = {
        'place': place,
        'filter': show,
        'dat': dat,
    }
    return render(request, '../templates/LEKARZ/showvisit.html', context)

        # print("zz")
        #
        # context = {
        #     'place': place,
        #     'filter': show,
        # }
        # return render(request, '../templates/LEKARZ/showvisit.html', context)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['personel'])

def editper(request):
    if 'pass' in request.POST:
        formpass = PasswordChangeForm(request.user, request.POST)
        if formpass.is_valid():
            user = formpass.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Twoje hasło zostało zmienione!')

        else:
            messages.error(request, 'Błędne hasło.')
    else:
        formpass = PasswordChangeForm(request.user)
    forms = EditUserForms(instance=request.user)
    show = Personal_med.objects.get(iduser=request.user)
    form = EDITPROFILE(instance=show)
    if 'profile' in request.POST:
        form = EDITPROFILE(request.POST, instance=show)
        forms = EditUserForms(request.POST, instance=request.user)
        if form.is_valid() :
            f1=form.save(commit=False)
            f2=forms.save(commit=False)
            f2.last_name = f1.last_name
            f2.first_name = f1.first_name
            f1.save()
            f2.save()
            messages.success(request, 'Dane zostały zmienione!')
        else:
            messages.error(request, 'Dane nie zostały zmienione!')
    context = {
        'form': form,
        'forms': forms,
        'formpass': formpass,
    }
    return render(request, '../templates/Worker/editform.html', context)

@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['lekarz'])

def editlek(request):
    if 'pass' in request.POST:
        formpass = PasswordChangeForm(request.user, request.POST)
        if formpass.is_valid():
            user = formpass.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Twoje hasło zostało zmienione!')

        else:
            messages.error(request, 'Błędne hasło.')
    else:
        formpass = PasswordChangeForm(request.user)
    forms = EditUserForms(instance=request.user)
    show = Personal_med.objects.get(iduser=request.user)
    form = EDITPROFILE(instance=show)
    if 'profile' in request.POST:
        form = EDITPROFILE(request.POST, instance=show)
        forms = EditUserForms(request.POST, instance=request.user)
        if form.is_valid() :
            f1=form.save(commit=False)
            f2=forms.save(commit=False)
            f2.last_name = f1.last_name
            f2.first_name = f1.first_name
            f1.save()
            f2.save()
            messages.success(request, 'Dane zostały zmienione!')
        else:
            messages.error(request, 'Dane nie zostały zmienione!')
    context = {
        'form': form,
        'forms': forms,
        'formpass': formpass,
    }
    return render(request, '../templates/LEKARZ/editform.html', context)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['lekarz'])

def editvisit(request, pk ):
    show = Visit.objects.get(id=pk)
    STATUSFORM = modelformset_factory(Visit, fields=('status',), extra=0,)
    # DOCFORM = modelformset_factory(Visit, fields=('id10',), extra=0, setattr("class":'form-control'))
    DOCFORM2 = modelformset_factory(Visit, fields=( 'description_person',), extra=0,)
    forms = STATUSFORM(queryset=Visit.objects.filter(id=pk))
    form2 = DOCFORM(instance=show)
    form = DOCFORM2(queryset=Visit.objects.filter(id=pk))
    per = show.patient_person
    doc = show.term.work_person
    showrec = e_system_RECEPTY.objects.filter(idvisit=pk)
    showskier = e_system_SKIEROWANIA.objects.filter(idvisit=pk)
    print(per)
    print(doc)
    formrec = FORMREC()
    formskie = FORMSKIER()
    if "rec" in request.POST:
        formrec = FORMREC(request.POST)
        if formrec.is_valid():
            fors=formrec.save(commit=False)
            fors.idpac = per
            fors.iddoc = doc
            fors.idvisit = show
            print(fors)
            fors.save()
            print('Ok')
            messages.success(request ,"Recepta została dodana")
            redirect('editvisit', pk)
        else:
            messages.error(request, "Recepta nie została dodana")
    if "skie" in request.POST:
        formskie = FORMSKIER(request.POST)
        if formskie.is_valid():
            fors=formskie.save(commit=False)
            fors.idpac = per
            fors.iddoc = doc
            fors.idvisit = show
            fors.save()
            print('Ok')
            messages.success(request ,"Skierowanie zostało dodana")
            redirect('editvisit', pk)
        else:
            messages.error(request, "Skierowanie nie zostało dodana")
    if "typ" in request.POST:
        forms = STATUSFORM(request.POST)
        if forms.is_valid():
                forms.save()
                messages.success(request, "Status zaktualizwany")

    if "roz" in request.POST:
        form2 = DOCFORM(request.POST)
        if form2.is_valid():
            form2.save()
            messages.success(request, "Status zaktualizwany")
    if "opis" in request.POST:
        form = DOCFORM2(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Opis zaktualizwany")
    context = {
        'show': show,
        'form': form,
        'form2': form2,
        'forms': forms,
        'formrec': formrec,
        'formskie': formskie,
        'showrec': showrec,
        'showskier': showskier,
    }
    return render(request, '../templates/LEKARZ/editvisit.html', context)