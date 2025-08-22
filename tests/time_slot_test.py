from datetime import timedelta

from time_slots.time_slot import TimeSlot


def test_time_slot_overlaps(now):
    slot1 = TimeSlot(now, now + timedelta(minutes=30))
    slot2 = TimeSlot(now + timedelta(minutes=15), now + timedelta(minutes=45))
    assert slot1.overlaps(slot2)


def test_time_slot_does_not_overlap(now):
    slot1 = TimeSlot(now, now + timedelta(minutes=30))
    slot2 = TimeSlot(now + timedelta(minutes=30), now + timedelta(minutes=45))
    assert not slot1.overlaps(slot2)
