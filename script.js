// frontend/script.js
document.getElementById('image-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    let formData = new FormData();
    formData.append('image', document.getElementById('image-upload').files[0]);
  
    // Show progress bar
    let progress = document.getElementById('progress');
    progress.style.width = '0%';
  
    fetch('/upload-image', {
      method: 'POST',
      body: formData,
    })
    .then(response => response.blob())
    .then(data => {
      let imageURL = URL.createObjectURL(data);
      document.getElementById('compressed-image-container').innerHTML = `<img src="${imageURL}" />`;
    })
    .catch(error => console.error('Error:', error));
  });
  