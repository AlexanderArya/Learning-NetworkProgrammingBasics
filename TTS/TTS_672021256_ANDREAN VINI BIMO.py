from ncclient import manager
from pprint import pprint
import xmltodict
from datetime import datetime
import sys
from socket import close


pilihan = int(input("Masukan pilihan anda: "))

if pilihan == 1:
  router = {"ip": "sandbox-iosxe-recomm-1.cisco.com",
          "port": 830,
          "user": "developer",
          "pass": "lastorangerestoreball8876"}

  print(router)

elif pilihan == 2:
  router = {"host": "sandbox-iosxe-recomm-1.cisco.com",
          "potr": 830,
          "username": "developer",
          "pass": "lastorangerestoreball8876"}

  print(router)

elif pilihan == 3:
  router = {"ip": "sandbox-iosxe-recomm-1.cisco.com",
          "port": 830,
          "user": "developer",
          "pass": "lastorangerestoreball8876"}

  netconf_filter = """
  <filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
        <name>GigabitEthernet1</name>
      </interface>
    </interfaces>
  </filter>
  """

  m = manager.connect(host=router["ip"],
                    port=router["port"],
                    username=router["user"],
                    password=router["pass"],
                    hostkey_verify=False)

  interface_netconf = m.get_config("running", netconf_filter)
  interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]
  a = interface_python["interfaces"]["interface"]["name"]["#text"]

  log_file = "TTS.log"

  log_time = str(datetime.now())

  # Pengerjaan di directory sendiri
  # with open(log_file,"a") as f:
  #   f.writelines("Entry logged at:",log_time ,"by", a)

  # Pengerjaan di Google Colab
  print("Entry logged at:",log_time ,"by", a)

else :
  print("_____________________________________")
  print("    TTS Pemrograman Jaringan 2023    ")
  print("_____________________________________")
  print("Nama : Andrean Vini Bimo Arya Wibowo ")
  print("NIM : 672021256 ")
  
  m.
  sys.exit(0)

