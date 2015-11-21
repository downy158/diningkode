from django.shortcuts import render
from django.http import Http404

restaurants = [{
                "name": "mcdonalds", 
                "price": "$", 
                "review": "its ok",
                "rating": 3,
                "phone": "02-123-1234",
                "address": "123 fake street",
                "image": "https://igcdn-photos-a-a.akamaihd.net/hphotos-ak-xfa1/t51.2885-15/e35/11820669_781036755340552_1301778049_n.jpg"
               }, 
               {
                "name": "burger_king", 
                "price": "$$", 
                "review": "flame grilled burgers!",
                "rating": 5,
                "phone": "02-234-2345",
                "address": "124 real avenue",
                "image": "https://igcdn-photos-d-a.akamaihd.net/hphotos-ak-xap1/t51.2885-15/s750x750/sh0.08/e35/12142091_980840855305675_1952232999_n.jpg"
               },
               {
                "name": "KFC", 
                "price": "$$", 
                "review": "fried chicken is great!",
                "rating": 4,
                "phone": "02-345-3456",
                "address": "125 unreal court",
                "image": "https://igcdn-photos-e-a.akamaihd.net/hphotos-ak-xtf1/t51.2885-15/e35/11850418_412365505620396_1952467682_n.jpg"
               }]
# helper functions
def find_restaurant_by_name(restaurants, name):
    # code here!
    for resto in restaurants:
        if resto['name'] == name:
            return resto
    return None
            # ex. find_restaurant_by_name(restaurants, "mcdonalds") returns the dict of mcdonalds

def filter_restaurants_by_rating(restaurants, rating):
    # code here!
    filter_restaurants = []
    for resto in restaurants:
        if resto['rating'] >= rating:
            filter_restaurants.append(resto)

    return filter_restaurants


    # ex. filter_restaurants_by_rating(restaurants, 4) returns a list of dictionaries that include burger_king and KFC

def list(request):
    return render(request, 'restaurants/list.html', {"restaurants": restaurants})

def detail(request, name):
    # code here!
    restoname= find_restaurant_by_name(restaurants, name)
    return render(request, 'restaurants/detail.html', {"restoname": restoname})

def rating(request, value):
    # code here!
    value = int(value)
    restaurant = filter_restaurants_by_rating(restaurants, value)
    return render(request, 'restaurants/rating.html', {"restaurant": restaurant, "value": value})

