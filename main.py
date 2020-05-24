import csv

FIRMEN = []


def write_to_csv():
    with open('data.txt', mode='w', encoding='utf-8-sig', newline='') as csv_file:
        fieldnames = ['token', 'ner']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=" ")

        # writer.writeheader()

        for firma in FIRMEN:
            for index, element in enumerate(firma, start=0):
                # NAME
                if element == "not found":
                    continue
                if index == 0:
                    el = element.strip().split()

                    for i, e in enumerate(el, start=0):
                        if e.isspace():
                            break
                        if i == 0:
                            writer.writerow(
                                {"token": e.strip(), "ner": "B-FIR"})
                        else:
                            writer.writerow(
                                {"token": e.strip(), "ner": "I-FIR"})

                # URL
                if index == 1:
                    if element.isspace():
                        break
                    writer.writerow(
                        {"token": element.strip(), "ner": "O"})

                # STREET
                if index == 2:
                    el = element.strip().split()
                    for i, e in enumerate(el, start=0):
                        if e.isspace():
                            break
                        if i == 0:
                            writer.writerow(
                                {"token": e.strip(), "ner": "B-STREET"})
                        else:
                            writer.writerow(
                                {"token": e.strip(), "ner": "I-STREET"})

                # ZIP
                if index == 3:
                    if element.isspace():
                        break
                    writer.writerow(
                        {"token": element.strip(), "ner": "B-ZIP"})

                # CITY
                if index == 4:
                    el = element.strip().split()
                    for i, e in enumerate(el, start=0):
                        if e.isspace():
                            break
                        if i == 0:
                            writer.writerow(
                                {"token": e.strip(), "ner": "B-CITY"})
                        else:
                            writer.writerow(
                                {"token": e.strip(), "ner": "I-CITY"})

                # LAND
                if index == 5:
                    el = element.strip().split()
                    for i, e in enumerate(el, start=0):
                        if e.isspace():
                            break
                        if i == 0:
                            writer.writerow(
                                {"token": e.strip(), "ner": "B-COUNTRY"})
                        else:
                            writer.writerow(
                                {"token": e.strip(), "ner": "I-COUNTRY"})

                # PHONE
                if index == 6:
                    el = element.strip().split()
                    for i, e in enumerate(el, start=0):
                        if e.isspace():
                            break
                        if i == 0:
                            writer.writerow(
                                {"token": e.strip(), "ner": "O"})
                        else:
                            writer.writerow(
                                {"token": e.strip(), "ner": "O"})

                # FAX
                if index == 7:
                    el = element.strip().split()
                    for i, e in enumerate(el, start=0):
                        if e.isspace():
                            break
                        if i == 0:
                            writer.writerow(
                                {"token": e.strip(), "ner": "O"})
                        else:
                            writer.writerow(
                                {"token": e.strip(), "ner": "O"})

                # USTD-ID
                if index == 8:
                    el = element.strip().split()
                    for i, e in enumerate(el, start=0):
                        if e.isspace():
                            break
                        if i == 0:
                            writer.writerow(
                                {"token": e.strip(), "ner": "O"})
                        else:
                            writer.writerow(
                                {"token": e.strip(), "ner": "O"})

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


if __name__ == "__main__":
    main()
