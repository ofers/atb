# at-bay

1. clone or download code from github to /app
2. set the db IP at "/app/webapp/mydb.py" to the deocker host IP (need to be fixed)
3. build docker with: "sudo docker build -t webapp ." from "/app/docker"
4. run docker stack by exec the run.sh script at: "/app/docker"
