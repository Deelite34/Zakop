from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import AddFindingUrlForm
from .models import User, Finding
from django.urls import reverse
# Create your views here.


def index(request):
    limit = 10
    findings = Finding.objects.order_by('finding_date')[:limit]
    context = {'findings': findings}
    return render(request, 'zakop_app/index.html', context)


def add_finding(request):
    if request.method == 'GET':
        form = AddFindingUrlForm()
    else:
        form = AddFindingUrlForm(data=request.POST)
        if form.is_valid():
            new_finding = form.save(commit=False)
            user = User.objects.get(id=request.user.id)
            new_finding.user_id = request.user
            new_finding.save()
            return HttpResponseRedirect(reverse('zakop_app:index'))
    current_user = request.user
    print(f'User {request.user.username} with id:{current_user.id} has attempted to add finding')
    return render(request, 'zakop_app/add_finding.html', {'form': form})
