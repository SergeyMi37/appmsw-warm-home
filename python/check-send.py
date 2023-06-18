# Program for regularly reading the temperature sensor and sending a message to the telebot
#pip install requests
#pip install --upgrade pip
import requests
import threading
import datetime
import yaml
import socket
import sys

_path_file_conf = sys.argv[1]
with open(_path_file_conf) as _fi:
    _param = yaml.safe_load(_fi)
print(_param["token"])
_time=int(_param["timeout"])
_time_dflt=_time


def send_telegram(text: str):
    _TOKEN=_param["token"]
    _url = "https://api.telegram.org/bot"
    _channel_id = _param["chat_id"]
    _method = _url + _TOKEN + "/sendMessage"

    r = requests.post(_method, data={
         "chat_id": _channel_id,
         "text": text
          })

    if r.status_code != 200:
        #raise Exception("post_text error")
        print("Error",r.status_code)
    else:
        print("Sent successfully")


def read_tempera():
    tfile=open(_param["dirbus1w"])
    ttext=tfile.read()
    tfile.close()
    te=ttext.split("\n")[1].split(" ")[9]
    return float(te[2:])/1000


def check_tempera():
    global _time,_time_dflt
    threading.Timer(_time, check_tempera).start()  # Restart after 3600 seconds - every hour
    _temp=read_tempera()
    _msg="👉 temperature "+str(_temp)
    _dt=str(datetime.datetime.today().strftime("%Y-%m-%d_%H.%M"))

    #print(_temp)
    if _temp < _param["min_threshold"]:
        _msg=" 🚨🚨🚨🚨🚨 Attention limit lower temperature threshold "+str(_temp)
        send_telegram(_msg)
        _time=60
    elif _temp > _param["max_threshold"]:
        _msg=" 🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨 Attention upper temperature limit "+str(_temp)
        send_telegram(_msg)
        _time=60
    elif _param["dubug_print"]:
        send_telegram(_msg)
        _time=_time_dflt

    print(_dt+_msg)
    _ret=save_db(_dt,_msg,_temp)
    print(_ret)


def save_db(_dt,_msg,_temp):
    _username=_param["username"]
    _password=_param["password"]
    _base_url=_param["base_url"]+_dt+_msg
    #print(_param)

    headers = {'Accept': 'application/json;odata=verbose'}
    responce = requests.get(_base_url,verify=False,auth=(_username,_password),headers=headers)

    respon_list=responce.json()
    #print(respon_list)
    return respon_list


if __name__ == '__main__':
    msg=" ✅ Start monitoring the temperature sensor. Periodicity: "+str(_param["timeout"])+", alert thresholds: "+str(_param["min_threshold"])+" "+str(_param["max_threshold"])
    send_telegram(msg+ " "+socket.gethostname()+" "+str(socket.gethostbyname(socket.gethostname())))
    send_telegram("Current temperature "+str(read_tempera()))
    _ret=save_db("",msg,"")
    print(_ret,msg)
    check_tempera()
