from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    path('about/', views.About.as_view(), name='about'),
    path('advertisements/', views.AdvertisementListView.as_view(), name='advertisements'),
    path('advertisements/add', views.AdvertisementAddView.as_view(), name='advertisement_add'),
    path('advertisements/<int:rubric_id>/', views.AdvertisementByRubricListView.as_view(), name='by_rubric'),
    path('advertisement/<int:pk>', views.AdvertisementDetailView.as_view(), name='advertisement-detail'),
]
