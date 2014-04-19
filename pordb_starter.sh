echo 'Enter Password for user postgres'
su -c 'pg_ctl -D /var/lib/pgsql/data start' postgres &&

sleep 1

echo 'PorDB wird gestartet'
python /home/ego/python/pypordb/pordb.py &
