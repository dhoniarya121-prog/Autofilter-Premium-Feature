if [ -z "$UPSTREAM_REPO" ]
then
    echo "Cloning main Repository"
    git clone https://github.com/hidden141/Autofilter-Premium-Feature.git /Autofilter-Premium-Feature
else
    echo "Cloning Custom Repo from $UPSTREAM_REPO"
    git clone $UPSTREAM_REPO /Autofilter-Premium-Feature
fi
cd /Autofilter-Premium-Feature
pip3 install -U -r requirements.txt
echo "Starting Bot..."
python3 bot.py
