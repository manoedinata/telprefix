import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet
import json

from telprefix.path import JSON_DATA_PATH

def getHTMLText(result: ResultSet | None) -> str:
    if result is not None:
        result = result.text.strip()
    return result

# URL Artikel
# Sumber: https://www.pinhome.id
URL = "https://www.pinhome.id/blog/kode-nomor-prefix/"

class TelPrefixScrap():
    def __init__(self) -> None:
        self.data = {}
        self.URL = URL

    def request(self) -> BeautifulSoup:
        req = requests.get(URL)
        reqParse = BeautifulSoup(req.text, "html.parser")

        return reqParse

    def parse(self):
        reqParse = self.request()
        tables = reqParse.find_all("table")

        currentTable = 0
        for index, table in enumerate(tables):
            tableRow = table.find_all("tr")
            for row in tableRow[1:]:
                # Extract table rows data
                prefix = row.find_all("td")[0]

                tableRowJudul = tableRow[0]
                if( len(tableRowJudul.find_all("td")) == 4 ):
                    jenis = row.find_all("td")[1]
                    keterangan = row.find_all("td")[2]
                    provider = row.find_all("td")[3]
                else:
                    jenis = None
                    keterangan = row.find_all("td")[1]
                    provider = row.find_all("td")[2]

                # Get & strip text
                prefix = getHTMLText(prefix)
                provider = getHTMLText(provider)
                jenis = getHTMLText(jenis)
                keterangan = getHTMLText(keterangan)

                # Tidy up
                if provider == "":
                    if index == currentTable:
                        provider = self.data[list(self.data.keys())[-1]]["provider"]
                    else:
                        provider = None

                if jenis is not None:
                    if "atau" in jenis:
                        jenis = jenis.split(" atau ")
                    elif "dan" in jenis:
                        jenis = jenis.split(" dan ")

                self.data[prefix] = {
                    "provider": provider,
                    "jenis": jenis,
                    "keterangan": keterangan
                } 

            currentTable += 1

        return self.data

    def save(self):
        with open(JSON_DATA_PATH, "w") as file:
            json.dump(self.data, file, indent=4)

    def scrap(self):
        parse = self.parse()
        save = self.save()

        return parse
