import csv
from random import randrange

FIRMEN = []
TAGS = ["firma", "url", "street", "zip",
        "city", "country", "phone", "fax", "ustid"]

FILLER = {
    "beginning": ["Impressum", "Angaben gemäß § 5 TMG"],
    "firma": ["Firma:"],
    "adresse": ["Anschrift"],
    "kontakt": ["Kontakt"],
    "phone": ["Telefon", "Tel.", "Tel.:"],
    "fax": ["Fax", "Telefax", "Fax:"],
    "website": ["Internet", "Webauftritt"],
    "ustid": ["Ust-IdNr.:", "Umsatzsteuer-Identifikationsnummer gemäß §27 a Umsatzsteuergesetz", "Umsatzsteuer-ID"]
}
# writer.writerow({"token": "", "ner": ""})


def randomize_data(f_obj):
    rnd = randrange(0, 10)
    if rnd < 2:
        f_obj["beginning"] = "Impressum"

    if rnd > 1 and rnd < 4:
        f_obj["beginning"] = "Angaben gemäß § 5 TMG"

    rnd = randrange(0, 10)
    if rnd < 2:
        f_obj["firma_pre"] = "Firma"

    rnd = randrange(0, 10)
    if rnd < 2:
        f_obj["adresse_pre"] = "Anschrift"

    rnd = randrange(0, 10)
    if rnd < 2:
        f_obj["kontakt_pre"] = "Kontakt"

    rnd = randrange(0, 10)
    if rnd < 2:
        f_obj["phone_pre"] = "Telefon"

    if rnd > 1 and rnd < 4:
        f_obj["phone_pre"] = "Tel."

    if rnd > 3 and rnd < 6:
        f_obj["phone_pre"] = "Tel.:"

    rnd = randrange(0, 10)
    if rnd < 2:
        f_obj["fax_pre"] = "Fax"

    if rnd > 1 and rnd < 4:
        f_obj["fax_pre"] = "Telefax"

    if rnd > 3 and rnd < 6:
        f_obj["fax_pre"] = "Fax:"

    rnd = randrange(0, 10)
    if rnd < 2:
        f_obj["website_pre"] = "Internet"

    if rnd > 1 and rnd < 4:
        f_obj["website_pre"] = "Webauftritt"

    rnd = randrange(0, 10)
    if rnd < 2:
        f_obj["ustid_pre"] = "Ust-IdNr.:"

    if rnd > 1 and rnd < 4:
        f_obj["ustid_pre"] = "Umsatzsteuer-ID"


