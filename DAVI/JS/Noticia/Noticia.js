
let ConteudoNoticia = document.getElementById("ConteudoNoticia")
let ModalNoticia    = document.getElementById("ModalNoticia")
let NoticiaBarraDeFechamento = document.getElementById("Noticia-BarraDeFechamento")
let NoticiaBarraDeProgresso  = document.getElementById("Noticia-BarraDeProgesso")
let NoticiaDetalhada  = document.getElementById("Noticia-NoticiaDetalhada")
let NoticiaProgresso  = document.getElementById("Noticia-Progresso")
let TamanhoDaNoticiaReal
let TamanhoDaNoticiaAparente
let PosicaoVertical
let PorcentagemVertical

function AtualizaBarraProgresso(event) {
    TamanhoDaNoticiaReal = NoticiaDetalhada.scrollHeight
    TamanhoDaNoticiaAparente = NoticiaDetalhada.clientHeight
    PosicaoVertical = NoticiaDetalhada.scrollTop
    PorcentagemVertical = PosicaoVertical / (TamanhoDaNoticiaReal - TamanhoDaNoticiaAparente) * 100
    NoticiaProgresso.style.width = `${PorcentagemVertical}%`
    }


 

function abrirNoticia(page, event) {

    fetch(page)
        .then(Response => Response.text())
        .then(html => { 
            let modal = document.createElement('div')
            modal.classList.add("MODAL")
            modal.id = "ModalNoticia"
            modal.innerHTML = html
            document.getElementById("SIUNI").appendChild(modal)
            } )
        .catch(error => console.log("Não foi possivel carregar: ", error ) )

    }


window.addEventListener("click", (event) => {
    if (event.target = document.getElementById('ModalNoticia')) { fecharModal('ModalNoticia', event) }
    })
    












