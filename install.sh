clear

if which python3 >/dev/null; then
    if which python >/dev/null; then
        if [ "$(python --version)" == "Python 3*" ]; then
            echo "[^] Python 3 is required." 
            exit 1
        fi
    else
        echo "[^] Python 3 not found." 
        exit 1
    fi
fi

echo "[!] Creating virtualenv"
python3 -m virtualenv venv

if [ ! -f "activate" ]; then
	ln -s venv/bin/activate .
fi

. ./activate

echo "[!] Installing Piper"
pip3 install .


clear
sleep 1
echo ""
echo "Install.sh complete. "
echo "Feel free to guide the rats with Piper"
echo ""
echo "To use the virtualenv created run:"
echo "    . ./activate"
echo ""