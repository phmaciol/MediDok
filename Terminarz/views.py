from datetime import datetime
import datetime
from datetime import timedelta
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from Profile.models import *
from Regiony.models import *
from Terminarz.models import *
from Terminarz.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from Profile.decorators import unauth_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import UpdateView
from django.utils import timezone, dateformat
# Create your views here.

@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@admin_only
def term_gen(request):
    forms = GenericTERM()


    if request.method == 'POST':

        forms = GenericTERM(request.POST)
        if forms.is_valid():
            stock = forms.save(commit=False)

            days = stock.work_start_date
            a = 0
            hours = stock.work_start
            hours_stop = stock.work_stop
            hours_addd = stock.work_start
            hours_addd = datetime.time(hour=hours.hour, minute=hours.minute)
            print(hours_addd)
            x = 60/stock.work_time
            x -= 1
            b = 0

            if days >= stock.work_date:
                if days < stock.work_stop_date:
                    if stock.work_start < stock.work_stop:
                        while days < stock.work_stop_date:
                            if days.weekday() == stock.work_day:

                                while hours_stop >= hours_addd:
                                    queryADD = Term_day.objects.create(work_place=stock.work_place,
                                                                       work_person=stock.work_person,
                                                                       work_date=days, work_time=hours_addd,
                                                                       work_day=stock.work_day,
                                                                       work_type=stock.work_type)
                                    queryADD.save()
                                    while b < x:
                                        hours_addd = datetime.time(hour=hours_addd.hour, minute=hours_addd.minute + stock.work_time)
                                        queryADD = Term_day.objects.create(work_place=stock.work_place,
                                                                           work_person=stock.work_person,
                                                                           work_date=days,
                                                                           work_time=hours_addd,
                                                                           work_day=stock.work_day,
                                                                           work_type=stock.work_type)
                                        queryADD.save()

                                        b += 1
                                        print(hours_addd)
                                    b = 0
                                    hours_addd = datetime.time(hour=hours_addd.hour + 1, minute=b)
                                    print(hours_addd)
                                print(days)
                            hours_addd = datetime.time(hour=hours.hour, minute=hours.minute)
                            days = days + datetime.timedelta(days=1)
                        messages.error(request, "Terminarz został wygenrowany")
                    else:
                        messages.error(request, "Godzina rozpoczecia musi być mniejsza od godziny zakończenia")
                else:
                    messages.error(request, "Data rozpoczecia musi być mniejsza od daty zakończenia")
            else:
                messages.error(request, "Data rozpoczecia musi być datą dzisiejszą lub z przyszłości")





            return redirect('term_gen')
    return render(request, '../templates/ADMIN/term.html', {'forms': forms, })

@login_required(login_url='loginPage') #blokowanie niezalogowanym uzytkownikom dawac przed kazdym widokiem
@admin_only
def term_gen_only(request, pk, pi):
    forms = GenericTERM()


    if request.method == 'POST':

        forms = GenericTERM(request.POST)
        if forms.is_valid():
            stock = forms.save(commit=False)
            # days = stock.work_stop_date.weekday()
            # days = stock.work_stop_date - stock.work_start_date
            # days = stock.work_start_date + datetime.timedelta(days=1)
            days = stock.work_start_date
            a = 0
            hours = stock.work_start
            hours_stop = stock.work_stop
            hours_addd = stock.work_start
            hours_addd = datetime.time(hour=hours.hour, minute=hours.minute)
            print(hours_addd)
            x = 60/stock.work_time
            x -= 1
            b = 0

            if days >= stock.work_date:
                if days < stock.work_stop_date:
                    if stock.work_start < stock.work_stop:
                        while days < stock.work_stop_date:
                            if days.weekday() == stock.work_day:

                                while hours_stop >= hours_addd:
                                    queryADD = Term_day.objects.create(work_place=stock.work_place,
                                                                       work_person=stock.work_person,
                                                                       work_date=days, work_time=hours_addd,
                                                                       work_day=stock.work_day,
                                                                       work_type=stock.work_type)
                                    queryADD.save()
                                    while b < x:
                                        hours_addd = datetime.time(hour=hours_addd.hour, minute=hours_addd.minute + stock.work_time)
                                        queryADD = Term_day.objects.create(work_place=stock.work_place,
                                                                           work_person=stock.work_person,
                                                                           work_date=days,
                                                                           work_time=hours_addd,
                                                                           work_day=stock.work_day,
                                                                           work_type=stock.work_type)
                                        queryADD.save()

                                        b += 1
                                        print(hours_addd)
                                    b = 0
                                    hours_addd = datetime.time(hour=hours_addd.hour + 1, minute=b)
                                    print(hours_addd)
                                print(days)
                            hours_addd = datetime.time(hour=hours.hour, minute=hours.minute)
                            days = days + datetime.timedelta(days=1)
                        messages.error(request, "Terminarz został wygenrowany")
                    else:
                        messages.error(request, "Godzina rozpoczecia musi być mniejsza od godziny zakończenia")
                else:
                    messages.error(request, "Data rozpoczecia musi być mniejsza od daty zakończenia")
            else:
                messages.error(request, "Data rozpoczecia musi być datą dzisiejszą lub z przyszłości")





            return redirect('term_gen')
    return render(request, 'Worker/../templates/ADMIN/term.html', {'forms': forms, })