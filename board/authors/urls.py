from django.urls import path

from advertisements.views import AuthorAdvertisementListView, AuthorAdvertisementEditView
from authors.views import AnotherLoginView, AnotherLogoutView, register_view, \
    AuthorEditFormView, AuthorPasswordResetView, AuthorPasswordResetDoneView, AuthorPasswordResetConfirmView

urlpatterns = [
    path('login/', AnotherLoginView.as_view(), name='login'),
    path('logout/', AnotherLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('edit/', AuthorEditFormView.as_view(), name='edit_author'),
    path('password_reset/', AuthorPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done', AuthorPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', AuthorPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('advertisements/', AuthorAdvertisementListView.as_view(), name='author_advertisements'),
    path('advertisement/<int:advertisement_id>', AuthorAdvertisementEditView.as_view(), name='edit_advertisement')
]
