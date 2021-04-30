import csv
import json
import os
import random

import fire
from beautifultable import BeautifulTable


def create_if_not_exist(file_name: str):
    """
    Checks for the existence of the provided JSON DB.
    If it does not, this will add {data:[]}.
    :param str file_name: The absolute path to the DB file
    """
    if not os.path.exists(file_name):
        with open(file_name, "w") as db_file:
            db = {"data": []}
            json.dump(db, db_file)
        print("Succesfully created {} in the directory.".format(name))


def display(file_name: str):
    table = BeautifulTable()
    with open(file_name) as jsondoc:
        data = json.load(jsondoc)
        real_data = data["data"]
        header = list(data["data"][0].keys())
        for all_data in real_data:
            table.rows.append(list(all_data.values()))
        table.columns.header = header
        print(table)


def delete(file_name: str):
    if os.path.exists(file_name):
        x = input("Do you want to remove the json file..(y/n)")
        if x in ["y", "Y"]:
            os.remove(name)
        else:
            print("Action terminated")
    else:
        print("The file does not exist")


def convert(csv_file, json_db):
    print("Reading data from {}".format(csv_file))
    arr = []
    with open(csv_file) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for csvRow in csvReader:
            csvRow["id"] = random.randint(1000000000, 9999999999)
            arr.append(csvRow)
    print("Writing data into {}".format(json_db))
    x = {}
    x["data"] = arr
    with open(json_db, "w") as json_file:
        json.dump(x, json_file)
    print("Conversion successful")

def convert_db_to_csv(filename :str,targetcsv="converted.csv"):
    with open(filename,"r") as db:
        json_loaded=json.load(db)['data']
        csv_file=open(targetcsv,"a")
        csv_writer=csv.writer(csv_file)
        header=json_loaded[0].keys()
        csv_writer.writerow(header)
        for each in json_loaded:
            csv_writer.writerow(each.values())
        csv_file.close()    




def main():
    fire.Fire(
        {
            "create": create_if_not_exist,
            "display": display,
            "delete": delete,
            "convert": convert,
            "converttocsv": convert_db_to_csv
        }
    )


if __name__ == "__main__":
    main()
