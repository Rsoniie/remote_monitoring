document.getElementById('addUserButton').addEventListener('click', async () => {
    // await apiCall('http://localhost:5000/add_user', 'POST', 'Add User', null);
    await apiCall('http://127.0.0.1:5000/add_user', 'POST', 'Add User', null);
});

document.getElementById('addDataButton').addEventListener('click', async () => {
    const username = document.getElementById('username').value;
    if(username) {
        // await apiCall(`http://localhost:5000/add_data/${username}`, 'POST', 'Add Data', username);
        await apiCall(`http://127.0.0.1:5000/add_data/${username}`, 'POST', 'Add Data', username);
    } else {
        displayResponse('Username is required for adding data.');
    }
});

document.getElementById('fetchHistoryButton').addEventListener('click', async () => {
    const username = document.getElementById('username').value;
    if(username) {
        await apiCall(`http://127.0.0.1:5000/history/${username}`, 'GET', 'Fetch History', username);
    } else {
        displayResponse('Username is required to fetch history.');
    }
});

async function apiCall(url, method, action, username) {
    try {
        const options = {
            method: method,
            headers: {
                'Content-Type': 'application/json'
            }
        };
        const response = await fetch(url, options);
        const data = await response.json();

        displayResponse(`${action} - Status: ${response.status}, Data: ${JSON.stringify(data)}`);
    } catch (error) {
        displayResponse(`Error in ${action}: ${error.message}`);
    }
}

function displayResponse(message) {
    document.getElementById('responseArea').textContent = message;
}
