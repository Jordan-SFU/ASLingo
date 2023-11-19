navigator.mediaDevices.getUserMedia({ video: true })
    .then(function(stream) {
        var video = document.querySelector('video');
        video.srcObject = stream;

        // Access video track to get details
        var videoTrack = stream.getVideoTracks()[0];
        console.log('Video track settings:', videoTrack.getSettings());
    })
    .catch(function(err) {
        console.log(err);
    });