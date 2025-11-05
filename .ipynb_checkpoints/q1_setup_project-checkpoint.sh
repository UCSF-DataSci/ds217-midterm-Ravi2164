#!/bin/bash
import pandas as pd
echo " strating project setup.."

echo "setting up directories..."
mkdir -p data output reports 

echo "generating dataset.."
python3 generate_data.py

echo "saving directory structure.."
ls -la > reports/directory_structure.txt 
echo "Project setup complete!" 





