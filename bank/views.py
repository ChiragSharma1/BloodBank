from django.shortcuts import render, redirect
from BloodBank.settings import BLOOD_BANK_API_KEY
from .models import User
# Create your views here.
import requests
import json
from .forms import DonarForm
import folium

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
    location = request.GET['location'].title()
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
        'https://api.data.gov.in/resource/fced6df9-a360-4e08-8ca0-f283fc74ce15?api-key=' + BLOOD_BANK_API_KEY + '&limit=2800&format=json&filters[__city]='+location).json()['records']
    # print(response)
    bloodbank = []
    # adding map
    if len(response) != 0:
        latitude = float(response[0]['__latitude'])
        longitude = float(response[0]['__longitude'])
        m = folium.Map(location=[latitude, longitude], zoom_start=13)
    else:
        m = folium.Map()
    for rs in response:
        dic = {
            'id': rs['sr_no'],
            'name': rs['_blood_bank_name'],
            'state': rs['__state'],
            'city': rs['__city'],
            'address': rs['__address'],
            'mobile': rs['_mobile'],
        }
        latitude = float(rs['__latitude'])
        longitude = float(rs['__longitude'])
        folium.Marker([latitude, longitude],
                      tooltip="Click for more",
                      popup=rs['_blood_bank_name']).add_to(m)
        bloodbank.insert(0, dic)

    # print(bloodbank)
    m = m._repr_html_()
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
        'm': m,
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


def get_bank(request, bankid):
    bankid = str(bankid)
    bank = requests.get(
        'https://api.data.gov.in/resource/fced6df9-a360-4e08-8ca0-f283fc74ce15?api-key=' + BLOOD_BANK_API_KEY + '&limit=2800&format=json&filters[sr_no]='+bankid).json()['records'][0]
    longitude = float(bank['__longitude'])
    latitude = float(bank['__latitude'])
    m = folium.Map(location=[latitude, longitude], zoom_start=13)
    folium.Marker([latitude, longitude],
                  tooltip="Click for more",
                  popup=bank['_blood_bank_name']).add_to(m)
    bank_details = {
        'name': bank['_blood_bank_name'],
        'state': bank['__state'],
        'city': bank['__city'],
        'pincode': bank['_pincode'],
        'address': bank['__address'],
        'email': bank['_email'],
        'mobile_number': bank['_mobile'],
        'contact_number': bank['__contact_no'],
        'timing': bank['__service_time'],
    }
    m = m._repr_html_()
    return render(request, 'bank/bank.html', {
        'm': m,
        'bank': bank_details,
    })
