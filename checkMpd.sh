#!/bin/bash
while : ; do
        mpc idle
        mpc current > mpdStatus.txt
        python3 text.py
done

