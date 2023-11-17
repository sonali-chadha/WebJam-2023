let serverURL = '[instert link... from ngrok?]'


function callBackEnd(){
    fetch(serverURL)
    .then(res => res.json())
    .then(data => {
        //something data blah blah
        document.getElementById('display').innerHTML = data.message
    })
}
