import requests

def get_inofs():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.63"}
    info = requests.get("https://outputter.io/full-identity/germany/", headers=headers).text
    infonames = ["Name", "Address", "City", "Postcode", "Phone", "BIC", "IBAN"]
    infos = []
    for i in infonames:
        rawinfo = info.split(f'row">{i}')[1].split('"top">')[1].split('<')[0]
        infos.append(rawinfo)

    return {
        "Name": infos[0],
        "Address": infos[1],
        "City": infos[2],
        "Postcode": infos[3],
        "Phone": infos[4],
        "BIC": infos[5],
        "IBAN": infos[6]
    }