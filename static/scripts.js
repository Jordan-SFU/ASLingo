function sendFrames() {
  if (video.paused || video.ended) {
      return;
  }
  var canvas = document.createElement('canvas');
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  var ctx = canvas.getContext('2d');
  ctx.drawImage(video, 0, 0);
  var dataURL = canvas.toDataURL('image/jpeg', 0.5);
  var data = dataURL.split(',')[1];

  // Send a POST request to the server with the frame data
  fetch('/process_frame', {
      method: 'POST',
      body: data
  }).then(response => response.text())
    .then(prediction => {
      // Do something with the prediction
      console.log(prediction);
  });

  setTimeout(sendFrames, 1000 / 30);
}