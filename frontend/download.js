document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.getElementById('darkModeToggle');

    // Apply dark mode if it's enabled in localStorage
    if (localStorage.getItem('darkMode') === 'enabled') {
        document.body.classList.add('dark-mode');
        toggleBtn.classList.add('dark-mode-btn');
        toggleBtn.textContent = '☀️';
    }

    toggleBtn.addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
        toggleBtn.classList.toggle('dark-mode-btn');
        
        // Save the preference in localStorage
        if(document.body.classList.contains('dark-mode')) {
            toggleBtn.textContent = '☀️';
            localStorage.setItem('darkMode', 'enabled');
        } else {
            toggleBtn.textContent = '🌙';
            localStorage.setItem('darkMode', 'disabled');
        }
    });

    const downloadButton = document.getElementById('download-btn');
    const fileNameDisplay = document.getElementById('file-name');

    const urlParams = new URLSearchParams(window.location.search);
    const downloadUrl = urlParams.get('download_url');
    const fileName = urlParams.get('file_name') || 'converted_file.html';

    if (downloadUrl) {
        fileNameDisplay.textContent = `File: ${fileName}`;
        downloadButton.disabled = false;
        downloadButton.addEventListener('click', () => {
            const link = document.createElement('a');
            link.href = downloadUrl;
            link.download = fileName;
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        });
    } else {
        fileNameDisplay.textContent = 'Error: No file available for download';
        downloadButton.disabled = true;
    }
});