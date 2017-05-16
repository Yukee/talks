#!/bin/bash

for idx in {0..7}
do cairosvg "wheel_P3_$idx.svg" -o "wheel_P3_$idx.pdf"
done

