from database.connection import get_connection

def create_tables():

    connection = get_connection
    cursor = connection.cursor()




    connection.commit()
    connection.close()