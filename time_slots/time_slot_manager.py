from typing import List

from time_slots.time_slot import TimeSlot


class TimeSlotManager:
    def __init__(self):
        self.slots: List[TimeSlot] = []
    

    def add_time_slot(self, time_slot: TimeSlot):
        self.slots.append(time_slot)


    def is_time_slot_available(self, requested_slot: TimeSlot) -> bool:
        for slot in self.slots:
            if slot.overlaps(requested_slot):
                return False
        return True
