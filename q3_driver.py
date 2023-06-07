import psycopg2
import json


class PersonData:
    def __init__(self):
        self.user = "postgres"
        self.password = "agens"
        self.host = "127.0.0.1"
        self.port = 5432
        self.conn = psycopg2.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        self.cur = self.conn.cursor()
        self.conn.autocommit = True


    def table_create(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS public.user_table (
        user_id numeric(10,0) NOT NULL,
        name character varying(50) COLLATE pg_catalog."default" NOT NULL,
        age numeric(3,0) NOT NULL,
        phone character varying(20) COLLATE pg_catalog."default",
        CONSTRAINT user_table_pkey PRIMARY KEY (user_id)
    )
        """)

    def add_data(self, user_id: int, name: str, age: int, phone: str = None):
        try:
            self.cur.execute("""
            INSERT INTO public.user_table (user_id, name, age, phone) VALUES (%s, %s, %s, %s)
            """, (user_id, name, age, phone))
            self.conn.commit()
        except (Exception, psycopg2.Error) as e:
            self.conn.rollback()
            print(e)


    def remove_data(self, user_id: int):
        self.cur.execute("""
                DELETE FROM public.user_table WHERE user_id = (%s)
                """, (user_id,))
        self.conn.commit()

    def fetch_data(self):
        data = []
        self.cur.execute("""
        SELECT * FROM public.user_table
        """)
        results = self.cur.fetchall()
        for row in results:
            user_data = {
                "user_id": int(row[0]),
                "name": str(row[1]),
                "age": int(row[2]),
            }
            if str(row[3]):
                user_data["phone"] = str(row[3])
            data.append(user_data)

        final_data = {
            "status_code": 200,
            "data": data
        }
        print(json.dumps(final_data, indent=4))

    def close_conn(self):
        self.cur.close()
        self.conn.close()


# p1 = PersonData()
# p1.table_create()
# p1.remove_data(1)
# p1.fetch_data()
# p1.close_conn()