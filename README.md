### Example of reverse proxy using Nginx
Reverse proxy allows you to terminate SSL/TLS and redirect traffic to internal services.
In this example __app1__ and __app2__ docker containers are playing role of such services.

### How to generate SSL certificate
```
$ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout example.key -out example.crt

Generating a RSA private key
...................................+++++
............+++++
writing new private key to 'example.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:RU
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Example Company
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:
Email Address []:
```
