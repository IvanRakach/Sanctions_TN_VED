from django.shortcuts import render

# Create your views here.


def index(request):
    param_for_render = {
        'header_phones': "header_phones",
        'title': 'Проверка кодов ТН ВЭД'
    }
    return render(request, 'tn_ved_main/index.html', context=param_for_render)
