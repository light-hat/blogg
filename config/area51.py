[program:area51]
command=/home/l1ghth4t/venv/bin/gunicorn config.wsgi:application -c /home/l1ghth4t/area51/config/gunicorn.conf.py
directory=/home/l1ghth4t/area51/
user = l1ghth4t
autorestart=true
redirect_stderr=true
stdout_logfile = /home/l1ghth4t/area51/logs/debug.log