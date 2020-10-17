source /root/venv_mock_yiban/bin/activate
eval $(ps -ef | grep "/root/MockYiban/conf/uwsgi/mock-yiban.ini" | awk '{print "kill -9 "$2}')
nohup uwsgi -i /root/MockYiban/conf/uwsgi/mock-yiban.ini >/dev/null 2>&1 &