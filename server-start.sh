export AIRDROOP_IP="10.0.0.23"

# start stupid servers
cd ~/Desktop/serve/scripts

# If you gave me a specific IP, I will serve to all local net clients;
# you have to specify this for Flask and the JS api callers
if [ -z "$AIRDROOP_IP" ]
then
	flask --app api run 2> /dev/null &
else
	echo 'hi i lived'
	echo $AIRDROOP_IP
	sed -i -e "s/localhost/$AIRDROOP_IP/g" js/useAPI.js
	sed -i -e "s/localhost/$AIRDROOP_IP/g" bundle_html.py
	# flask --app api run --host="$AIRDROOP_IP" 2> /dev/null &
	flask --app api run --host=$AIRDROOP_IP &
fi


python3 -m http.server -d ~/Desktop/serve 2> /dev/null &
chromium "http://localhost:8000" 2>/dev/null &