// methods for calling the python API from html

const hostIP = "localhost"
const apiURL = `http://${hostIP}:5000`

async function addUrl() {
	await fetch(apiURL + "/addlink", {
		method: "POST",
		headers: {
			'Content-Type': "application/json",
			'Accept': "application/json",
		},
		body: JSON.stringify({
			"url": document.getElementById("new-link-text").value,
		}),
	}).then(() => {
		document.getElementById("new-link-text").value = "";
	});
}

async function deleteUrl(url) {
	await fetch(apiURL + "/deletelink", {
		method: "POST",
		headers: {
			'Content-Type': "application/json",
			'Accept': "application/json",
		},
		body: JSON.stringify({
			"url": url,
		}),
	}).then(() => {
		window.location.reload();
	});
}

async function resetLinks() {
	await fetch(apiURL + "/resetdb", {
		method: "POST",
	}).then(() => {
		window.location.reload();
	});
}
