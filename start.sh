echo "Cloning Repo, Please Wait..."
git clone -b alpha https://github.com/OnlyFaris/xluastream.git /xluastream
cd /xluastream
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
pip install -U youtube-dl
youtube-dl -U
echo "Starting Bot, Please Wait..."
python3 main.py
