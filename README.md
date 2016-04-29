# uWSGI WebSocket Bug Demo

 > Demo application for the uWSGI websocket bug - https://github.com/unbit/uwsgi/issues/1241

## Setup
```shell
git clone https://github.com/michaelimfeld/uwsgi-ws-bug-demo.git
cd uwsgi-ws-bug-demo
./start.sh
```

After executing the `./start.sh` script, navigate your browser to localhost:8080 and click on `Start WebSocket Test`.

Take a look back at your console where you started the demo app and you'll see that not all messages have been received by the backend. If you refresh the page, the missing message will finally arrive.

```shell
λ localhost uwsgi-ws-bug-demo → ./start.sh
*** Starting uWSGI 2.0.12 (64bit) on [Fri Apr 29 09:19:42 2016] ***
compiled with version: 5.2.1 20151010 on 03 February 2016 15:38:31
(...)
spawned uWSGI http 1 (pid: 14819)
[pid: 14818|app: 0|req: 1/1] 127.0.0.1 () {40 vars in 716 bytes} [Fri Apr 29 09:19:47 2016] GET / => generated 683 bytes in 12 msecs (HTTP/1.1 200) 1 headers in 59 bytes (2 switches on core 25)
2016-04-29 09:19:50.681814: Received ws message: 'Hello World - 1'
2016-04-29 09:19:50.721504: Received ws message: 'Hello World - 2'
```

After the page refresh the log will look like this:

```shell
[pid: 15451|app: 0|req: 3/2] 127.0.0.1 () {40 vars in 716 bytes} [Fri Apr 29 09:31:15 2016] GET / => generated 830 bytes in 5 msecs (HTTP/1.1 200) 1 headers in 59 bytes (2 switches on core 13)
  2016-04-29 09:31:15.998975: Received ws message: 'Hello World - 3'
  Traceback (most recent call last):
      File "/usr/local/lib/python2.7/dist-packages/web/application.py", line 239, in process
          return self.handle()
        File "/usr/local/lib/python2.7/dist-packages/web/application.py", line 230, in handle
          return self._delegate(fn, self.fvars, args)
        File "/usr/local/lib/python2.7/dist-packages/web/application.py", line 420, in _delegate
          return handle_class(cls)
        File "/usr/local/lib/python2.7/dist-packages/web/application.py", line 396, in handle_class
          return tocall(*args)
        File "wsgi.py", line 30, in GET
          data = uwsgi.websocket_recv_nb()
      IOError: unable to receive websocket message
```
