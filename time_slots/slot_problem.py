from time_slots.time_slot import TimeSlot


def is_time_slot_available(requested_slot: TimeSlot, timeslots: list[TimeSlot]) -> bool:
    for slot in timeslots:
        if slot.overlaps(requested_slot):
            return False
    return True