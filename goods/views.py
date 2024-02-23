from django.shortcuts import render

# Create your views here.


def catalog(request):
    context = {
        'title': "Home - Catalog",
        'goods': [
            {'image': 'deps/images/goods/set of tea table and three chairs.jpg',
             'name': 'Чайный столик и три стула',
             'description': 'Комплект из трёх стульев и дизайнерский столик для гостинной комнаты.',
             'price': 150.00},

            {'image': 'deps/images/goods/set of tea table and two chairs.jpg',
             'name': 'Чайный столик и два стула',
             'description': 'Набор из стола и двух стульев в минималистическом стиле.',
             'price': 93.00},

            {'image': 'deps/images/goods/double bed.jpg',
                'name': 'Двухспальная кровать',
                'description': 'Кровать двухспальная с надголовником и вообще очень ортопедичная.',
                'price': 670.00}
        ]
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
