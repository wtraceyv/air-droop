// Export methods for calling the python API from html

const apiURL = "http://localhost:5000"

function addUrl() {
	fetch(apiURL + "/addlink", {
		method: "POST",
		headers: {
			'Content-Type': "application/json",
			'Accept': "application/json",
		},
		body: JSON.stringify({
			"url": document.getElementById("new-link-text").value,
		}),
	});
}

function resetLinks() {
	fetch(apiURL + "/resetdb", {
		method: "POST",
	});
}

// TODO: nope need IDs
function deleteUrl() {
	fetch(apiURL + "/deletelink", {
		method: "POST",
		headers: {
			'Content-Type': "application/json",
			'Accept': "application/json",
		},
		body: JSON.stringify({
			// FIXME: put the fix here
			"url": document.getElementById("new-link-text").value,
		}),
	});
}