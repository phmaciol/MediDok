"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from Placowki import views
from Profile.views import *
from Personel.views import *
from Pacjent.views import *
from Placowki.views import *
from Terminarz.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Logowanie i Rejestracja APK Profile
    path('registration', registration, name='registration'),
    path('', loginPage, name='loginPage'),
    path('logout/', logoutUser, name='logout'),

    #Panel Admina django
    path('admin/', admin.site.urls, name='admin'),
        # Admin panel
    path('home/', home,name='home' ),
    path('home/users/<int:pk>', user_person,name='user_person' ),
    path('home/register', orga_admin ,name='orga_admin' ),
    path('home/register/orga_tabs', orga_admin_tabs ,name='orga_admin_tabs' ),
    path('home/register/struct', struct_admin ,name='struct' ),
    path('home/register/unit', unit_admin ,name='unit' ),
    path('home/register/orga_tabs/one/<int:pk>', orga_admin_tabs_one ,name='orga_admin_tabs_one' ),
    path('home/register/orga_tabs/unit/<int:pk>', orga_admin_one_unit ,name='orga_admin_one_unit' ),
    path('home/register/unit/<int:pk>', admin_one_unit  ,name='admin_one_unit' ),
    path('home/register/orga_tabs/delete/<int:pk>', delete_organization ,name='delete_organization' ),
    path('home/register/orga_tabs/one/delete/<int:dd>/<int:pi>', delete_struct ,name='delete_struct' ),
    path('home/register/orga_tabs/one/unit/delete/<int:dd>/<int:pi>', delete_unit ,name='delete_unit' ),
    # path('home/register/orga_tabs/<int:pk>', orga_admin_tabs ,name='orga_admin_tabs_edit' ),
    path('person/', user_web,name='user_web' ),#Rejestr personelu
    path('users/', users_web,name='users_web' ),
    path('users/adduser', adduser ,name='adduser' ),
    path('users/adduser/person/<int:pk>', adduserPerson ,name='adduserPER' ),
    path('deleteper/<int:pk>', delete_per ,name='delete_per' ),
    path('deleteusers/<int:pk>/<int:pi>/', deleteusers ,name='deleteusers' ),
    path('edituser/<int:pk>/', infouser ,name='infouser' ),
    path('document_page_adm/', document_upload_adm, name="upload_adm"),
    path('termgeneric/', term_gen, name='term_gen' ),
    # path('visit_adm/', register_visit_adm, name='visit_adm'),



    # Personel panel
    path('home2/', home_per,name='home_per' ),
    path('home2/dekl', deklPERS ,name='deklPERS' ),
    path('home2/deklaracje', showdekl ,name='showdekl' ),
    path('home2/dekl/<int:pk>', deklPERSone ,name='deklPERSone' ),
    path('home2/form/<int:pk>', formsPERS ,name='formsPERS' ),
    path('home2/doc/<int:pk>', docPERS ,name='docPERS' ),
    path('home2/dekl/<int:pk>/<int:pi>', deklREJ ,name='deklREJ' ),
    path('home2/deklone/<int:pk>/', deklREJlek ,name='deklREJlek' ),
    path('home/form_all/', add_form ,name='add_form' ),
    path('home/doc_all/', doc_show ,name='doc_show' ),
    path('check/', check_per ,name='check_per' ),
    path('editper/', editper ,name='editper' ),
    path('check/<int:pk>', check ,name='check' ),
    path('delete_user/<int:pk>', deleteuser, name="deleteuser"),
    path('visit_check/', visit_per, name='visit_per'),
    path('visit_check/one/<int:pk>', visit_one, name='visit_one_PERS'),
    path('visit_check/place', place, name='place'),
    path('visit_check/place/<int:pk>', lekvis, name='lekvis'),
    path('visit_check/place/<int:pk>/<int:pi>', regvis, name='regvis'),

    #Panel lekarza
    path('homelek/', home_lek, name='home_lek'),
    path('homelek/place/', placeform, name='placeform'),
    path('homelek/place/<int:pk>', showvisit, name='showvisit'),
    path('homelek/place/visit/<int:pk>', editvisit, name='editvisit'),
    path('homelek/profile', editlek, name='editlek'),

    # PACJENT PANEL
    path('home1/', home_user,name='home_user' ),
    path('notcheck/', not_check,name='not_check' ),
    path('document_page/', document_upload, name="upload"),
    path('delete_doc/<int:id>', deleteItem, name="deleteItem"),
    path('editprofile/', Edit_form, name='editprofile'),
    path('visit/', register_visit, name='visit'),
    path('visitone/<int:pk>', ONE_visit, name='visit_one'),
    path('cancel/<int:pk>', cancel, name='cancel'),
    path('visitregi/<int:pk>/<int:pi>', visit_register, name='visit_register'),
    path('systemrec/', e_systemREC, name='e_systemREC'),
    path('systemskier/', e_systemSKIER, name='e_systemSKIER'),
    path('organization/', organizations, name='organization'),
    path('organization/spec', spec , name='spec'),
    path('organization/hospital', hospital , name='hospital'),
    path('organization/clinic', clinic , name='clinic'),
    path('organization/page/<int:id>', organizations_page, name='organization_page'),
    path('organization/<int:id>', organizations_next, name='organization_next'),
    # path('registervisit/', register_visit, name='register_visit'),
    path('visitreg/<int:unitpk>/<int:perspk>', visitreg, name='visitreg'),
    path('dekl', DEKL_ON, name='dekl'),


    path('api-auth/', include('rest_framework.urls')),


    # url(r'^test/$', views.test.as_view(), name='test-list'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
