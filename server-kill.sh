# kill processes
pkill flask
pkill python

cd ~/Desktop/serve/scripts

# reset anything environment-related
sed -i "s/$AIRDROOP_IP/localhost/g" "js/useAPI.js"
sed -i "s/$AIRDROOP_IP/localhost/g" "bundle_html.py"