def write_to_csv():
    with open('data.txt', mode='w', encoding='utf-8-sig', newline='') as csv_file:
        fieldnames = ['token', 'ner']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=" ")

        # writer.writeheader()

        for firma in FIRMEN:
            f_obj = {
                "beginning": "",
                "firma_pre": "",
                "adresse_pre": "",
                "kontakt_pre": "",
                "phone_pre": "",
                "fax_pre": "",
                "website_pre": "",
                "ustid_pre": "",
                "firma": "",
                "url": "",
                "street": "",
                "zip": "",
                "city": "",
                "country": "",
                "phone": "",
                "fax": "",
                "ustid": ""
            }
            for index, element in enumerate(firma, start=0):
                # NAME
                if element == "not found":
                    continue
                if index == 0:
                    el = element.strip()
                    f_obj["firma"] = el

                # URL
                if index == 1:
                    el = element.strip()
                    f_obj["url"] = el

                # STREET
                if index == 2:
                    el = element.strip()
                    f_obj["street"] = el

                # ZIP
                if index == 3:
                    el = element.strip()
                    f_obj["zip"] = el

                # CITY
                if index == 4:
                    el = element.strip()
                    f_obj["city"] = el

                # LAND
                if index == 5:
                    el = element.strip()
                    f_obj["country"] = el

                # PHONE
                if index == 6:
                    el = element.strip()
                    f_obj["phone"] = el

                # FAX
                if index == 7:
                    el = element.strip()
                    f_obj["fax"] = el

                # USTD-ID
                if index == 8:
                    el = element.strip()
                    f_obj["ustid"] = el

            randomize_data(f_obj)

            # beginning
            if f_obj["beginning"]:
                el = f_obj["beginning"].strip().split()
                for i, e in enumerate(el, start=0):
                    if e.isspace():
                        break
                    if i == 0:
                        writer.writerow(
                            {"token": e.strip(), "ner": "O"})
                    else:
                        writer.writerow(
                            {"token": e.strip(), "ner": "O"})

            # firma
            if f_obj["firma"]:
                if f_obj["firma_pre"]:

                    el = f_obj["firma_pre"] + " " + f_obj["firma"]
                    el = el.strip().split()

                    for i, e in enumerate(el, start=0):
                        if e.isspace():
                            break
                        if i == 0:
                            writer.writerow(
                                {"token": e.strip(), "ner": "O"})
                            writer.writerow(
                                {"token": ":", "ner": "O"})
                        if i == 1:
                            writer.writerow(
                                {"token": e.strip(), "ner": "B-FIR"})
                        else:
                            if e == f_obj["firma_pre"]:
                                continue
                            writer.writerow(
                                {"token": e.strip(), "ner": "I-FIR"})
                else:
                    el = f_obj["firma"].strip().split()
                    for i, e in enumerate(el, start=0):
                        if e.isspace():
                            break
                        if i == 0:
                            writer.writerow(
                                {"token": e.strip(), "ner": "B-FIR"})
                        else:
                            writer.writerow(
                                {"token": e.strip(), "ner": "I-FIR"})

            # strasse
            if f_obj["street"]:
                if f_obj["adresse_pre"]:
                    el = f_obj["adresse_pre"] + " " + f_obj["street"]
                    el = el.strip().split()
                    for i, e in enumerate(el, start=0):
                        if e.isspace():
                            break
                        if i == 0:
                            writer.writerow(
                                {"token": e.strip(), "ner": "O"})
                        if i == 1:
                            writer.writerow(
                                {"token": e.strip(), "ner": "B-STREET"})
                        else:
                            if e == f_obj["adresse_pre"]:
                                continue
                            writer.writerow(
                                {"token": e.strip(), "ner": "I-STREET"})
                else:
                    el = f_obj["street"].strip().split()
                    for i, e in enumerate(el, start=0):
                        if e.isspace():
                            break
                        if i == 0:
                            writer.writerow(
                                {"token": e.strip(), "ner": "B-STREET"})
                        else:
                            writer.writerow(
                                {"token": e.strip(), "ner": "I-STREET"})
            # zip
            if f_obj["zip"]:
                if element.isspace():
                    break
                writer.writerow(
                    {"token": f_obj["zip"].strip(), "ner": "B-ZIP"})
            # city
            if f_obj["city"]:
                el = f_obj["city"].strip().split()
                for i, e in enumerate(el, start=0):
                    if e.isspace():
                        break
                    if i == 0:
                        writer.writerow(
                            {"token": e.strip(), "ner": "B-CITY"})
                    else:
                        writer.writerow(
                            {"token": e.strip(), "ner": "I-CITY"})

            writer.writerow(
                {"token": "Deutschland", "ner": "B-COUNTRY"})

            # kontakt_pre
            if f_obj["kontakt_pre"]:
                writer.writerow({"token": "Kontakt", "ner": "O"})

            # strasse
            if f_obj["url"]:
                if f_obj["website_pre"]:
                    el = f_obj["website_pre"] + " " + f_obj["url"]
                    el = el.strip().split()
                    for i, e in enumerate(el, start=0):
                        if e.isspace():
                            break
                        if i == 0:
                            writer.writerow(
                                {"token": e.strip(), "ner": "O"})
                        if i == 1:
                            writer.writerow(
                                {"token": e.strip(), "ner": "O"})
                        else:
                            if e == f_obj["website_pre"]:
                                continue
                            writer.writerow(
                                {"token": e.strip(), "ner": "O"})
                else:
                    el = f_obj["url"].strip().split()
                    for i, e in enumerate(el, start=0):
                        if e.isspace():
                            break
                        if i == 0:
                            writer.writerow(
                                {"token": e.strip(), "ner": "O"})
                        else:
                            writer.writerow(
                                {"token": e.strip(), "ner": "O"})

            # phone
            if f_obj["phone"]:
                if f_obj["phone_pre"]:
                    el = f_obj["phone_pre"] + " " + f_obj["phone"]
                    el = el.strip().split()
                    for i, e in enumerate(el, start=0):
                        if e.isspace():
                            break
                        if i == 0:
                            writer.writerow(
                                {"token": e.strip(), "ner": "O"})
                        if i == 1:
                            writer.writerow(
                                {"token": e.strip(), "ner": "B-PHONE"})
                        else:
                            if e == f_obj["phone_pre"]:
                                continue
                            writer.writerow(
                                {"token": e.strip(), "ner": "I-PHONE"})
                else:
                    el = f_obj["phone"].strip().split()
                    for i, e in enumerate(el, start=0):
                        if e.isspace():
                            break
                        if i == 0:
                            writer.writerow(
                                {"token": e.strip(), "ner": "B-PHONE"})
                        else:
                            writer.writerow(
                                {"token": e.strip(), "ner": "I-PHONE"})
            # fax
            if f_obj["fax"]:
                if f_obj["fax_pre"]:
                    el = f_obj["fax_pre"] + " " + f_obj["fax"]
                    el = el.strip().split()
                    for i, e in enumerate(el, start=0):
                        if e.isspace():
                            break
                        if i == 0:
                            writer.writerow(
                                {"token": e.strip(), "ner": "O"})
                        if i == 1:
                            writer.writerow(
                                {"token": e.strip(), "ner": "B-FAX"})
                        else:
                            if e == f_obj["fax_pre"]:
                                continue
                            writer.writerow(
                                {"token": e.strip(), "ner": "I-FAX"})
                else:
                    el = f_obj["fax"].strip().split()
                    for i, e in enumerate(el, start=0):
                        if e.isspace():
                            break
                        if i == 0:
                            writer.writerow(
                                {"token": e.strip(), "ner": "B-FAX"})
                        else:
                            writer.writerow(
                                {"token": e.strip(), "ner": "I-FAX"})

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
            if not ''.join(row).strip():
                continue
            FIRMEN.append(row)


# data format: 0 Name, 1 website, 2 Straße. 3 PLZ, 4 Stadt, 5 land, 6 telefonnummer, 7 faxnummer, 8 ustid-nr
def main():
    get_data()
    write_to_csv()


if __name__ == "__main__":
    main()
