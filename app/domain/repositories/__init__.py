from datetime import datetime

class BaseRepository():
    
    def __init__(self, session):
        self.session = session

    def create(self, model):
        self.session.add(model)
        self.session.commit()
        return model
    
    def update(self, model):
        self.session.commit()
        return model
    
    def remove(self, model):
        model.deleted_at = datetime.today()
        self.session.commit()

    # def _execute_query(self, query):
    #     query = query.filter()