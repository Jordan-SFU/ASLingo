navigator.mediaDevices.getUserMedia({ video: true })
  .then(function(stream) {
    /* use the stream */
    var video = document.querySelector('video');
    video.srcObject = stream;
  })
  .catch(function(err) {
    /* handle the error */
    console.log(err);
  });

  // Capture a frame from the video
var canvas = document.createElement('canvas');
canvas.getContext('2d').drawImage(video, 0, 0, video.videoWidth, video.videoHeight);

// Convert the frame to a blob
canvas.toBlob(function(blob) {
  // Send the blob to the server
  fetch('/predict', {
    method: 'POST',
    body: blob
  })
  .then(response => response.json())
  .then(data => {
    // Display the prediction
    console.log(data.prediction);
  });
}, 'image/jpeg');