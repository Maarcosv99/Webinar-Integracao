$("#presentation").officeToHtml({
    inputObjId: "select_file",
    pptxSetting: {
        slidesScale: "100%", //Change Slides scale by percent
        slideMode: true, /** true,false*/
        slideType: "divs2slidesjs", /*'divs2slidesjs' (default) , 'revealjs'(https://revealjs.com) */
        revealjsPath: "", /*path to js file of revealjs. default:  './revealjs/reveal.js'*/
        keyBoardShortCut: true,  /** true,false ,condition: slideMode: true*/
        mediaProcess: true, /** true,false: if true then process video and audio files */
        jsZipV2: false,
        slideModeConfig: {
            first: 1,
            keyBoardShortCut: false, /** true,false ,condition: */
            showSlideNum: false, /** true,false */
            showTotalSlideNum: true, /** true,false */
            autoSlide:1, /** false or seconds , F8 to active ,keyBoardShortCut: true */
            randomAutoSlide: false, /** true,false ,autoSlide:true */ 
            loop: true,  /** true,false */
            background: false, /** false or color*/
            transition: "slid", /** transition type: "slid","fade","default","random" , to show transition efects :transitionTime > 0.5 */
            transitionTime: 0 /** transition time between slides in seconds */               
        },
        revealjsConfig: {} /*revealjs options. see https://revealjs.com */
    }
});

if (window.location.protocol == "https:") {
    var ws_scheme = "wss://";
  } else {
    var ws_scheme = "ws://"
  };

const ws = new WebSocket('ws://' + window.location.host + '/ws')

ws.onmessage = this.onMessage

setInterval(() => ws.send('echo'), 1000)

function onMessage(ev) {
    const recv = JSON.parse(ev.data)
    if (recv.event == 'next') {
        document.getElementById('slides-next').click();
    } else if (recv.event == 'prev') {
        document.getElementById('slides-prev').click();
    }
}

function slideFull() {
    document.getElementById('presentation_div').requestFullscreen()
}

// Function after presentation is loaded
const pauseVerifyDiv = () => {
    clearInterval(verifyDiv);
}

const verifyDiv = setInterval(() => {
    if (document.getElementById('all_slides_warpper') !== null) {
        $('#select_file_div').hide()
        pauseVerifyDiv()
    }
}, 100)