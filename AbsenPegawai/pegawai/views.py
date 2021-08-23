from django.shortcuts import render
from django.views.generic import CreateView, ListView
from . import models
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'index.html')

class AbsenCreateView(CreateView):
    model = models.Post
    fields = ['kategori']
    def form_valid(self, form):
        form.instance.nama = self.request.user
        return super().form_valid(form)
    template_name = "absen.html"


class absensiListView(ListView):
    model = models.Post
    context_object_name = "absen"
    ordering = ['-waktu']
    template_name = "index.html"








def pegawai_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})

def pegawai_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

