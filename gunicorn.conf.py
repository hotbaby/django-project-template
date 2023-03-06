# encoding: utf8

import os
import socket

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.environ.get('LOG_DIR', '.')
HOST_NAME = socket.gethostname()

# Core
wsgi_app = "settings.wsgi:application"
reload = False

# Server
bind = '0.0.0.0:8000'
backlog = 2048

# worker processes
workers = 16
threads = 64
worker_class = 'gevent'
worker_connections = 4096

# Debug
spew = False
reload = False

timeout = 0    # Workers silent for more than this many seconds are killed and restarted.
graceful_timeout = 300  # Timeout for graceful workers restart.
keepalive = 75


# Logging
logger_class = "apps.utils.logging_.CustomGunicornLogger"
# access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
access_log_format = '{"remote_addr": "%(h)s", "remote_user": "%({X-Username}i)s", "time_local": "%(t)s", "host": "%({Host}i)s", "request_method": "%(m)s", "request_path": "%(U)s", "request_querystring": "%(q)s", "protocol": "%(H)s", "status": "%(s)s", "request_time": "%(L)s", "response_length": "%(B)s", "http_referer": "%(f)s", "http_user_agent": "%(a)s"}'
logconfig_dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {},
    "loggers": {},
    "handlers": {},
    "formatters": {}
}


# Server hooks
def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)


def pre_fork(server, worker):
    pass


def pre_exec(server):
    server.log.info("Forked child, re-executing.")


def when_ready(server):
    server.log.info("Server is ready. Spawning workers")


def worker_int(worker):
    worker.log.info("worker received INT or QUIT signal")

    ## get traceback info
    import threading, sys, traceback
    id2name = {th.ident: th.name for th in threading.enumerate()}
    code = []
    for threadId, stack in sys._current_frames().items():
        code.append("\n# Thread: %s(%d)" % (id2name.get(threadId, ""), threadId))
        for filename, lineno, name, line in traceback.extract_stack(stack):
            code.append('File: "%s", line %d, in %s' % (filename, lineno, name))
            if line:
                code.append("  %s" % (line.strip()))
    worker.log.debug("\n".join(code))


def worker_abort(worker):
    worker.log.info("worker received SIGABRT signal")