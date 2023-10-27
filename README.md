# air-droop
Dumb local network file and link sharing with frontend. Don't use it to do anything important.

Uses:
- Python: bundles html with templating, hosts API, talks to DB
  - Flask for API
  - Sqlite3 for basic DB functions
- Vanilla HTML, CSS, JS
- Shell script to get it going

### Note:
`server-start.sh` and `scripts/js/useAPI.js` must reflect the intended IP address to work for all devices on network. You can use localhost, but then the API actions will only work on the host. Replace the IPs with the host's full local IP, and the app will work fully for all devices local to the host. This is to accomodate Flask.
