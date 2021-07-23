from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.utils.translation import gettext as _
from django.db.models import Q

from advertisements.forms import AdvertisementForm, SearchForm
from advertisements.models import Advertisement, Author, Rubric


class MainView(View):
    def get(self, request):
        rubrics = Rubric.objects.all()
        advertisements = Advertisement.objects.all()[:10]
        context = {
            'title': _('Главная'),
            'name': _('Доска объявлений'),
            'rubrics': rubrics,
            'advertisements_list': advertisements
        }
        return render(request, 'advertisements/index.html', context=context)


class Contacts(TemplateView):
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Контакты')
        context['phone'] = '0-800-123-456'
        context['email'] = 'admin@admin.com'
        rubrics = Rubric.objects.all()
        context['rubrics'] = rubrics
        return context


class About(TemplateView):
    template_name = 'advertisements/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('О нас')
        context['name'] = _('Региональная доска объявлений')
        context['description'] = _('На сайте можно дать объявление о продаже/покупке/аренде')
        rubrics = Rubric.objects.all()
        context['rubrics'] = rubrics
        return context


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisements/advertisements.html'
    context_object_name = 'advertisements_list'
    # status = 'Активно'
    # status_active_id = AdvertisementStatus.objects.filter(name=status).get().pk
    # queryset = Advertisement.objects.filter(status=status_active_id)
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        advertisements = Advertisement.objects.filter(rubric=self.kwargs['rubric_id'])
        if 'keyword' in self.request.GET:
            keyword = self.request.GET['keyword']
            q = Q(title__icontains=keyword) or Q(description__icontains=keyword)
            advertisements = advertisements.filter(q)
        else:
            keyword = ''
        form = SearchForm(initial={'keyword': keyword})
        context['title'] = _('Объявления')
        context['form'] = form
        return context


class AdvertisementByRubricListView(AdvertisementListView):
    paginate_by = 5

    def get_queryset(self):
        advertisements = Advertisement.objects.filter(rubric=self.kwargs['rubric_id'])
        keyword = ''
        if 'keyword' in self.request.GET:
            keyword = self.request.GET['keyword']
            q = Q(title__contains=keyword) | Q(description__contains=keyword)
            advertisements = advertisements.filter(q)
        return advertisements

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rubric_id = self.kwargs['rubric_id']
        current_rubric = Rubric.objects.get(pk=rubric_id)
        rubrics = Rubric.objects.all()
        context['title'] = current_rubric
        context['rubrics'] = rubrics
        return context


class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'advertisements/advertisement_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['object']
        rubrics = Rubric.objects.all()
        context['rubrics'] = rubrics
        return context


class AdvertisementAddView(DetailView):

    def get(self, request):

        try:
            author = Author.objects.get(user=self.request.user)
        except Author.DoesNotExist:
            author = None

        if author:
            form = AdvertisementForm()
            context = {
                'form': form,
                'author': author
            }
        else:
            context = {
                'message': _('Вы не зарегистрированы как автор'),
                'author': author
            }
        return render(request, 'advertisements/add_advertisement.html', context=context)

    def post(self, request):
        form = AdvertisementForm(request.POST, request.FILES)
        author = Author.objects.get(user=request.user)
        if form.is_valid():
            Advertisement.objects.create(**form.cleaned_data, author=author)
            context = {
                'form': form,
                'message': _('Добавлено')
            }
        else:
            form = AdvertisementForm()
            context = {
                'form': form,
            }
        return render(request, 'advertisements/add_advertisement.html', context=context)


class AuthorAdvertisementListView(ListView):
    model = Advertisement
    context_object_name = 'advertisements_list'
    template_name = 'authors/author_advertisements.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            author = Author.objects.get(user=self.request.user)
        except Author.DoesNotExist:
            author = None
            context['message'] = _('Вы не зарегистрированы как автор')
        if author is not None and self.queryset is None:
            context['message'] = _('Объявлений нет')
        return context

    def get_queryset(self):
        try:
            author = Author.objects.get(user=self.request.user)
            queryset = Advertisement.objects.filter(author=author)
        except Author.DoesNotExist:
            queryset = []
        return queryset


class AuthorAdvertisementEditView(View):
    def get(self, request, advertisement_id):
        advertisement = Advertisement.objects.get(id=advertisement_id)
        advertisement_form = AdvertisementForm(instance=advertisement)
        context = {
            'title': 'Личный кабинет',
            'form': advertisement_form,
            'advertisement_id': advertisement_id
        }
        return render(request, 'advertisements/advertisement_edit.html', context=context)

    def post(self, request, advertisement_id):
        advertisement = Advertisement.objects.get(id=advertisement_id)
        advertisement_form = AdvertisementForm(request.POST, request.FILES, instance=advertisement)

        if advertisement_form.is_valid():
            advertisement_form.save()
        context = {
            'form': advertisement_form,
            'message': _('Сохранено')
        }
        return render(request, 'advertisements/advertisement_edit.html', context=context)
