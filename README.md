# telprefix

Simple scripts to retrieve and find Indonesia's phone numbers prefixes. Data scraped from https://www.pinhome.id/blog/kode-nomor-prefix/.

🐍 This repository contains a simple library to scrap and find all phone numbers prefixes in Indonesia. The library is available in `telprefix/` directory.

## Example

```py3
from telprefix import TelPrefix

telPrefix = TelPrefix()
scrap = telPrefix.scrap()
find = telPrefix.find("0812")

print(find)
# {'provider': 'Telkomsel', 'jenis': ['Kartu Simpati', 'Halo'], 'keterangan': 'Nomor mempunyai 11 sampai 12 digit angka', 'nomor': '0812'}
```

## Data Source

The list is extracted from Pinhome.id's [blog post](https://www.pinhome.id/blog/kode-nomor-prefix/): https://www.pinhome.id/blog/kode-nomor-prefix/, modified only for cosmetic changes. The actual content is left untouched.

> Note for **Pinhome.id**: If my use case is against your ToS or any terms, please write a message to me so I will make this repository private, so it won't be available for public anymore.
