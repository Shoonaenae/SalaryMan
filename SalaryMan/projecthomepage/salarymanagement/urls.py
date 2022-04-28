from django.urls import path
from . import views

#paths arranged alphabetically by name
app_name = 'salarymanagement'

urlpatterns = [ 
    #URLs for student app
    path('aboutus', views.AboutUsView.as_view(), name="about_us_view"),
    path('addemployee', views.AddEmployeeView.as_view(), name="add_employee_view"),
    path('addemployer', views.AddEmployerView.as_view(), name="add_employer_view"),
    path('addsalary', views.AddSalaryView.as_view(), name="add_salary_view"),
    path('contactus', views.ContactUsView.as_view(), name="contact_us_view"),
    path('dashboard', views.DashboardView.as_view(), name="dashboard_view"),
    path('feature', views.FeatureView.as_view(), name="feature_view"),
    path('home', views.HomeView.as_view(), name="home_view"),
    path('logout', views.LogoutView.as_view(), name="logout_view"),
    path('signin', views.SignInView.as_view(), name="sign_in_view"),
    path('signup', views.SignUpView.as_view(), name="sign_up_view"),
]