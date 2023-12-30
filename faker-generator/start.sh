#!/bin/bash

# Echo the correct URL
echo "Access the Fake Data Machine app at: http://localhost:8501"

# Start Streamlit in the background and redirect its output
nohup streamlit run app.py --server.address 0.0.0.0 --server.port 8501 > /dev/null 2>&1 &

# Wait a bit to ensure Streamlit starts
sleep 5

# Release the terminal
exec "$@"
