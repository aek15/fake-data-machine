#!/bin/bash

# Echo the correct URL
echo "Access the Fake Data Generator app at: http://localhost:8501"

# Start Streamlit in the background
streamlit run faker-generator/app.py --server.address 0.0.0.0 --server.port 8501 &

# Keep the script running
tail -f /dev/null
