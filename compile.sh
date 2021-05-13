pip install pyinstaller
pyinstaller src/main.py -F
rm build -r
mv dist/main ./
rm dist -rf
rm main.spec
./main
