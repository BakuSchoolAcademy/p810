from django.shortcuts import render


def contact(request):
    """
    contact view 
    indi duzelmelidir
    """
    return render(request, "contact/index.html")
