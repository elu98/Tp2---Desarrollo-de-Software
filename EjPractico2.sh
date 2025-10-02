#!/bin/bash

if python3 --version &> /dev/null; then
    echo "Python 3 is installed."
else
    echo "Python 3 is not installed. Please install Python 3 to proceed."
    sudo apt install python3
fi

if pip3 --version &> /dev/null; then
    echo "pip3 is installed."
else
    echo "pip3 is not installed. Installing pip3..."
    sudo apt install python3-pip
fi

mkdir -p {static/{css,images},templates,.venv}
touch app.py

python3 -m venv .venv

source .venv/bin/activate

pip3 install Flask
pip3 install Flask-Mail

echo "Virtual Environment created and Flask installed."

