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