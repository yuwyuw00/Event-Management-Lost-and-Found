def get_user_by_username(mongo, username):
    return mongo.db.users.find_one({'username': username})

def create_user(mongo, user_data):
    mongo.db.users.insert_one(user_data)