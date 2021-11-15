from django.shortcuts import render

from . import forms
from django.http import HttpResponse
from .data_processing import financial_data_display, financial_data_plot
import matplotlib.pyplot as plt
import io
import base64


# Create your views here.

def base_page_view(request):
    if request.method == "POST":
        form = forms.ExcellFileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            excel_file = cleaned_data.get('excel_file')
            if "plot" in request.POST:
                plot = financial_data_plot(excel_file)
                return render(
                    request,
                    template_name="financial_data_analysing/base_page.html",
                    context={
                        'graphic': plot
                    }
                )
            else:
                rows = financial_data_display(excel_file)
                return render(
                    request,
                    template_name="financial_data_analysing/base_page.html",
                    context={
                        'rows': rows
                    }
                )
        else:
            return HttpResponse(f"{form.errors.get('excel_file')}")
    return render(request,
                  template_name='financial_data_analysing/base_page.html',
                  context={
                      'form': forms.ExcellFileForm()
                  }
                  )
