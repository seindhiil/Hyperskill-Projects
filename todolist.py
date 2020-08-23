# Write your code here
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String,
                          default='default_value')
    deadline = Column(Date,
                        default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)

weekdays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
today = datetime.today()
monday_date = ""
tuesday_date = ""
wednesday_date = ""
thursday_date = ""
friday_date = ""
saturday_date = ""
sunday_date = ""
result = ""
while True:
    print()
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Missed tasks")
    print("5) Add task")
    print("6) Delete task")
    print("0) Exit")
    choice = input()
    if choice == "1":
        rows = session.query(Table).filter(Table.deadline == today.date()).all()
        print("Today", today.day, today.strftime('%b'))
        if len(rows) == 0:
            print("Nothing to do!")
        else:
            num = 1
            for row in rows:
                print(str(num) + ".", row)

    if choice == "2":

        if today.weekday() == 6:
            sunday_date = today
            monday_date = today + timedelta(days=1)
            tuesday_date = today + timedelta(days=2)
            wednesday_date = today + timedelta(days=3)
            thursday_date = today + timedelta(days=4)
            friday_date = today + timedelta(days=5)
            saturday_date = today + timedelta(days=6)
        if today.weekday() == 0:
            monday_date = today
            tuesday_date = today + timedelta(days=1)
            wednesday_date = today + timedelta(days=2)
            thursday_date = today + timedelta(days=3)
            friday_date = today + timedelta(days=4)
            saturday_date = today + timedelta(days=5)
            sunday_date = today - timedelta(days=1)
        if today.weekday() == 1:
            tuesday_date = today
            wednesday_date = today + timedelta(days=1)
            thursday_date = today + timedelta(days=2)
            friday_date = today + timedelta(days=3)
            saturday_date = today + timedelta(days=4)
            sunday_date = today + timedelta(days=5)
            monday_date = today + timedelta(days=6)
        if today.weekday() == 2:
            wednesday_date = today
            thursday_date = today + timedelta(days=1)
            friday_date = today + timedelta(days=2)
            saturday_date = today + timedelta(days=3)
            sunday_date = today + timedelta(days=4)
            monday_date = today + timedelta(days=5)
            tuesday_date = today + timedelta(days=6)
        if today.weekday() == 3:
            thursday_date = today
            friday_date = today + timedelta(days=1)
            saturday_date = today + timedelta(days=2)
            sunday_date = today + timedelta(days=3)
            monday_date = today + timedelta(days=4)
            tuesday_date = today + timedelta(days=5)
            wednesday_date = today + timedelta(days=6)
        if today.weekday() == 4:
            friday_date = today
            saturday_date = today + timedelta(days=1)
            sunday_date = today + timedelta(days=2)
            monday_date = today + timedelta(days=3)
            tuesday_date = today + timedelta(days=4)
            wednesday_date = today + timedelta(days=5)
            thursday_date = today + timedelta(days=6)
        if today.weekday() == 5:
            saturday_date = today
            sunday_date = today + timedelta(days=1)
            monday_date = today + timedelta(days=2)
            tuesday_date = today + timedelta(days=3)
            wednesday_date = today + timedelta(days=4)
            thursday_date = today + timedelta(days=5)
            friday_date = today + timedelta(days=6)

        """
        print(sunday_date)
        print(monday_date)
        print(tuesday_date)
        print(wednesday_date)
        print(thursday_date)
        print(friday_date)
        print(saturday_date)
        """

        Sunday = session.query(Table).filter(Table.deadline == sunday_date.date()).all()
        Monday = session.query(Table).filter(Table.deadline == monday_date.date()).all()
        Tuesday = session.query(Table).filter(Table.deadline == tuesday_date.date()).all()
        Wednesday = session.query(Table).filter(Table.deadline == wednesday_date.date()).all()
        Thursday = session.query(Table).filter(Table.deadline == thursday_date.date()).all()
        Friday = session.query(Table).filter(Table.deadline == friday_date.date()).all()
        Saturday = session.query(Table).filter(Table.deadline == saturday_date.date()).all()

        print()
        print("Sunday", sunday_date.day, sunday_date.strftime('%b'))
        if len(Sunday) == 0:
            print("Nothing to do!")
        else:
            num = 1
            for row in Sunday:
                print(str(num) + ".", row)
        print()
        print("Monday", monday_date.day, monday_date.strftime('%b'))
        if len(Monday) == 0:
            print("Nothing to do!")
        else:
            num = 1
            for row in Monday:
                print(str(num) + ".", row)
        print()
        print("Tuesday", tuesday_date.day, tuesday_date.strftime('%b'))
        if len(Tuesday) == 0:
            print("Nothing to do!")
        else:
            num = 1
            for row in Tuesday:
                print(str(num) + ".", row)
        print()
        print("Wednesday", wednesday_date.day, wednesday_date.strftime('%b'))
        if len(Wednesday) == 0:
            print("Nothing to do!")
        else:
            num = 1
            for row in Wednesday:
                print(str(num) + ".", row)

        print()
        print("Thursday", thursday_date.day, thursday_date.strftime('%b'))
        if len(Thursday) == 0:
            print("Nothing to do!")
        else:
            num = 1
            for row in Thursday:
                print(str(num) + ".", row)
        print()
        print("Friday", friday_date.day, friday_date.strftime('%b'))
        if len(Friday) == 0:
            print("Nothing to do!")
        else:
            num = 1
            for row in Friday:
                print(str(num) + ".", row)
        print()
        print("Saturday", saturday_date.day, saturday_date.strftime('%b'))
        if len(Saturday) == 0:
            print("Nothing to do!")
        else:
            num = 1
            for row in Saturday:
                print(str(num) + ".", row)
    if choice == "3":
        print("All tasks:")
        num_2 = 1
        get_all = session.query(Table.task, Table.deadline).order_by(Table.deadline).all()

        for row in get_all:
            # print(weekdays[row[1].weekday()], row[1].day, row[1].strftime('%b'))
            # print(str(num_2) + ".", str(row[0]))
            print(str(num_2) + ".", str(row[0]) + ".", row[1].day, row[1].strftime('%b'))
    if choice == "4":
        get_all_2 = session.query(Table.task, Table.deadline).order_by(Table.deadline).all()
        num_3 = 1
        check_num = 0
        for row in get_all_2:
            if int(row[1].day) < int(today.day):
                print(str(num_3) + ".", str(row[0]) + ".", row[1].day, row[1].strftime('%b'))
                check_num += 1
        if check_num == 0:
            print("Nothing is missed!")
    if choice == "5":
        print("Enter task")
        added_task = input()
        print("Enter deadline")
        date = input()
        date = datetime.strptime(date, "%Y-%m-%d")

        new_row = Table(task=added_task, deadline=date)
        session.add(new_row)
        session.commit()
    if choice == "6":
        get_all_3 = session.query(Table.task, Table.deadline).order_by(Table.deadline).all()
        num_4 = 1
        for row in get_all_3:
            print(str(num_4) + ".", str(row[0]) + ".", row[1].day, row[1].strftime('%b'))
            num_4 += 1
        delete_num = int(input())
        rows = session.query(Table).order_by(Table.deadline).all()
        delete_row = rows[delete_num-1]
        session.delete(delete_row)
        session.commit()
    if choice == "0":
        print("Bye!")
        exit()
