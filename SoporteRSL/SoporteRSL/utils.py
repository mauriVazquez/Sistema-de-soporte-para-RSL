from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def redireccionar(request):
    return redirect('inicio/')