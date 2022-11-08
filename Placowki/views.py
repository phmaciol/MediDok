from django.db.models import Q
from django.shortcuts import render, redirect
from Pacjent.forms import *
from Placowki.forms.Organization.forms import *
from Placowki.forms.Struct.forms import *
from Placowki.forms.Unit.forms import *
from Terminarz.models import *
from django.contrib import messages
from Profile.decorators import allowed_users, admin_only
from django.contrib.auth.decorators import login_required
# from django.contrib.messages.views import SuccessMessageMixin
# from django.urls import reverse_lazy
# from django.views import generic
# from bootstrap_modal_forms.mixins import PassRequestMixin

# Create your views here.
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@admin_only
# Rejestr placówek
def orga_admin(request):
    show = Organization.objects.all().count()
    show_one = Struct_Organization.objects.all().count()
    show_two = Unit.objects.all().count()

    context = {
        'show': show,
        'show_one': show_one,
        'show_two': show_two,

    }
    return render(request, '../templates/ADMIN/PLACE/organization_admin.html', context)

@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@admin_only
# Rejestr podmiotów
def orga_admin_tabs(request):
    show = Organization.objects.all()
    form = PodmiotForms()

    forms = []
    instance = []
    for x in show:
        instance = Organization.objects.get(id=x.id)

        forms.append(PodmiotEditForms(instance=instance))



    if request.method == "POST":
        form = PodmiotForms(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Podmiot leczniczy został dodany")
            return redirect('orga_admin_tabs')

        elif form.is_valid() != False:
            messages.error(request, 'Błąd')
            return redirect('orga_admin_tabs')

        forms = PodmiotEditForms(request.POST or None, request.FILES or None, instance=instance)

        if forms.is_valid():

            forms.save()
            messages.error(request, 'Zapisano zmiany')
            return redirect('orga_admin_tabs')

        elif  forms.is_valid() != False:
                messages.error(request, 'Błąddd')
                return redirect('orga_admin_tabs')
        # messages.error(request, 'Błąd aktualizacji')

    context = {
        'show': show,
        'form': form,
        'forms': forms,

    }
    return render(request, '../templates/ADMIN/PLACE/organization_tabels.html', context)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@admin_only
# Zakłady lecznicze placówkach
def orga_admin_tabs_one(request, pk):

    ZakladFormPodmiotALL = modelformset_factory(Struct_Organization, fields='__all__',  extra=0)
    show_one = Organization.objects.filter(id=pk)
    instance = Organization.objects.get(id=pk)
    show = Struct_Organization.objects.filter(organization = pk)
    form = PodmiotEditForms(instance=instance)
    forms = ZakladFormPodmiot(pk)

    formset = ZakladFormPodmiotALL(queryset=Struct_Organization.objects.filter(organization=pk))
    if request.method == "POST":
        form = PodmiotEditForms(request.POST, request.FILES, instance=instance)
    # for form in formset:
    #         form.fields['category'].queryset = Category.objects.filter(user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Zmiany zostały zapisane!")
            return redirect('orga_admin_tabs_one', pk)
        elif form.is_valid() != False:
            messages.error(request, "Zmiany nie zostały zapisane!")
            return redirect('orga_admin_tabs_one', pk)
        forms = ZakladFormPodmiot(pk, request.POST, request.FILES)


        if forms.is_valid():

            forms.save()
            messages.success(request, "Zakład został zarejestrowany!")
            return redirect('orga_admin_tabs_one', pk)
        elif forms.is_valid() != False:
            messages.error(request, "Zakład nie został zarejestrowany!")
            return redirect('orga_admin_tabs_one', pk)

        formset = ZakladFormPodmiotALL(request.POST, request.FILES)
        test = formset.save()
        messages.success(request, "Zmiany zapisane!")
        return redirect('orga_admin_tabs_one', pk)
        # test = formset.save(commit=False)
        # for xy in test:
        #     if xy.is_valid():
        #         xy.save()
        #
        #
        #     else:
        #         messages.error(request, "Zmiany nie zostały zapisane ")
        #         print(formset.errors)
        #         return redirect('orga_admin_tabs_one', pk)



    context = {
        'show': show,
        'show_one': show_one,
        'form': form,
        'forms': forms,
        'pk': pk,
        'formset': formset,

    }
    return render(request, '../templates/ADMIN/PLACE/organization_one.html', context)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@admin_only
# Zakłady lecznicze placówkach
def struct_admin(request):
    ZakladFormPodmiotALL = modelformset_factory(Struct_Organization, fields='__all__',  extra=0)
    formset = ZakladFormPodmiotALL(queryset=Struct_Organization.objects.all())
    show = Struct_Organization.objects.all()
    forms = ZakladFormALL()
    if 'two' in request.POST:
        forms = ZakladFormALL( request.POST, request.FILES,)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Zakład został zarejestrowany!")
            return redirect('struct')
        elif forms.is_valid() != False:
            messages.error(request, "Zakład nie został zarejestrowany!")
            return redirect('struct')
    if 'one' in request.POST:
        formset = ZakladFormPodmiotALL(request.POST, request.FILES)
        test=formset.save()
        if test:
            messages.success(request, "Zmiany zapisane!")
        else:
            messages.error(request, "Zmiany nie  zapisane!")
        return redirect('struct')
    context = {
        'show': show,
        'forms': forms,
        'formset': formset,

    }
    return render(request, '../templates/ADMIN/PLACE/struct_all.html', context)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@admin_only
# Zakłady lecznicze placówkach
def unit_admin(request):
    UnitFormPodmiotALL = modelformset_factory(Unit, fields='__all__', extra=0)
    formset = UnitFormPodmiotALL(queryset=Unit.objects.all())

    show = Unit.objects.all()
    forms = UnitALLforms()

    if 'two' in request.POST:
        forms = UnitALLforms( request.POST, request.FILES,)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Jednostka został zarejestrowany!")
            return redirect('struct')
        elif forms.is_valid() != False:
            messages.error(request, "Zakład nie został zarejestrowany!")
            return redirect('unit')
    if 'one' in request.POST:
        formset = UnitFormPodmiotALL(request.POST, request.FILES)
        test=formset.save()
        if test:
            messages.success(request, "Zmiany zapisane!")
        else:
            messages.error(request, "Zmiany nie  zapisane!")
        return redirect('unit')
    context = {
        'show': show,
        'forms': forms,
        'formset': formset,

    }
    return render(request, '../templates/ADMIN/PLACE/unit_all.html', context)
@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@admin_only
def orga_admin_one_unit(request, pk):

    UnitFormPodmiotALL = modelformset_factory(Unit, fields='__all__',  extra=0)
    show_one = Struct_Organization.objects.filter(id=pk)
    instance = Struct_Organization.objects.get(id=pk)
    show = Unit.objects.filter(organization = pk)

    form = ZakladFormEditPodmiot(instance=instance)
    forms = UnitFormPodmiot(pk)

    formset = UnitFormPodmiotALL(queryset=Unit.objects.filter(organization=pk))
    if request.method == "POST":
        form = ZakladFormEditPodmiot(request.POST, request.FILES, instance=instance)
    # for form in formset:
    #         form.fields['category'].queryset = Category.objects.filter(user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Zmiany zostały zapisane!")
            return redirect('orga_admin_one_unit', pk)
        elif form.is_valid() != False:
            messages.error(request, "Zmiany nie zostały zapisane!")
            return redirect('orga_admin_one_unit', pk)
        forms = UnitFormPodmiot(pk, request.POST, request.FILES)


        if forms.is_valid():

            forms.save()
            messages.success(request, "Zakład został zarejestrowany!")
            return redirect('orga_admin_one_unit', pk)
        elif forms.is_valid() != False:
            messages.error(request, "Zakład nie został zarejestrowany!")
            return redirect('orga_admin_one_unit', pk)

        formset = UnitFormPodmiotALL(request.POST, request.FILES)
        test = formset.save()
        messages.success(request, "Zmiany zapisane!")
        return redirect('orga_admin_one_unit', pk)
        # test = formset.save(commit=False)
        # for xy in test:
        #     if xy.is_valid():
        #         xy.save()
        #
        #
        #     else:
        #         messages.error(request, "Zmiany nie zostały zapisane ")
        #         print(formset.errors)
        #         return redirect('orga_admin_tabs_one', pk)



    context = {
        'show': show,
        'show_one': show_one,
        'form': form,
        'forms': forms,
        'pk': pk,
        'formset': formset,

    }
    return render(request, '../templates/ADMIN/PLACE/organization_one_unit.html', context)

def admin_one_unit(request, pk):
    show_one = Unit.objects.filter(id=pk)
    instance = Unit.objects.get(id=pk)

    show = doctor.objects.filter(unit = pk)
    form = UnitEditForms(instance=instance)
    forms = DoctorFormADD(pk)


    if request.method == "POST":
        form = UnitEditForms(request.POST, request.FILES, instance=instance)
        forms = DoctorFormADD(pk, request.POST)




        if forms.is_valid():
            forms.save()
            messages.success(request, "Lekarz został przypisany do jednostki!")
            return redirect('admin_one_unit', pk)
        elif forms.is_valid() != False:
            messages.error(request, "Lekarz nie został przypisany do jednostki!")
            return redirect('admin_one_unit', pk)
        if form.is_valid():
            form.save()
            messages.success(request, "Zmiany zostały zapisane!")
            return redirect('admin_one_unit', pk)
        elif form.is_valid() != False:
            messages.error(request, "Zmiany nie zostały zapisane!")
            return redirect('admin_one_unit', pk)


    context = {
        'show': show,
        'show_one': show_one,
        'form': form,
        'forms': forms,
        'pk': pk,


    }
    return render(request, '../templates/ADMIN/unit.html', context)










@login_required(login_url='loginPage')  # blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@admin_only
def delete_organization(request, pk):
        orga = Organization.objects.get(id=pk)
        txt_user = orga.name
        orga.delete()
        messages.success(request, 'Podmiot leczniczy' + txt_user +  'został usunięty' )

        return redirect('orga_admin_tabs')
@login_required(login_url='loginPage')  # blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@admin_only
def delete_struct(request, dd, pi):
        struct = Struct_Organization.objects.get(id=dd)
        txt_user = struct.name
        struct.delete()
        messages.success(request, 'Zakład leczniczy ' + txt_user+  ' został usunięty' )
        return redirect('orga_admin_tabs_one', pi)
@login_required(login_url='loginPage')  # blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@admin_only
def delete_unit(request, dd, pi):
        unit = Unit.objects.get(id=dd)
        txt_user = unit.name
        unit.delete()
        messages.success(request, 'Jednostka ' + txt_user+  ' został usunięty' )
        return redirect('orga_admin_one_unit', pi)
































@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@allowed_users(allowed_roles=['Custom'])


def spec(request):

    val = Personal.objects.get(iduser=request.user)
    if val.check:
        show = Struct_Organization.objects.filter(type_place=1)
        unit_show = Unit.objects.all()

        show_per = doctor.objects.all()
        return render(request, 'Customer/Place/spec_clinic.html',
                      {'show': show, 'show_per': show_per, 'unit_show': unit_show})
    else:
        return redirect('not_check')


def hospital(request):
    show = Struct_Organization.objects.filter(type_place=2)
    unit_show = Unit.objects.all()

    show_per = doctor.objects.all()

    return render(request, 'Customer/Place/hospital.html',
                  {'show': show, 'show_per': show_per, 'unit_show': unit_show})
def clinic(request):

    per = Personal.objects.get(iduser=request.user)
    dekltest = dekl.objects.filter(idpac = per.id).count()
    if dekltest == 0:
        doc_count = Form_user.objects.filter(patient_person=per.id).count()
        context = {
            'doc_count': doc_count,

        }
        if doc_count == 1:
            doc_dekl = Form_user.objects.get(patient_person=per.id, type_forms='0')
            context = {
                'doc_count': doc_count,
                'doc_dekl': doc_dekl,
            }

        return render(request, 'Customer/Place/clinic_none.html', context )
    elif dekltest == 1:

        dekll = dekl.objects.get(idpac__iduser=request.user)
        pk = dekll.idunit.organization.id
        show = Struct_Organization.objects.filter(Q(type_place=0) and Q(id=pk))
        unit_show = Unit.objects.all()

        show_per = doctor.objects.all()
        context = {
            'show': show,
            'unit_show': unit_show,
            'show_per': show_per,

        }
        return render(request, 'Customer/Place/clinic.html', context)


def organizations_page(request, id):
    show_struct = Struct_Organization.objects.filter(organization=id)
    show = Organization.objects.filter(id=id)
    return render(request, 'Customer/Place/organization_page.html', {'show': show, 'show_struct': show_struct})
def organizations_next(request, id):
    show = Struct_Organization.objects.filter(organization=id)
    return render(request, 'Customer/Place/struct_place.html', {'show': show})
