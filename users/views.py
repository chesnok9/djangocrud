from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import (CreateView, DeleteView, UpdateView)
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django import forms
import csv

from users.templatetags.user_filters import allowed, bizzfuzz
from .models import CustomUser
from .forms import CreateUserForm

class UserList(ListView):
    model = CustomUser

class UserDetailView(DetailView):
    model = CustomUser

class UserCreateView(CreateView):
    form_class = CreateUserForm
    model = CustomUser
    success_url = reverse_lazy('users:user-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        print(self.object.password)
        self.object.set_password(self.object.password)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class UserUpdateView(UpdateView):
    form_class = CreateUserForm
    model = CustomUser
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('users:user-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['password'].widget = forms.PasswordInput()
        return form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        print(self.object.password)
        self.object.set_password(self.object.password)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class UserDeleteView(DeleteView):
    model = CustomUser
    success_url = reverse_lazy('users:user-list')


def exportToCSV(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="milotest.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'Birthday', 'Eligible', 'Random Number', 'BizzFuzz'])

    users = CustomUser.objects.all()
    for user in users:
        writer.writerow([user.username, user.birth_date, allowed(user.birth_date), user.random_number, bizzfuzz(user.random_number)])

    return response