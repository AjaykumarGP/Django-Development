1. Error: That port is already in use
  While running the server use, "sudo lsof -t -i tcp:8000 | xargs kill -9", to kill all the process associated with port 8000 or any other port respectively.
