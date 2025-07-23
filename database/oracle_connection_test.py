import oracledb
username = "DEV_USER"
password = "DUGmf@2021#23"
connection_string = "(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1521)(host=adb.sa-saopaulo-1.oraclecloud.com))(connect_data=(service_name=g0c4e0695fbcd67_ocdatabase001_high.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))"

connection = oracledb.connect(user=username, password=password, dsn=connection_string)