#!/bin/bash

script_directory="$(pwd)/utils"  # Replace with the actual path to the /utils directory

run_script_new_tab() {
  osascript -e "tell application \"Terminal\" to do script \"cd '$script_directory' && python3 '$1'\""
}

# go to h365 and run npm run serve
osascript -e "tell application \"Terminal\" to do script \"cd '$(pwd)'/h365 && npm run serve\""

# Get a list of all Python files in the /utils directory and run them in new tabs, excluding files containing "test"
for script in "$script_directory"/*.py; do
  if [[ "$script" != *"test"* ]]; then
    run_script_new_tab "$script"
  fi
done



