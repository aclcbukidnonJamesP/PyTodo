import csv
import os
from models.users import User



users_csv_file = 'data/users.csv'
user_csv_header = ["id", "last_name", "first_name", "password", "email"]

def initialize_users_csv():
    if os.path.exists(users_csv_file):
        return

    with open(users_csv_file, 'w', newline="") as file:
        csv_writer = csv.DictWriter(file, user_csv_header)
        csv_writer.writeheader()


def create_user(user : User):

    with open(users_csv_file, 'a', newline="") as file:
        csv_writer = csv.DictWriter(file, user_csv_header)
        csv_writer.writerow(user.__dict__)


def get_all_users() -> list[User]:
    with open(users_csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        users = []
        for row in csv_reader:
            user = User(
                id=row["id"],
                last_name=row["last_name"],
                first_name=row["first_name"],
                password=row["password"],
                email=row["email"]
            )
            users.append(user)
        return users


def get_user_by_id(user_id) -> User | None:
    with open(users_csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row["id"] == user_id:
                user = User(
                    id=row["id"],
                    last_name=row["last_name"],
                    first_name=row["first_name"],
                    password=row["password"],
                    email=row["email"]
                )
                return user
        return None


def get_user_by_email(email: str) -> User | None:
    with open(users_csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row["email"] == email:
                user = User(
                    id=row["id"],
                    last_name=row["last_name"],
                    first_name=row["first_name"],
                    password=row["password"],
                    email=row["email"]
                )
                return user
        return None


def update_user_by_id(user_id ,user : User) :
    with open(users_csv_file, 'r') as file, \
         open(users_csv_file, 'w', newline="") as write_file:

        csv_reader = csv.DictReader(file)
        csv_writer = csv.DictWriter(write_file, user_csv_header)

        csv_writer.writeheader()

        for row in csv_reader:
            if row["id"] == user_id:
                row["last_name"] = user.last_name
                row["first_name"] = user.first_name
                row["password"] = user.password
                row["email"] = user.email

            csv_writer.writerow(row)




def update_user_by_email(email: str ,user : User):

    with open(users_csv_file, 'r') as file, \
            open(users_csv_file, 'w', newline="") as write_file:

        csv_reader = csv.DictReader(file)
        csv_writer = csv.DictWriter(write_file, user_csv_header)

        csv_writer.writeheader()

        for row in csv_reader:
            if row["email"] == email:
                row["last_name"] = user.last_name
                row["first_name"] = user.first_name
                row["password"] = user.password
                row["email"] = user.email
            csv_writer.writerow(row)




def delete_user_by_id(user_id: str):

    with open(users_csv_file, 'r') as file, \
            open(users_csv_file, 'w', newline="") as write_file:

        csv_reader = csv.DictReader(file)
        csv_writer = csv.DictWriter(write_file, user_csv_header)

        csv_writer.writeheader()

        for row in csv_reader:
            if row["id"] != user_id:
                csv_writer.writerow(row)



def delete_user_by_email(email: str):

    with open(users_csv_file, 'r') as file, \
        open(users_csv_file, 'w', newline="") as write_file:

        csv_reader = csv.DictReader(file)
        csv_writer = csv.DictWriter(write_file, user_csv_header)

        csv_writer.writeheader()

        for row in csv_reader:
            if row["email"] != email:
                csv_writer.writerow(row)
