if (window.location.protocol == "https:") {
    var ws_scheme = "wss://";
  } else {
    var ws_scheme = "ws://"
  };

const ws = new WebSocket('ws://' + window.location.host + '/ws')

function controlPresentation(ev) {
    switch(ev) {
        case 'pass_left':
            ws.send('prev')
            break;
        case 37:
            ws.send('prev')
            break;
        case 'pass_right':
            ws.send('next')
            break;
        case 39:
            ws.send('next')
            break;
        case 'play':
            ws.send('play')
            playAndPause('pause');
            break;
        case 13:
            ws.send('play')
            playAndPause('pause');
            break;
        case 'pause':
            ws.send('pause')
            playAndPause('play');
            break;
        case 32:
            playAndPause('play');
            break;
        case 'exit':
            ws.send('exit')
            break;
        case 8:
            ws.send('exit')
            break;
        case 'faster':
            ws.send('faster')
            break;
        case 38:
            ws.send('faster')
            break;
        case 'slower':
            ws.send('slower')
            break;
        case 40:
            ws.send('slower')
            break;
    }
}

play = true

document.onkeyup = function(ev) {
    ev = ev || window.event;
    keyCode = ev.keyCode || ev.which;
    console.log('Key: ' + keyCode)
    controlPresentation(keyCode);
}

function playAndPause(ev) {
    el = document.getElementById('playPause')
    if (play) {
        ws.send('pause')
        play = false
        el.src = '/static/images/control/button_pause.svg'
        el.setAttribute('onclick', "controlPresentation('pause')")
    } else {
        ws.send('play')
        play = true
        el.src = '/static/images/control/button_play.svg'
        el.setAttribute('onclick', "controlPresentation('play')")
    }
}

// Callback qundo uma mensagem for recebida
//ws.onmessage = this.onMessage

// Manter conexão ativa
setInterval(() => ws.send('echo'), 1000)

/* function onMessage(ev) {
    const recv = JSON.parse(ev.data)
    console.log(recv);

    ws.send('Opa Marcos')
} */