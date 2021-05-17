import psycopg2

HOSTNAME = '127.0.0.1'
USERNAME = 'postgres'
PASSWORD = 'post'
DATABASE = 'menu'

def run_exec(query):
    connection = psycopg2.connect(host=HOSTNAME , user=USERNAME , password=PASSWORD, dbname=DATABASE )
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    try:
        result = cursor.fetchall()
    except:
        result =None
    connection.close()
    return result

class  MenuItem():
    items = []
    def __init__(self, item, price):
        self.item = item
        self.price= price


    def save(self):
            for id, item, price in MenuItem.all():
                   if self.item == item:
                         return None
            query = f"INSERT INTO menu_item (item,price) VALUES  ('{self.item}', {price});"
            return run_exec(query)

    def delete(self):
        for id, item, price in MenuItem.all():
            if self.item == item:
                query = f"DELETE FROM menu_item WHERE  name = '{self.item}'; "
                return run_exec(query)
            print("{item} is not in the menu".format(self.item))
            return None

    @staticmethod
    def all():
        query = f"SELECT * FROM menu_item;"
        return run_exec(query)


@staticmethod
def get_by_name(str):
        query = f"SELECT * FROM menu_item WHERE name = '{str}';"
        return run_exec(query)

def main():
    item = MenuItem('Imperial Burger', 35)
    item.save()
    print("After adding Imperial Burger:\n", MenuItem.all())
    item.delete()
    print("After deleting Imperial Burger:\n", MenuItem.all())
    item.update('Veggie Burger', 37)
    print("After updating Veggy Burger:\n", MenuItem.all())
    print(MenuItem.get_by_name('Beef Stew'))
    print(MenuItem.get_by_name('Ratatouille'))
