# at-bay

Install:
1. clone or download code from github to /app
2. set the db IP at "/app/webapp/mydb.py" to the decker host IP (need to be fixed)
3. build docker with: "sudo docker build -t webapp ." from "/app/docker"
4. run docker stack by exec the run.sh script at: "/app/docker"


Known issues:
1. no check if employee PID exist before adding a new emp. no duplicate emp will be added but no error/info msg will be pop to the user.
2. communication between the 2 dockers are based on the host IP. this is not dynamic and ned to be fixed.