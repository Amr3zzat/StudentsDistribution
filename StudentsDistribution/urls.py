
from django.conf.urls import url ,include
from django.contrib import admin
from helwan import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add_stu/$', views.add_stu),
    url(r'^login/$',views.signin),
    url(r'^logout/$', views.signout),
    url(r'^list/$',views.list),
    url(r'^select/$', views.update_profile),

]
