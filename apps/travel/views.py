from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Trip, Travel_Companions, User

# Create your views here.
def index(request):
    user = request.session["logged_in_user"]
    all_trips = Trip.objects.all()
    all_trips_list = list(all_trips)
    joined_trips_list = []
    joined_trips = Travel_Companions.objects.filter(companion_id = request.session["logged_in_user"])
    for trip in joined_trips:
        joined_trips_list.append(trip.trip)
    # print other_trips
    # print all_trips_list
    other_trips = [item for item in all_trips_list if item not in joined_trips_list]
    print other_trips
    context = {
        "user": User.objects.get(id = request.session["logged_in_user"]),
        "all_trips": Trip.objects.all(),
        "trips": other_trips,
        "companions": Travel_Companions.objects.filter(companion_id = request.session["logged_in_user"]),
        "other_trips": other_trips
    }
    return render(request, "travel/index.html", context)

def add(request):
    print ("*"*50)
    if request.method == "POST":
        submitted_data = {
            "trip_name": request.POST["trip_name"],
            "trip_destination": request.POST["trip_destination"],
            "trip_description": request.POST["trip_description"],
            "trip_begin": request.POST["trip_begin"],
            "trip_end": request.POST["trip_end"],
            "created_by": request.session["logged_in_user"],
        }
        results = Trip.objects.trip_validator(submitted_data)
        # print ("*"*50)
        # for item in Trip.objects.all():
        #     print item.id, item.trip_name, item.trip_destination, item.created_by
        # print ("*"*50)
        if results[0]:
            messages.success(request, "Trip successfully added!")
            new_trip = Trip.objects.last()
            Travel_Companions.objects.create(trip = new_trip, companion = User.objects.get(id = request.session["logged_in_user"]))
            return redirect("travel:main")
        else:
            for error in results[1]:
                messages.error(request, error)
            return redirect("travel:new_trip")
    return redirect(reverse("travel:main"))

def new(request):
    context = {
        "user": User.objects.get(id = request.session["logged_in_user"]),
        # "trips_joined": trips_joined
    }
    return render(request, "travel/new.html", context)

def show(request, trip_id):
    companions = Travel_Companions.objects.filter(trip = trip_id)
    context = {
        "user": User.objects.get(id = request.session["logged_in_user"]),
        "trip": Trip.objects.get(id = trip_id),
        "companions": companions
    }
    print ("*"*50)
    # for item in context[trip]:
    #     print item.id, item.trip_name, item.trip_destination
    # for people in companions:
    #     print people.id, people.first_name, people.last_name
    # print ("*"*50)
    return render(request, "travel/trip.html", context)

def join(request, trip_id):
    trip = Trip.objects.get(id = trip_id)
    roster = Travel_Companions.objects.create(trip = trip, companion = User.objects.get(id = request.session["logged_in_user"]))
    # print ("*"*50)
    # for names in Course_Student_List.objects.all():
    #     print names.id, names.student.first_name, names.course.course_name_id.course_name
    # print ("*"*50)
    messages.success(request, "You are now part of the expedition:" + trip.trip_name)
    return redirect(reverse("travel:main"))
    # return redirect(reverse("travel:show_trip", kwargs={"trip_id": trip.id}))
