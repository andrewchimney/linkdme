# LIKNDM.EE

This a project that is a clone on linktr.ee which is a website where users can create a landing page to store all their links for easy access. It is avaible at https://linkdm.ee. 

# Built With

This project is built using a Python Flask backend that serves pure javascript, css, and html files. The flask backend runs on a Ubuntu Linux AWS EC2 instance. On the linux instance, there is an Apache server that uses a reverse proxy forward requests from linkdm.ee to flask server running locally. There is a also a PostgreSQL database running on an AWS RDS instance to store database and an AWS S3 bucket to store images.

# Usage

After visiting linkdm.ee you will be greeted with a home page which has a sign up and log in button. Click the sign up button to be taken to https://linkdm.ee/auth/register where you can enter a username and password to create an account. After creating a profile, you will be taken to the profile page, where you can add a profile picture, create a bio, and add links. Your profile will always be at ht<span>tps://<span>linkdm.ee/\<username\>.


