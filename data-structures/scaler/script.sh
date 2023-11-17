# !/bin/bash

files=($(ls [0-9][0-9]-*.md))

for item in "${files[@]}"
do
    # echo $item
    mails=($(echo $item | tr "-" "\n"))
    bar=$(printf "%s-" "${mails[@]:1}")
    bar=$(echo $bar | rev | cut -c2- | rev)
    mv $item "0${mails[0]}-$bar"
    # echo "0${mails[0]}-$bar"
done