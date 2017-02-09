from datetime import datetime
from enum import Enum
import uuid


class EventType(Enum):
    ArpDevicePresent = 0
    NmapDevicePresent = 1

class Event(dict):
    uuid = uuid.uuid4()
    created_at = datetime.utcnow().isoformat()

    def __init__(self, type, *args, **kwargs):
        self['type'] = type.name
        self['uuid'] = str(self.uuid)
        self['created_at'] = self.created_at
        self['record'] = dict(*args, **kwargs)
