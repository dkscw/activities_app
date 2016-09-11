from django.conf.urls import url
import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^activities/$', views.ActivityList.as_view()),
    url(r'^activity/(?P<pk>[0-9]+)/$', views.ActivityDetail.as_view()),
]