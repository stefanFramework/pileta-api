from domain.repositories import BaseRepository

class DeviceRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session)