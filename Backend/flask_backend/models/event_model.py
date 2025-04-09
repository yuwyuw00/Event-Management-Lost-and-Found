def create_event(mongo, event_data):
    mongo.db.events.insert_one(event_data)

def get_all_events(mongo):
    return list(mongo.db.events.find())

def get_event_by_id(mongo, event_id):
    return mongo.db.events.find_one({'_id': event_id})