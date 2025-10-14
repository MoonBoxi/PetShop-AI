from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Service, TimeSlot, Booking, ServiceType
from .forms import BookingForm
from .services import get_or_create_time_slots
from datetime import datetime

def service_list(request, service_type_id=None):
    service_type = None
    services = Service.objects.all()

    if service_type_id:
        service_type = get_object_or_404(ServiceType, id=service_type_id)
        services = services.filter(service_type=service_type)

    context = {
        'service_type': service_type,
        'services': services
    }
    return render(request, 'scheduling/service_list.html', context)

@login_required
def select_date(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'scheduling/select_date.html', {'service': service})

@login_required
def select_time_slot(request, service_id, date):
    service = get_object_or_404(Service, id=service_id)
    date_obj = datetime.strptime(date, '%Y-%m-%d').date()
    time_slots = get_or_create_time_slots(date_obj, service.service_type.name)
    available_slots = [slot for slot in time_slots if slot.is_available]

    return render(request, 'scheduling/select_time_slot.html', {
        'service': service,
        'date': date_obj,
        'time_slots': available_slots
    })

@login_required
def book_service(request, service_id, time_slot_id):
    service = get_object_or_404(Service, id=service_id)
    time_slot = get_object_or_404(TimeSlot, id=time_slot_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.service = service
            booking.time_slot = time_slot
            booking.save()

            time_slot.is_available = False
            time_slot.save()

            return redirect('scheduling:booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()

    return render(request, 'scheduling/book_service.html', {
        'service': service,
        'time_slot': time_slot,
        'form': form
    })

@login_required
def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'scheduling/booking_confirmation.html', {'booking': booking})