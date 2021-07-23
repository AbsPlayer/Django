from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView
from django.shortcuts import render, redirect
from django.views import View
from django.utils.translation import gettext as _

from advertisements.models import Author
from authors.forms import ExtendedRegisterForm, AuthorForm, AuthorLoginForm


class AnotherLoginView(LoginView):
    authentication_form = AuthorLoginForm
    template_name = 'authors/login.html'


class AnotherLogoutView(LogoutView):
    next_page = '/'


def register_view(request):
    if request.method == 'POST':
        form = ExtendedRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            web = form.cleaned_data.get('web')
            facebook = form.cleaned_data.get('facebook')
            viber = form.cleaned_data.get('viber')
            telegram = form.cleaned_data.get('telegram')
            whatsapp = form.cleaned_data.get('whatsapp')
            skype = form.cleaned_data.get('skype')
            other_contact = form.cleaned_data.get('other_contact')
            Author.objects.create(
                user=user,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                web=web,
                facebook=facebook,
                viber=viber,
                telegram=telegram,
                whatsapp=whatsapp,
                skype=skype,
                other_contact=other_contact
            )
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = ExtendedRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'authors/register.html', context=context)


class AuthorEditFormView(View):

    def get(self, request):

        try:
            author = Author.objects.get(user=self.request.user)
        except Author.DoesNotExist:
            author = None

        if author:
            author = Author.objects.get(user=request.user)
            form = AuthorForm(instance=author)
            context = {
                'form': form,
            }
        else:
            context = {
                'message': _('Вы не зарегистрированы как автор')
            }
        return render(request, 'authors/edit.html', context=context)

    def post(self, request):
        author = Author.objects.get(user=request.user)
        form = AuthorForm(request.POST, instance=author)

        if form.is_valid():
            author.save()
        context = {
            'form': form,
            'message': _('Сохранено')
        }
        return render(request, 'authors/edit.html', context=context)


class AuthorPasswordResetView(PasswordResetView):
    template_name = 'authors/reset_password.html'
    subject_template_name = 'authors/reset_subject.txt'
    email_template_name = 'authors/reset_email.html'


class AuthorPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'authors/password_reset_done.html'


class AuthorPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'authors/password_reset_confirm.html'
    post_reset_login = True
    success_url = '/'
