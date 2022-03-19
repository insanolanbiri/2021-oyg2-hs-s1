#!/bin/bash
if [ "${BASH_SOURCE[0]}" -ef "$0" ]; then
    echo "bunu source ile kullanman gerek dostum"
    exit 1
fi

function derle (){ 
    gcc "$1" "${@:2}" -o "${1::-2}" && "${1::-2}"
    rm "${1::-2}" 2>/dev/null 
}
