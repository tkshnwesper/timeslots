from datetime import timedelta

from time_slots.slot_problem import is_time_slot_available
from time_slots.time_slot import TimeSlot


def test_time_slot_is_available_when_no_other_slots(now):
    assert is_time_slot_available(TimeSlot(now, now + timedelta(minutes=30)), [])


def test_time_slot_not_available(now):
    assert not is_time_slot_available(
        TimeSlot(now, now + timedelta(minutes=30)), [
            TimeSlot(now + timedelta(minutes=15), 
                     now + timedelta(minutes=45))
                     ])


### below test cases are not necessary - for illustration purpose only ###


def test_time_slot_available_when_no_overlap(now):
    assert is_time_slot_available(
        TimeSlot(now + timedelta(minutes=30), now + timedelta(minutes=60)), [
            TimeSlot(now, now + timedelta(minutes=30))
        ]
    )


def test_time_slot_not_available_when_between_two_slots(now):
    assert not is_time_slot_available(
        TimeSlot(now + timedelta(minutes=15), now + timedelta(minutes=45)), [
            TimeSlot(now, now + timedelta(minutes=30)),
            TimeSlot(now + timedelta(minutes=40), now + timedelta(minutes=60))
        ]
    )


def test_time_slot_available_when_exactly_at_start(now):
    assert is_time_slot_available(
        TimeSlot(now, now + timedelta(minutes=30)), [
            TimeSlot(now + timedelta(minutes=30), now + timedelta(minutes=60))
        ]
    )


def test_time_slot_available_when_exactly_at_end(now):
    assert is_time_slot_available(
        TimeSlot(now + timedelta(minutes=30), now + timedelta(minutes=60)), [
            TimeSlot(now, now + timedelta(minutes=30))
        ]
    )


def test_time_slot_available_when_multiple_slots(now):
    assert is_time_slot_available(
        TimeSlot(now + timedelta(minutes=30), now + timedelta(minutes=60)), [
            TimeSlot(now, now + timedelta(minutes=30)),
            TimeSlot(now + timedelta(minutes=60), now + timedelta(minutes=80))
        ]
    )