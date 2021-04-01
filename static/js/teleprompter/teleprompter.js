var app = new Vue({
  el: '#app',
  data: {
  	tp: {
      largura: 300,
      altura: 296,
      alturaLeitura: 25,
      velocidade: 16,
      tamanhoTexto: 25,
      alturaLinha: 40,
      alturaLeitura: 25,
      opacidadeLeitura: 1,
      element: document.getElementById('speech'),
      scrolling: null,
      inc: 1,
      wait: 50,
      altura: document.getElementById('speech').offsetHeight
    },
    connection: null,
  },
  created: function() {
  	window.addEventListener('keyup', this.keyUp);
    document.getElementById('speech').removeAttribute('maxlength');

    this.connection = new WebSocket('ws://' + window.location.host + '/ws')

    setInterval(() => this.connection.send('echo'), 1000)

    this.connection.onmessage = ((ev) => {
        const response = JSON.parse(ev.data);
        /*this.remoteControl(response);*/
    });

    $( "#teleprompter").draggable();
  },
  methods: {
      doScroll: function() {
      	document.getElementById('speech').style.top = '-'+this.tp.inc+'px';
        this.tp.inc = this.tp.inc + 1;
      },
      play: function() {
      	if (!this.tp.scrolling) {
        	this.tp.scrolling = setInterval(() => this.doScroll(), parseInt(this.tp.velocidade));
        }
        //document.getElementById('foco').style.display = 'block';
      },
      edit: function() {
      	if (this.tp.scrolling) {
        	clearInterval(this.tp.scrolling);
          this.tp.scrolling = null;
          document.getElementById('foco').removeAttribute('style');
          document.getElementById('foco').style.display = 'none !important';
        }
      },
      pauseInPlay: function() {
      	if (this.tp.scrolling) {
        	clearInterval(this.tp.scrolling);
          this.tp.scrolling = null;
        } else {
        	this.play();
        }
      },
      reset: function() {
      	document.getElementById('speech').style.top = '0px';
        document.getElementById('speech').scrollTop = 0;
        clearInterval(this.tp.scrolling);
        this.tp.scrolling = null;
        
        setTimeout(() => this.play(), 2000);
        document.getElementById('foco').style.display = 'block';
        this.tp.inc = 1;
      },
      scrollShow: function() {
      	document.getElementById('foco').removeAttribute('style');
        document.getElementById('foco').style.display = 'none !important';
      },
      keyUp: function(event) {
        switch (event.which) {
          case 39:
            this.connection.send('next');
            break;
          case 37:
            this.connection.send('prev');
            break;
          case 32:
            this.pauseInPlay();
            break;
          case 8:
            document.getElementById('foco').style.display = 'block';
            break;
        }
      },
      /*
      remoteControl: function(ev) {
        switch (ev.event) {
            case 'play':
                this.pauseInPlay();
                break;
            case 'pause':
                this.pauseInPlay();
                break;
            case 'faster':
                this.tp.velocidade--;
                break;
            case 'slower':
                this.tp.velocidade++;
                break;
        }
      }
      */
    }
  });