from dataclasses import dataclass
from datetime import datetime


@dataclass
class TimeSlot:
    start: datetime
    end: datetime

    def overlaps(self, other: 'TimeSlot') -> bool:
        return self.start < other.end and other.start < self.end