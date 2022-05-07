import base64
import calendar
import json
import time
import requests


class xitroo():
    def __init__(self, email):
        self.email = email

    def get_bodytext(self):
        ts = calendar.timegm(time.gmtime())
        i = 1
        idsite = requests.get("https://api.xitroo.com/v1/mails?locale=de&mailAddress=" + self.email +
                              "&mailsPerPage=25&minTimestamp=0.0&maxTimestamp=" + str(ts + 500),
                              headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; "
                                                     "Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                                     "Chrome/92.0.4515.159 Safari/537.36"}).text
        idjson = json.loads(idsite)
        while True:
            try:
                mails = idjson["mails"][0]
                id = mails['_id']
                mega = requests.get("https://api.xitroo.com/v1/mail?locale=de&id=" + id,
                                    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; "
                                                           "Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                                           "Chrome/92.0.4515.159 Safari/537.36"}).text
                megajson = json.loads(mega)
                base64code = megajson['bodyText']
                if base64code.count('==') == 0:
                    base64code += '=='
                bodytext = base64.b64decode(base64code)
                break
            except:
                noemail = idjson['type']
                print(noemail)
                if i == 5:
                    return
                i += 1
                time.sleep(5)
        return bodytext