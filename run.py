from nest import Nest
from database import Database
from settings import settings

def main():

    nest_username = settings['nest_username']
    nest_password = settings['nest_password']
    db_username = settings['db_username']
    db_password = settings['db_password']
    db_name = settings['db_name']
    db_host = settings['db_host']
    db_port = settings['db_port']
    db_table = settings['db_table']

    n = Nest(nest_username, nest_password)
    n.login()
    n.get_status()

    d = Database(db_username, db_password, db_name, db_host, db_port, db_table)
    d.persist(n.show_status())

if __name__=="__main__":
   main()
