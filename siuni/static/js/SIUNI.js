let isOpenModal = 0

function mudaCorBotao(event) {
    let botaoAtual = event.currentTarget
    if (botaoAnterior) { botaoAnterior.style.backgroundColor = ''; }
    botaoAtual.style.backgroundColor = 'var(--HoverItemBackgroundColor)';
    botaoAnterior = botaoAtual;
    }





















































// var Conteudo = document.getElementById("Conteudo")

// var Altura = Conteudo.offsetHeight
// var Largura = Conteudo.offsetWidth

// var CANVAS = document.getElementById("Canvas")

// CANVAS.width = Largura
// CANVAS.height = Altura

// var context = CANVAS.getContext("2d")

// var Raio = 50
// var X = 100
// var Y = 100
// var DX = 5
// var DY = 7

// context.fillStyle='#00F';

// function DesenhaBola() {
//     context.beginPath();
//     context.arc(X, Y, Raio, 0, Math.PI * 2);
//     context.fill();
//     }

// let animacaoBola;

// function AnimaBola() {
//     // console.log("anima")
//     context.clearRect(0, 0, Largura, Altura);
//     DesenhaBola()
    
//     if ( X - Raio < 0 || X + Raio > Largura ) { DX = -DX}
//     if ( Y - Raio < 0 || Y + Raio > Altura )  { DY = -DY}
    
//     X += DX
//     Y += DY

//     animacaoBola = requestAnimationFrame(AnimaBola)

//     }

// AnimaBola()


     






