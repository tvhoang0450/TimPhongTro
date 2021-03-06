from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
from django.views import View

from .models import NguoiDung
from .forms import NguoiDungForm
from PhongTro.models import PhongTro


class LoginClass(View):
    def get(self, request):
        return render(request, 'NguoiDung/login.html')

    def post(self, request):
        tk = request.POST.get('username')
        mk = request.POST.get('password')
        my_user = authenticate(username=tk, password=mk)
        if my_user is None:
            return HttpResponse('User không tồn tại, Đăng nhập thất bại')
        login(request, my_user)
        return redirect('/', {'username': tk})


class RegisterClass(View):
    def get(self, request):
        a = NguoiDungForm()
        return render(request, 'NguoiDung/register.html', {'f': a})

    def post(self, request):
        nd = NguoiDungForm(request.POST)
        if nd.is_valid():
            nd.save()
            return redirect('/NguoiDung/login')
        else:
            return HttpResponse('Dwx liệu không validate')


class ProfileClass(View):
    def get(self, request, **kwargs):
        a = self.request.GET.get('id')
        user_id = self.request.user
        print(a)
        print(self)
        dsach_tin_dang = PhongTro.objects.filter(NguoiDung_id=user_id)
        return render(request, 'NguoiDung/profile.html', {'dsach_tin_dang': dsach_tin_dang})
