from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from front.forms import FormQuotation


class Home(View):
    form_class = FormQuotation
    template_name = 'front/home.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})
