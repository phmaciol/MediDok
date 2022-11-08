from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import Group
from Profile.models import *
from Regiony.models import *
from Pacjent.models import *
from Profile.forms import *
from .filters import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .decorators import unauth_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm, AdminPasswordChangeForm, SetPasswordForm
from django.views.generic import UpdateView
from django.core.paginator import Paginator
# Create your views here.

@unauth_user
def registration(request):


        form = CreateUserForms()
        if request.method == 'POST':

            form = CreateUserForms(request.POST)
            a_valid = form.is_valid()

            if a_valid:
                user = form.save()

                username = form.cleaned_data.get('username')
                group =Group.objects.get(name = "custom")
                user.groups.add(group)

                messages.success(request, 'Konto użytkownika ' + username + ' zostało stworzone')
                return redirect('loginPage')


        return render(request, '../templates/Acount/registration.html', { 'form':form})
@unauth_user
def loginPage(request):

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user,)
                return redirect('home')
            else:
                messages.info(request, 'Nazwa użytkownika lub hasło nie poprawne!')
        context = {}
        return render (request, '../templates/Acount/login_page.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, 'Zostałeś bezpiecznie wylogowany')
    return redirect('loginPage')

@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@admin_only
def home(request):
    show = User.objects.filter(groups=2).count()
    user_one = User.objects.filter(groups=3).count()
    user_two = User.objects.filter(groups=4).count()
    show_user = user_two + user_one
    show_groups = User.objects.all().count()
    print(show)
    print(show_user)
    show_one = Personal.objects.filter(check=0).count()
    show_two = Personal.objects.filter(check=1).count()
    context = {
        'show': show,
        'show_user': show_user,
        'show_groups': show_groups,
        'show_one': show_one,
        'show_two': show_two,
    }
    return render(request, '../templates/ADMIN/home_admin.html', context)
def user_person(request, pk):
    if pk == 0:
        show = User.objects.filter(groups=2)
        context ={
            'show': show,
            'pki': pk,
        }
        return render(request, '../templates/ADMIN/USERS/pac_user.html', context)
    elif pk == 1:
        show= User.objects.filter(Q(groups=3) | Q(groups=4))

        context = {
            'show': show,
            'pki': pk,
        }
        return render(request, '../templates/ADMIN/USERS/per_user.html', context)
    elif pk == 2:
        show= User.objects.all

        context = {
            'show': show,
            'pki': pk,
        }
        return render(request, '../templates/ADMIN/USERS/users_all.html', context)
    else: redirect('home')


def deleteusers(request, pk, pi):

    user = User.objects.get(id=pk)
    test = Personal_med.objects.filter(id=pk).count()
    test2 = Personal.objects.filter(id=pk).count()
    txt_user = user.username
    print
    if test == '0' and test2 == '0':
        user.delete()
        messages.success(request, 'Konto użytkownika' + txt_user + ' zostało usunięte')
        return redirect('user_person', pi)
    else:
        messages.error(request, 'Konto użytkownika' + txt_user + ' nie zostało usunięte należy najpierw usunąć wpis do rejestru')
        return redirect('user_person', pi)
def infouser(request, pk):
    test = Personal.objects.filter(iduser=pk).count()
    test2 = Personal_med.objects.filter(iduser=pk).count()
    if test == 1:
        instance = Personal.objects.get(iduser=pk)
        instance_one = User.objects.get(id=pk)
        forms = EditUserFormsADMIN(instance=instance_one)
        form = EditPersonalFormsDATA(instance=instance)
        form_one = EditPersonalFormsADRES(instance=instance)
        form_con = EditPersonalFormsCON(instance=instance)
        form_con2 = EditEmail(instance=instance_one)
        formpass = AdminPasswordChangeForm(user=instance_one)

        if 'one' in request.POST:
            forms = EditUserFormsADMIN(request.POST, instance=instance_one)
            form = EditPersonalFormsDATA(request.POST, instance=instance)
            forms.save()
            form.save()
            messages.success(request, 'Zamiany w "Dane Osobowe" zostały zmienione')
        elif 'two' in request.POST:
            form_one = EditPersonalFormsADRES(request.POST, instance=instance)
            if form_one.is_valid():
                form_one.save()
                messages.success(request, 'Zamiany w "Dane Adresowe" zostały zmienione')

        elif 'three' in request.POST:
            form_con = EditPersonalFormsCON(request.POST, instance=instance)
            form_con2 = EditEmail(request.POST, instance=instance_one)
            form_con.save()
            form_con2.save()
            messages.success(request, 'Zamiany w "Dane Kontaktowe" zostały zmienione')
        elif 'four' in request.POST:
            formpass = AdminPasswordChangeForm(instance_one,request.POST)
            if formpass.is_valid():
                formpass.save()
                messages.success(request, 'Hasło zostało zmienione ')
            else:
                messages.error(request, 'Hasło nie zostało zmienione ')




        context = {
            'form': form,
            'form_one': form_one,
            'forms': forms,
            'form_con': form_con,
            'form_con2': form_con2,
            'formpass': formpass,
        }
        return render(request, '../templates/ADMIN/USERS/edit_pac.html', context)
    elif test2 == 1:
        instance = Personal_med.objects.get(iduser=pk)
        instance_one = User.objects.get(id=pk)
        forms = EditUserFormsADMIN(instance=instance_one)
        form = EditPERSONELFormsDATA(instance=instance)
        form_one = EditPERSONELFormsADRES(instance=instance)
        form_con = EditPersonalFormsCON(instance=instance)
        form_con2 = EditEmail(instance=instance_one)
        formpass = AdminPasswordChangeForm(user=instance_one)

        if 'one' in request.POST:
            forms = EditUserFormsADMIN(request.POST, instance=instance_one)
            form = EditPERSONELFormsDATA(request.POST, instance=instance)
            forms.save()
            form.save()
            messages.success(request, 'Zamiany w "Dane Osobowe" zostały zmienione')
        elif 'two' in request.POST:
            form_one = EditPERSONELFormsADRES(request.POST, instance=instance)
            if form_one.is_valid():
                form_one.save()
                messages.success(request, 'Zamiany w "Dane Adresowe" zostały zmienione')

        elif 'three' in request.POST:
            form_con = EditPERSONELFormsCON(request.POST, instance=instance)
            form_con2 = EditEmail(request.POST, instance=instance_one)
            form_con.save()
            form_con2.save()
            messages.success(request, 'Zamiany w "Dane Kontaktowe" zostały zmienione')
        elif 'four' in request.POST:
            formpass = AdminPasswordChangeForm(instance_one, request.POST)
            if formpass.is_valid():
                formpass.save()
                messages.success(request, 'Hasło zostało zmienione ')
            else:
                messages.error(request, 'Hasło nie zostało zmienione ')
        context = {
            'form': form,
            'form_one': form_one,
            'forms': forms,
            'form_con': form_con,
            'form_con2': form_con2,
            'formpass': formpass,
        }
        return render(request, '../templates/ADMIN/USERS/edit_per.html', context)
    else:
        instance_one = User.objects.get(id=pk)
        forms = EditUserFormsADMIN(instance=instance_one)
        form_con2 = EditEmail(instance=instance_one)
        formpass = AdminPasswordChangeForm(user=instance_one)

        if 'one' in request.POST:
            forms = EditUserFormsADMIN(request.POST, instance=instance_one)
            forms.save()
            messages.success(request, 'Zamiany w "Dane Osobowe" zostały zmienione')
        elif 'three' in request.POST:
            form_con = EditPERSONELFormsCON(request.POST, instance=instance)
            form_con2 = EditEmail(request.POST, instance=instance_one)
            form_con.save()
            form_con2.save()
            messages.success(request, 'Zamiany w "Dane Kontaktowe" zostały zmienione')
        elif 'four' in request.POST:
            formpass = AdminPasswordChangeForm(instance_one, request.POST)
            if formpass.is_valid():
                formpass.save()
                messages.success(request, 'Hasło zostało zmienione ')
            else:
                messages.error(request, 'Hasło nie zostało zmienione ')
        context = {


            'forms': forms,

            'form_con2': form_con2,
            'formpass': formpass,
        }
        return render(request, '../templates/ADMIN/USERS/users.none.html', context)


def user_web(request):
    show = User.objects.all()
    show_one = Personal_med.objects.all()

    filters = Personal_filters(request.GET, queryset=show_one)
    p = Paginator(filters.qs, 10)

    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)



    context = {
        'page': page,
        'filters': filters,
    }
    return render(request, '../templates/ADMIN/personel.html', context)
