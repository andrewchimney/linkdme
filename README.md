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
sudo ssh -i "databasedec2.pem" ubuntu@ec2-3-19-164-119.us-east-2.compute.amazonaws.com
sudo systemctl restart apache2
curl http://3.19.164.119/
curl http://127.0.0.1:8080
sudo nano /etc/apache2/apache2.conf
sudo nano /etc/apache2/sites-available/000-default.conf
sudo service apache2 status
waitress-serve --host=127.0.0.1 --call 'flaskr:create_app'
cntrl z
bg
fg
printenv
nano /etc/environment
crontab -e
crontab -l