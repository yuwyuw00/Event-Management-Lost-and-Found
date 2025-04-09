def register_user_for_event(mongo, user_id, event_id):
    mongo.db.registrations.insert_one({'user_id': user_id, 'event_id': event_id})

def get_user_registrations(mongo, user_id):
    return list(mongo.db.registrations.find({'user_id': user_id}))