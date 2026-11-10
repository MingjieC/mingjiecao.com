#!/bin/sh
# Compile cv.tex and copy the PDF to files/ for the website.
set -e
cd "$(dirname "$0")"
mkdir -p build
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build cv.tex >/dev/null
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build cv.tex >/dev/null
cp build/cv.pdf ../files/Mingjie_Cao_CV.pdf
echo "Built files/Mingjie_Cao_CV.pdf"
