from datetime import timedelta

from time_slots.time_slot_manager import TimeSlotManager
from time_slots.time_slot import TimeSlot


def test_time_slot_is_available_when_no_other_slots(now):
    slot_manager = TimeSlotManager()
    assert slot_manager.is_time_slot_available(TimeSlot(now, now + timedelta(minutes=30)))


def test_time_slot_not_available(now):
    slot_manager = TimeSlotManager()
    slot_manager.add_time_slot(
            TimeSlot(now + timedelta(minutes=15), now + timedelta(minutes=45))
    )
    assert not slot_manager.is_time_slot_available(
        TimeSlot(now, now + timedelta(minutes=30)))


def test_time_slot_not_available_when_between_two_slots(now):
    slot_manager = TimeSlotManager()
    slot_manager.add_time_slot(
        TimeSlot(now, now + timedelta(minutes=30))
    )
    slot_manager.add_time_slot(
        TimeSlot(now + timedelta(minutes=40), now + timedelta(minutes=60))
    )
    assert not slot_manager.is_time_slot_available(
        TimeSlot(now + timedelta(minutes=15), now + timedelta(minutes=45))
    )


def test_time_slot_available_when_exactly_at_start(now):
    slot_manager = TimeSlotManager()
    slot_manager.add_time_slot(
        TimeSlot(now + timedelta(minutes=30), now + timedelta(minutes=60))
    )
    assert slot_manager.is_time_slot_available(
        TimeSlot(now, now + timedelta(minutes=30))
    )


def test_time_slot_available_when_exactly_at_end(now):
    slot_manager = TimeSlotManager()
    slot_manager.add_time_slot(TimeSlot(now, now + timedelta(minutes=30)))
    assert slot_manager.is_time_slot_available(
        TimeSlot(now + timedelta(minutes=30), now + timedelta(minutes=60)))

    
def test_time_slot_available_when_multiple_slots(now):
    slot_manager = TimeSlotManager()
    slot_manager.add_time_slot(TimeSlot(now, now + timedelta(minutes=30)))
    slot_manager.add_time_slot(TimeSlot(now + timedelta(minutes=60), now + 
                                        timedelta(minutes=80)))
    assert slot_manager.is_time_slot_available(
        TimeSlot(now + timedelta(minutes=30), now + timedelta(minutes=60))
    )