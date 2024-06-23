# linkdme
 
local postgres database
params = {
            'database': 'postgres',
            'user': 'postgres',
            'password': 'skippy123',
            'host': '127.0.0.1',
            'port': 5432
            }

helpful commands:
sudo systemctl restart apache2
curl http://3.19.164.119/
sudo nano /etc/apache2/apache2.conf
sudo service apache2 status
waitress-serve --host=127.0.0.1 --call 'flaskr:create_app'
cntrl z
bg
fg
printenv
nano /etc/environment