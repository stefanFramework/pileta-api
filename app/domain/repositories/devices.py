from domain.repositories import BaseRepository
from domain.models.devices import Device

class DeviceRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session)

    def find_all(self):
        return self.session.query(Device).all()