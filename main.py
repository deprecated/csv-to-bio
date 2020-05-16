import csv

FIRMEN = []


def write_to_csv():
    with open('data_new.csv', mode='w', encoding='utf-8-sig', newline='') as csv_file:
        fieldnames = ['token', 'ner']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=" ")

        writer.writeheader()

        for firma in FIRMEN:
            for index, element in enumerate(firma, start=0):
                # NAME
                if element == "not found":
                    continue
                if index == 0:
                    el = element.strip().split(" ")

                    for i, e in enumerate(el, start=0):
                        if i == 0:
                            writer.writerow(
                                {"token": e, "ner": "B-PER"})
                        else:
                            writer.writerow(
                                {"token": e, "ner": "I-PER"})

                # URL
                if index == 1:
                    writer.writerow(
                        {"token": element, "ner": "B-URL"})

                # STREET
                if index == 2:
                    el = element.strip().split(" ")
                    for i, e in enumerate(el, start=0):
                        if i == 0:
                            writer.writerow(
                                {"token": e, "ner": "B-STREET"})
                        else:
                            writer.writerow(
                                {"token": e, "ner": "I-STREET"})

                # ZIP
                if index == 3:
                    writer.writerow(
                        {"token": element, "ner": "B-ZIP"})

                # CITY
                if index == 4:
                    el = element.strip().split(" ")
                    for i, e in enumerate(el, start=0):
                        if i == 0:
                            writer.writerow(
                                {"token": e, "ner": "B-CITY"})
                        else:
                            writer.writerow(
                                {"token": e, "ner": "I-CITY"})

                # LAND
                if index == 5:
                    el = element.strip().split(" ")
                    for i, e in enumerate(el, start=0):
                        if i == 0:
                            writer.writerow(
                                {"token": e, "ner": "B-COUNTRY"})
                        else:
                            writer.writerow(
                                {"token": e, "ner": "I-COUNTRY"})

                # PHONE
                if index == 6:
                    el = element.strip().split(" ")
                    for i, e in enumerate(el, start=0):
                        if i == 0:
                            writer.writerow(
                                {"token": e, "ner": "B-PHONE"})
                        else:
                            writer.writerow(
                                {"token": e, "ner": "I-PHONE"})

                # FAX
                if index == 7:
                    el = element.strip().split(" ")
                    for i, e in enumerate(el, start=0):
                        if i == 0:
                            writer.writerow(
                                {"token": e, "ner": "B-FAX"})
                        else:
                            writer.writerow(
                                {"token": e, "ner": "I-FAX"})

                # USTD-ID
                if index == 8:
                    el = element.strip().split(" ")
                    for i, e in enumerate(el, start=0):
                        if i == 0:
                            writer.writerow(
                                {"token": e, "ner": "B-USTID"})
                        else:
                            writer.writerow(
                                {"token": e, "ner": "I-USTID"})

            writer.writerow({"token": "", "ner": ""})


def get_data():
    with open('data.csv', newline='', encoding="utf-8-sig") as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            FIRMEN.append(row)


# data format: 0 Name, 1 website, 2 Straße. 3 PLZ, 4 Stadt, 5 land, 6 telefonnummer, 7 faxnummer, 8 ustid-nr
def main():
    get_data()
    write_to_csv()


main()
