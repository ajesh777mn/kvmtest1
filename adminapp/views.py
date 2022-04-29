from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from adminapp.models import *#importing tables


from django.http import HttpResponse
# from weasyprint import HTML




# Create your views here.
def home(request):
    wp1=home_wallpaper.objects.get(id=1)#uid possition values will be stored in data
    wp2=home_wallpaper.objects.get(id=2)#uid possition values will be stored in data
    wp3=home_wallpaper.objects.get(id=3)#uid possition values will be stored in data

    return render(request,'adminapp/home.html',{'wp1':wp1,'wp2':wp2,'wp3':wp3})




    

def online_appl(request):
        return render(request,'adminapp/online_appl.html')

        # Render html content through html template with context
    # template = get_template(settings.PDF_TEMPLATE)
    # context = {
    #         'invoice': self,
    # }

    # html = template.render(context)

    #     # Write PDF to file
    # document_html = HTML(string=html, base_url=request.build_absolute_uri())
    # document = document_html.render()
    # if len(document.pages) > 1:
    #     for page in document.pages[1:]:
    #         str(page)
    #         pdf = document.write_pdf()
    # else:
    #     pdf = document.write_pdf()
    #     #response = HttpResponse(html)
    #     response = HttpResponse(pdf, content_type='application/pdf')
    #     response['Content-Disposition'] = 'filename="Invoice {0} | Invoice {0}.pdf"'.format(self.id)
    #     return response 