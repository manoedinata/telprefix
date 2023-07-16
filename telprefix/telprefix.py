import os.path
import json

from telprefix.path import JSON_DATA_PATH
from telprefix.scrap import TelPrefixScrap

class TelPrefix():
    def __init__(self) -> None:
        pass

    def scrap(self):
        scrap = TelPrefixScrap()
        scrap.scrap()

    def find(self, prefix: str):
        with open(JSON_DATA_PATH, "r") as file:
            self.data: dict = json.load(file)

        prefixData = self.data.get(prefix, None)

        prefixData["nomor"] = prefix
        return prefixData
