#!/bin/bash
#ramember to chmod u+x 😊 or else I will find you, and I will Kill you
set -euo pipefail
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
Python=$(which python3)
uploadFile () {
    if [[ "$1" != *"/.DS_Store" ]]; then
        if [ ! -f "$1" ]; then
            $Python "$SCRIPT_DIR/GoogleDrive.py" --op="D" --fi="$1"
        else
            $Python "$SCRIPT_DIR/GoogleDrive.py" --op="I" --fi="$1"
        fi
    fi
}

export -f uploadFile

fswatch -0 "$SCRIPT_DIR"| xargs -0 -n 1 -I {} bash -c 'uploadFile "{}"'