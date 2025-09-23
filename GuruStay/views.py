from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Property, Booking
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect


# Create your views here.



class HomeView(TemplateView):
    template_name = 'GuruStay/home.html'


@login_required(login_url='login')
def dashboard(request):
    assets = Property.objects.all()
    context = {
        "assets": assets
    }
    return render(request, 'GuruStay/dashboard.html', context)


class PropertyCreateView(CreateView):
    model = Property
    success_url = reverse_lazy('dashboard')
    fields = ['title', 'location', 'image', 'price_per_night', 'description']
    template_name = 'GuruStay/property_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)



class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    fields = ["check_in", "check_out", "guests"]
    template_name = "GuruStay/booking.html"
    success_url = "GuruStay/payment.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.property = Property.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["asset"] = get_object_or_404(Property, pk=self.kwargs["pk"])
        return context
    
@login_required
def become_host(request):
    request.user.is_host = True
    request.user.save()
    return redirect("dashboard")