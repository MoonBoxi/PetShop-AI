from datetime import datetime, timedelta
from .models import TimeSlot, ServiceType

def get_or_create_time_slots(date, service_type_name):
    service_type = ServiceType.objects.get(name=service_type_name)
    time_slots = TimeSlot.objects.filter(date=date, service_type=service_type)
    if not time_slots.exists():
        time_slots = generate_time_slots(date, service_type)
    return time_slots

def generate_time_slots(date, service_type):
    time_slots = []
    working_hours = [
        (timedelta(hours=8), timedelta(hours=12, minutes=30)),
        (timedelta(hours=14), timedelta(hours=18, minutes=30))
    ]

    for start, end in working_hours:
        current_time = start
        while current_time < end:
            slot_start_time = (datetime.min + current_time).time()
            slot_end_time = (datetime.min + current_time + timedelta(minutes=30)).time()
            if current_time + timedelta(minutes=30) <= end:
                time_slot = TimeSlot.objects.create(
                    service_type=service_type,
                    date=date,
                    start_time=slot_start_time,
                    end_time=slot_end_time
                )
                time_slots.append(time_slot)
            current_time += timedelta(minutes=30)
    return time_slots
