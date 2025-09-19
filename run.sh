#!/bin/bash
# Simple script to run the Quester game

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required to run this game. Please install Python 3."
    exit 1
fi

# Check if colorama is installed
python3 -c "import colorama" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing colorama..."
    python3 -m pip install colorama
fi

# Run the game
echo "Starting Quester..."
python3 quester.py