# media.ilmnuri.com

## this app has api and website of ilmnuri apps. 

* in nginx conf do not forget to put
```bash 
     location / {
              include uwsgi_params;
              uwsgi_pass unix:/usr/share/nginx/html/app.sock;
        }
```
