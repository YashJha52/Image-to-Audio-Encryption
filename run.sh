#!/bin/bash

echo "Activating sip virtual environment..."
source sip/bin/activate

echo "Launching Frontend UI..."
python -m frontend.ui