def users_web(request):
    show_one = User.objects.all()


    filters = User_filters(request.GET, queryset=show_one)
    p = Paginator(filters.qs, 10)

    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    context = {
        'page': page,
        'filters': filters,
    }
    return render(request, '../templates/ADMIN/users.html', context)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@admin_only
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@admin_only
def deleteuser(request, pk):
    user = User.objects.get(id=pk)
    test = Personal_med.objects.filter(id=pk).count()
    test2 = Personal.objects.filter(id=pk).count()
    txt_user = user.username
    print
    if test == '0' and test2 == '0':
        user.delete()
        messages.success(request, 'Konto użytkownika' + txt_user + ' zostało usunięte')
        return redirect('user_person', pi)
    else:
        messages.error(request,
                       'Konto użytkownika' + txt_user + ' nie zostało usunięte należy najpierw usunąć wpis do rejestru')
        return redirect('user_person', pi)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@admin_only
def adduser(request):
    adduser = AddNewUser()

    if request.method == "POST":
        adduser = AddNewUser(request.POST)

        if adduser.is_valid:


            users = adduser.save()
            pk = users.id
            print(pk)
            messages.success(request, 'Konto użytkownika ' + users.username + ' zostało stworzone')
            return redirect('adduserPER', pk)






    context = {
            'form1': adduser,


        }
    return render(request, '../templates/ADMIN/adduser.html' ,context)
