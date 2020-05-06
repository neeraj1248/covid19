
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.state_input,name="state_input"),
    # path('state_district_wise_report',views.state_district_wise_report,name='state_district_wise_report')
]
