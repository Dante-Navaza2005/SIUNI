
// Carregamento do siuni inicial

function carregarSiuni(event) {
    console.log('Siuni carregado')
    document.getElementById('abaPucAgora').click()

    }





// CARREGAMENTO DE PAGINAS ========================================================================================================================== >>>
let PaginaAtual 

let isConstruido = 0

let isOpenModal = 0


function LoadPageContent(Page, event) {

    if (PaginaAtual != Page) {

        fetch(Page)
        .then(response => response.text())
        .then(data => { document.getElementById("Conteudo").innerHTML = data } )
        .catch(error => console.log("Não foi possivel carregar: ", error ) )
        
        PaginaAtual = Page 
        console.log(PaginaAtual)

        mudaCorBotao(event)

        isConstruido = false
        }

    }

let observadorDePaginas = new MutationObserver( (mutationList) => {
    for (mutation in mutationList) {

        const PucAgora = document.querySelector("#PucAgora")
        const Calendario = document.querySelector("#CalendarioPuc")
        const Perfil = document.querySelector("#Perfil")
        const MeuCurso = document.querySelector("#MeuCurso")

        if (PucAgora) {
            if (isConstruido == false) { construirPucAgora() }
            }
        else if (Calendario) {
            if (isConstruido == false) { construirCalendario() }
            }
        else if (Perfil) {
            if (isConstruido == false) { construirPerfil() }
            }
        else if (MeuCurso) { 
            if (isConstruido == false) { construirMeuCurso() } 
            }
        }
    })

observadorDePaginas.observe(document.body, { childList:true, subtree:true })



let botaoAnterior = null;

function mudaCorBotao(event) {
    let botaoAtual = event.currentTarget
    if (botaoAnterior) { botaoAnterior.style.backgroundColor = ''; }
    botaoAtual.style.backgroundColor = 'var(--HoverItemBackgroundColor)';
    botaoAnterior = botaoAtual;
    }







 

// ANIMÇÃO BOLINHA ================================================================================================================================== >>>























































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


     






