from django.shortcuts import render, redirect
from django.views import View
from .models import Ticket

l = []


class Home(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):

        ticketinfo = Ticket(date_time=request.POST["ticketdetails"],
                            Location=request.POST["location"])
        ticketinfo.save()

        return redirect("/new/", {})


class newpage(View):
    def get(self, request):
        parkticket = list(Ticket.objects.all())
        print(parkticket[0])
        return render(request, 'new.html', {"tickets": parkticket})
