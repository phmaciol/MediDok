from datetime import datetime
import datetime

from django.db.models import Q

from django.forms import modelformset_factory
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from Pacjent.models import *
from Profile.models import *
from Terminarz.models import *
from Pacjent.forms import *
from Personel.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from Profile.decorators import unauth_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required
from Pacjent.filters import *
from django.http import HttpResponse
# Create your views here.
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@admin_only

def document_upload_adm(request):




    document = Document.objects.all()
    # document = Document.objects.select_related(User, Personal)

    return render(request, 'ADMIN/dok_up.html', { 'document': document})
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@admin_only
def register_visit_adm(request):

    views_visit = Visit.objects.all()

    return render(request, 'admin/visit.html', {'views_visit': views_visit})
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['Custom'])
def document_upload(request):
    val = Personal.objects.get(iduser=request.user)
    if val.check:
        upload_form = DocumentForm()
        user_in = request.user
        profile = Personal.objects.filter(iduser=user_in)

        document = Document.objects.filter(author_user=user_in)
        if request.method == 'POST':

            upload_form = DocumentForm(request.POST, request.FILES)
            if upload_form.is_valid():
                upload_stock = upload_form.save(commit=False)
                upload_stock.author_user = user_in
                # upload_stock.author_person = Personal.objects.get(iduser=user_in)
                upload_stock.save()
                return redirect('upload')
        return render(request, 'Customer/document_page.html',
                      {'upload_form': upload_form, 'document': document, 'profile': profile})
    else:
        return redirect('not_check')


#delete
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['Custom'])
def deleteItem(request, id):
    item = Document.objects.get(id=id)
    item.delete()
    return redirect('upload')
# @admin_only
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['Custom'])
def visitreg(request, unitpk, perspk):

        actualy_date = timezone.now()
        result = Term_day.objects.filter(work_place=unitpk, work_person=perspk)
        # show = Term_day.objects.filter(work_place=unitpk, work_person=perspk)
        vis = Visit.objects.filter(term__work_place=unitpk)
        show = []
        xy = True
        print(actualy_date.date())
        for x in result:
            for y in vis:
                xy = True
                if y.term.id == x.id:
                    print(x.work_date, x.work_time, "Zajęte")
                    xy = False
                    break
            if x.work_date > actualy_date.date() and xy:
                 show.append(x)




        context = {
            'show': show,
            }
        return  render(request, 'Customer/visitreg.html', context)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['Custom'])
def register_visit(request):


    show = Visit.objects.filter(patient_user=request.user)
    return render(request, 'Customer/Visit.html', {'show': show})
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['Custom'])
def ONE_visit(request, pk):
    TERMFORM = modelformset_factory(Visit, fields=('term',), extra=0, )
    show = Visit.objects.get(id=pk)
    unitpk = show.unity_id
    personid = show.term.work_person_id
    idc = show.id10.all()
    edit_one = VisitForm_EDIT_PAC(unitpk, personid)
    print(idc)

    terms = [show.term]
    actualy_date = timezone.now()
    vis = Visit.objects.filter(term__work_place=show.unity_id)
    term = Term_day.objects.filter(Q(work_place=show.organization) and Q(work_person=show.term.work_person))
    formterm = TERMFORM(queryset=Visit.objects.filter(id=pk))
    for x in term:
        for y in vis:
            xy = True
            if y.term.id == x.id:
                print(x.work_date, x.work_time, "Zajęte")
                xy = False
                break
        if x.work_date > actualy_date.date() and xy:
            terms.append(x)

    if "termin" in request.POST:
        formterm = TERMFORM(request.POST)
        if formterm.is_valid():
            formterm.save()
            return redirect('visit_one', pk)
    if request.user.id == show.patient_user.id:
        rec = e_system_RECEPTY.objects.filter(idvisit=pk)
        skie = e_system_SKIEROWANIA.objects.filter(idvisit=pk)
        recCO = e_system_RECEPTY.objects.filter(idvisit=pk).count()
        skieCO = e_system_SKIEROWANIA.objects.filter(idvisit=pk).count()

    else:
        return HttpResponse('Nie masz dostępu do tej strony' )

    context = {
            'show': show,
            'rec': rec,
            'skie': skie,
            'idc': idc,
            'recCO': recCO,
            'skieCO': skieCO,
            'edit': edit_one,
            'terms': terms,
            'formterm': formterm,
        }
    return render(request, 'Customer/Visit_one.html', context)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['Custom'])
def visit_register(request, pk, pi):
    usr = User.objects.get(id = request.user.id)
    pers = Personal.objects.get(iduser = usr.id)
    unt = Unit.objects.get(id = pk)
    term = Term_day.objects.get(id = pi)
    stru = Struct_Organization.objects.get(id= unt.organization.id)
    org = Organization.objects.get(id= stru.organization.id)
    forms = VisitForm_CUST(initial={'patient_user': usr.id,'unity': unt, 'patient_person': pers, 'struct': stru, 'organization': org})


    if request.method == 'POST':

        forms = VisitForm_CUST(request.POST)
        if forms.is_valid():
            forms_stock = forms.save(commit=False)
            forms_stock.term = term
            forms_stock.save()

            return redirect('visit')
        else:
            messages.error(request, 'błąd' )

    context = {
            'forms': forms,
            'term': term,


        }
    return render(request, 'Customer/Visit_register.html',context)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['Custom'])
def organizations(request):
    val = Personal.objects.get(iduser=request.user)
    if val.check:
        show = Organization.objects.all()
        return render(request, 'Customer/Place/organization.html', {'show': show})
    else:
        return redirect('not_check')
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['Custom'])
def organizations_page(request, id):
    show_struct = Struct_Organization.objects.filter(organization=id)
    show = Organization.objects.filter(id=id)
    return render(request, 'Customer/Place/organization_page.html', {'show': show, 'show_struct': show_struct})
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['Custom'])
def organizations_next(request, id):
    show = Struct_Organization.objects.filter(organization=id)
    return render(request, 'Customer/Place/struct_place.html', {'show': show})
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['Custom'])
def not_check(request):
    return render(request, 'Customer/check.html')
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['Custom'])
def e_systemREC(request):
    person = Personal.objects.get(iduser=request.user)
    show = e_system_RECEPTY.objects.filter(idpac = person.id)
    context = {
        'show': show,
    }
    return render(request, 'Customer/systemREC.html', context)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['Custom'])
def e_systemSKIER(request):
    person = Personal.objects.get(iduser=request.user)
    show = e_system_SKIEROWANIA.objects.filter(idpac = person.id)
    context = {
        'show': show,
    }
    return render(request, 'Customer/systemSKIER.html', context)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['Custom'])
def DEKL_ON(request):
    form = DEKLFORM()
    pat = Personal.objects.get(iduser=request.user)
    if request.method == 'POST':
        form = DEKLFORM(request.POST, request.FILES)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.patient_person = pat

            forms.save()
            messages.success(request, 'Deklaracja została dodana')
            return  redirect('clinic')
        else:
            messages.error(request, 'Deklaracja nie została dodana')
            return redirect('clinic')

    context = {
        'form':form,
    }
    return render(request, 'Customer/dekl.html', context)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['Custom'])
def cancel(request, pk):
    show = Visit.objects.get(id=pk)
    show.status = "4"
    show.save()
    messages.success(request, 'Wizyta został odwołana')
    return redirect('visit_one', pk)