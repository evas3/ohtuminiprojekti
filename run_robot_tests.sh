#!/bin/bash

# Start the application
poetry run invoke start &

# Add a sleep to wait
sleep 10

# Run the robot tests
poetry run robot/src/tests

status=$?

# Stop the server in port
kill $(lsof -t -i:5001)

exit $status