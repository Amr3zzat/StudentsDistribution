
from django.conf.urls import url
from django.contrib import admin
from helwan import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^addstudent/$', views.add_stu),
    url(r'^accounts/login/$',views.signin),
    url(r'^accounts/logout/$',views.signout),
    url(r'^panel/$',views.list),
    url(r'^select/$', views.update_profile),
    url(r'^contact/$', views.contact),
    url(r'^set/$', views.setper),
    url(r'^calculate/$', views.calc),

]
