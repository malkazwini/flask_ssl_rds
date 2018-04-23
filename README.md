### Deploying a Flask application in AWS: An end-to-end tutorial

Simple Flask app that writes and reads from a databse. It uses Amazon RDS for the database backend, the app uses pyopenssl for self-signed certificates

here's a quickstart guide. 

Clone this repo to your local machine. In the top level directory, create a docker image:
```
$ docker build -t flasksslrds .

```
Now run the container:
```
$  docker run -p 4443:443 -e "rds_endpoint=<RDS_ENTRYPOINT>:<RDS PORT DEFAULT 3306>" -e "rds_username=<DB USERNAME>" -e "rds_password=<DB PASSWORD>" -e "rds_dbname=<DB NAME>" -d flasksslrds

```


And point your browser to https://0.0.0.0 or https://{DNS|IP}
