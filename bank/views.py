from django.shortcuts import render, redirect
from .models import User
# Create your views here.
import requests
import json
from .forms import DonarForm

donarblood = {
    'A+': ['A-', 'O+', 'O-'],
    'B+': ['B-', 'O+', 'O-'],
    'A-': ['O-'],
    'B-': ['O-'],
    'AB+': ['A+', 'B+', 'O+', 'O-', 'A-', 'B-', 'AB-'],
    'AB-': ['A-', 'B-', 'O-'],
    'O+': ['O-'],
    'O-': [],
}


def home(request):
    return render(request, 'bank/home.html')


def results(request):
    location = request.GET['location']
    blood = request.GET['blood']
    user_at_location = User.objects.filter(city__iexact=location)
    user_same_blood = user_at_location.filter(blood_group__iexact=blood)

    user_can_donate = User.objects.none()
    for bld in donarblood[blood]:
        users_with_bld = user_at_location.filter(blood_group__iexact=bld)
        user_can_donate |= users_with_bld
    print(user_same_blood)
    print(user_can_donate)
    bldcnt = user_same_blood.count()
    response = requests.get(
        'https://api.data.gov.in/resource/fced6df9-a360-4e08-8ca0-f283fc74ce15?api-key=579b464db66ec23bdd00000167e6cabfab3040ea41287770d6615098&limit=2800&format=json').json()['records']
    # print(response)
    bloodbank = []
    for rs in response:
        if rs['__city'].lower() == location.lower():
            dic = {
                'name': rs['_blood_bank_name'],
                'state': rs['__state'],
                'city': rs['__city'],
                'address': rs['__address'],
                'mobile': rs['_mobile'],
            }
            bloodbank.insert(0, dic)

    # print(bloodbank)
    bloodbankcnt = len(bloodbank)
    return render(request, 'bank/results.html', {
        'location': location,
        'blood': blood,
        'useratlocation': user_at_location,
        'usersameblood': user_same_blood,
        'userscandonate': user_can_donate,
        'cnt': bldcnt,
        'bloodbank': bloodbank,
        'bloodbankcnt': bloodbankcnt,
    })


def get_user(request, userid):
    user = User.objects.get(id=userid)
    context = {'user': user}
    return render(request, 'bank/userdetails.html', context)


def donarform(request):
    form = DonarForm()
    if request.method == 'POST':
        form = DonarForm(request.POST)
        # print(form.can_donate)
        # form.can_donate = True
        if form.is_valid():
            print('hi')
            form.save()
            return redirect('home')

    content = {'form': form}
    return render(request, 'bank/userform.html', content)