def adduserPerson(request,pk):
    test = User.objects.get(id=pk)
    print(test.groups)
    if test.groups == 2:
        form1 = PersonForms(pk)
        context = {
            'form1': adduser,

        }
        return render(request, '../templates/ADMIN/adduserPERSON.html', context)
    else:
        return render(request, '../templates/ADMIN/adduserPERSON.html')










@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['Custom'])
def home_user(request):
    user_in = request.user

    result_one = Personal.objects.filter(iduser=user_in)
    if result_one:
       return render(request, '../templates/Customer/home.html', {})

    else:
        form = CreatePersonalForms()

        if request.method == 'POST':

            form = CreatePersonalForms(request.POST, request.FILES)
            person_valid = form.is_valid()



            if person_valid :
                personal = form.save(commit=False)

                personal.iduser = request.user
                personal.last_name = request.user.last_name
                personal.first_name = request.user.first_name

                personal.save()

                messages.success(request, 'Dane zostały zaktualizowane')
                return redirect('home_user')
            else:
                messages.error(request, 'Nim zaczniesz uzupełni swoje dane')

        context = {
            'form': form,



            }
        return render(request, '../templates/Acount/home.html', context)



@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['Custom'])
def Edit_form(request):
    result_one = Personal.objects.get(iduser=request.user)
    formpass = PasswordChangeForm(request.user)
    if result_one.check == False:
        messages.error(request, 'Konto nie zostało potwierdzone')
    if 'pass' in request.POST:
        formpass = PasswordChangeForm(request.user, request.POST)
        if formpass.is_valid():
            user = formpass.save()
            messages.success(request, 'Twoje hasło zostało zmienione!')
            update_session_auth_hash(request, user)  # Important!


        else:
            messages.error(request, 'Błędne hasło.')
    else:
        formpass = PasswordChangeForm(request.user)

    update = Personal.objects.get(iduser=request.user)
    form2 = EditPersonalForms(instance=update)
    form = EditUserForms(instance=request.user)
    if request.method == 'POST':

        form = EditUserForms(request.POST, instance=request.user)
        form2 = EditPersonalForms(request.POST, instance=update)
        a_valid = form.is_valid()
        b_valid = form2.is_valid()

        if a_valid and b_valid:
            user = form.save()
            profile = form2.save()
            username = form.cleaned_data.get('username')
            return redirect('home')
        else:
            return redirect('editprofile')
            # messages.success(request, 'Konto użytkownika ' + username + ' zostało stworzone')


    return render(request, '../templates/Acount/EditForm.html', {'form': form,'form2': form2, 'formpass': formpass})