import psycopg2
import pprint
class DB:
    def __init__(self):
        self.new_words_queue = []
    def execute_command(self, *args, **kwargs):
        # connect to db
        self.con = psycopg2.connect(
            host='localhost',
            database='slownik',
            user='postgres',
            password='manu123',
            port=5432,
        )
        # cursor
        cur = self.con.cursor()
        #execute
        cur.execute(*args, **kwargs)
        self.con.commit()
        rows = cur.fetchall()
        #for row in rows:
        #    print(row)
        self.con.commit()
        #close cursor
        cur.close()
        #close connection
        self.con.close()
        return rows

    def get_es_words(self):
        self.es_words = self.execute_command("SELECT slowa.en FROM slowa;")
        return self.es_words

    def get_pl_words(self):
        self.pl_words = self.execute_command("SELECT slowa.pl FROM slowa;")
        return self.pl_words

    def add_words_to_bufor(self, pl, es):
        command = f"INSERT INTO slowa (pl, en) VALUES ('{pl}','{es}');"
        self.listToString = ''.join([str(elem) for elem in command])
        print(self.listToString)
        return self.listToString

    def clear_bufor(self):
        self.new_words_queue = []

    def get_nr_of_rand_records(self, nr):
        rand_records = self.execute_command(f"SELECT slowa.pl,slowa.en FROM slowa ORDER BY RANDOM() LIMIT {nr};")
        return rand_records

    def add_words_from_bufor(self):
        self.con = psycopg2.connect(
            host='localhost',
            database='slownik',
            user='postgres',
            password='manu123',
            port=5432,
        )
        # cursor
        cur = self.con.cursor()
        # execute
        cur.execute(self.listToString)
        self.con.commit()
        # close cursor
        cur.close()
        # close connection
        self.con.close()
        self.clear_bufor()
        return True

a=DB()
#print(a.get_es_words())
#print(a.get_pl_words())
#print(a.add_new_words('buty','los zapatos'))
#print(a.get_es_words())
#print(a.get_pl_words())
