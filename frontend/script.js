const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('upload');
const fileLabel = document.getElementById('file-label-text');
const iconArea = document.getElementById('icon-area');
const convertBtn = document.getElementById('convert-btn');

// Highlight drop zone on drag
dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('dragover');
});

dropZone.addEventListener('dragleave', () => {
    dropZone.classList.remove('dragover');
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('dragover');
    if (e.dataTransfer.files.length) {
        fileInput.files = e.dataTransfer.files;
        // Manually trigger change event so the file is processed
        fileInput.dispatchEvent(new Event('change'));
    }
});

// When file is manually selected
fileInput.addEventListener('change', () => {
    if (fileInput.files.length) {
        updateFileName(fileInput.files[0].name);
        convertBtn.disabled = false;
    } else {
        fileLabel.textContent = 'Select or Drag Markdown File';
        iconArea.style.display = '';
        convertBtn.disabled = true;
    }
});

convertBtn.addEventListener('click', () => {
    if (fileInput.files.length) {
        uploadFile(fileInput.files[0]);
    }
});

function updateFileName(name) {
    fileLabel.textContent = name;
    iconArea.style.display = 'none';
}
function uploadFile(file) {
    const formData = new FormData();
    formData.append('file', file);

    fileLabel.textContent = 'Converting...';
    iconArea.style.display = 'none';

    fetch('/convert', {
        method: 'POST',
        body: formData
    })
    .then(async response => {
        const contentType = response.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
            return response.json();
        } else {
            const text = await response.text();
            throw new Error('Server error: ' + text);
        }
    })
    .then(data => {
        if (data.success) {
            fileLabel.textContent = 'Conversion Complete!';
            // Redirect to download page
            window.location.href = `download.html?download_url=${encodeURIComponent(data.download_url)}&file_name=${encodeURIComponent(data.filename)}`;
        } else {
            throw new Error(data.error || 'Conversion failed');
        }
    })
    .catch(error => {
        fileLabel.textContent = 'Error: ' + error.message;
        setTimeout(() => {
            fileLabel.textContent = 'Select or Drag Markdown File';
            iconArea.style.display = '';
        }, 3000);
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const toggleBtn = document.getElementById('darkModeToggle');

    // Check for saved dark mode preference
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
});