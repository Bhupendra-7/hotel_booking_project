from django.shortcuts import render,get_object_or_404, redirect
from .models import Room
from .forms import BookingForm


def room_list(request):
    rooms = Room.objects.filter(is_available=True)
    unavailable_rooms = Room.objects.filter(is_available=False)
    context = {
        'rooms': rooms,
        'unavailable_rooms': unavailable_rooms,
    }
    return render(request, 'booking/room_list.html', context)




def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    context = {
        'room': room,
    }
    return render(request, 'booking/room_detail.html', context)



def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.save()
            room.is_available = False
            room.save()
            return redirect('room_list')
    else:
        form = BookingForm()

    return render(request, 'booking/book_room.html', {'form': form, 'room': room})