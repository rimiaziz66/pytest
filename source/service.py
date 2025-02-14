
db_data= {1:'A',2:'B', 3:'C' }


def get_data_from_db(user_id):
     return db_data.get(user_id)