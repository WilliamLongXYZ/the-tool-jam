pip install pyinstaller
pyinstaller src/main.py -F
rm build -r
mv dist/main ./
rm dist -r
rm main.spec
./main
