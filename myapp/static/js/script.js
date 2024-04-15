console.log("Hello from JS")
const socket = new WebSocket('ws://localhost:8000/ws/contar/');
let isFirstMessage = true;
const contadorContainer = document.getElementById('contador')
const sendButton = document.getElementById('sendButton')
const numInput = document.getElementById('numero');
const count = document.getElementById('count');

let numero 

socket.onopen = function (e) {
    console.log('Conexión establecida');
};

socket.onmessage = function (event) {
    const json = JSON.parse(event.data)
    console.log(json)
    count.innerText = " "+json.count + "/" + numero
    if (isFirstMessage) {
        contadorContainer.innerHTML = "<div class='countItem'>" + json.message + " --- Time:" + json?.timestamp + '</div>';
        isFirstMessage = false;
    } else {
        contadorContainer.innerHTML += "<div class='countItem'>" + json.message + " --- Time:" + json?.timestamp + '</div>';
    }
};
socket.onclose = function (event) {
    contadorContainer.innerHTML += '<div class="finishItem">Finished/disconnected</div>';
};

function enviarNumero() {
    sendButton.disabled = true;
    numInput.disabled = true

    contadorContainer.innerHTML += 'Contando...';
    numero = numInput.value;
    socket.send(JSON.stringify({ 'numero': numero }));
}
