from django.urls import path
from django.conf.urls.static import static
from staff import views as user_views 
from django.contrib.auth import views as auth_views

app_name = 'staff'

urlpatterns = [
    path('staff-page/', user_views.staffupdateprofile, name="staff_profile"),
    # path('staff-academic/', user_views.staffacademic, name="staff-academic"),
    path('staff-list/', user_views.stafflist, name="staff_list"),
    path('staff-pdf', user_views.staff_pdf, name="staff-pdf"),
    path('staff-csv', user_views.staff_csv, name="staff-csv"),

]