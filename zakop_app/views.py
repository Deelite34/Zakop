from django.shortcuts import render

from .forms import AddFindingUrlForm
from .models import user as user_model
# Create your views here.


def index(request):
    return render(request, 'zakop_app/index.html')


def add_finding(request):
    if request.method == 'GET':
        form = AddFindingUrlForm()
    else:
        form = AddFindingUrlForm(data=request.POST)
        if form.is_valid():
            new_finding = form.save(commit=False)
            new_finding.user_id = request.user.id
            # user_model.objects.raw(f"SELECT user_id FROM users WHERE name=\'{request.user.username}\';")
            new_finding.title = request.title
            new_finding.description = request.description
            new_finding.permalink = request.permalink
            new_finding.save()
            return HttpResponseRedirect(reverse('zakop_app:index'))
    current_user = request.user
    print(f'User {request.user.username} with id:{current_user.id} has attempted to add finding')
    return render(request, 'zakop_app/add_finding.html', {'form': form})
