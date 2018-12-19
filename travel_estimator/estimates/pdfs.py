# -*- coding: utf-8 -*-
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4


def render_to_pdf(my_page):
    """ https://docs.djangoproject.com/en/dev/howto/outputting-pdf/ """

    response = HttpResponse(content_type='application/pdf')
    # uncomment to toggle: downloading | display (moz browser)
    # response['Content-Disposition'] = 'attachment; filename="myfilename.pdf"'

    c = canvas.Canvas(response, pagesize=letter)
    # c.setLineWidth(.3)
    # c.setFont('Helvetica', 12)
   
    c.drawString(30, 750, "Name: {}".format(my_page.estimate_name))
    c.drawString(30, 735, "Other Information")
    c.drawString(415, 750, "Travel Date: {}".format(my_page.start_date))
    c.line(480,747,580,747)
    
    c.drawString(275,725,'AMOUNT OWED:')
    c.drawString(500,725,"$1,000.00")
    c.line(378,723,580,723)
 
    c.drawString(30,703,'RECEIVED BY:')
    c.line(120,700,580,700)
    c.drawString(120,703,"JOHN DOE")
    
    # c.drawString(100, 660, my_page.agent)
    c.showPage
    c.save()
    return response

