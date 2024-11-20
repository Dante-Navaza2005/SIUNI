
let pucAgoraIndiceAbaSelecionada = 1

let abaPintada = null



function construirPucAgora() {
    isConstruido = true
    pucAgoraDefinirabas( )
    pucAgoraSelecionarAba( pucAgoraIndiceAbaSelecionada )
    }
    
// Associar abas a função de selecionar aba EventListener
function pucAgoraDefinirabas() {
    let abas = document.querySelectorAll(".ABA")
    abas.forEach( (aba) => { aba.addEventListener("click", (event)=>{ pucAgoraSelecionarAba(aba.getAttribute('data-l')) } ) })
    }

// Selecionar aba, carregar conteudo e mudar a cor do botão
function pucAgoraSelecionarAba(indiceAba) {
    var aba = document.querySelector(`[data-l="${indiceAba}"]`)
    pucAgoraMudaCorAba(aba)
    pucAgoraIndiceAbaSelecionada = aba.getAttribute("data-l")
    pucAgoraCarregarConteudo(aba)    
    }

// função que muda a cor do botão
function pucAgoraMudaCorAba(aba) {
    if (abaPintada) { abaPintada.style.backgroundColor = '' }
    aba.style.backgroundColor = 'var(--BackgroundColorB)'
    abaPintada = aba
    }
            
// função que carrega o conteúdo
function pucAgoraCarregarConteudo(aba) {
    var conteudo = aba.getAttribute('data-ctn')
    var pucAgoraAreaDeconteudo = document.getElementById("AreaDeConteudo")
    fetch(`PucAgora/${conteudo}.html`)
        .then( response => response.text())
        .then( resposeText => { pucAgoraAreaDeconteudo.innerHTML = resposeText } )
        .catch(error => console.log("Não foi possivel carregar: ", error ) )

    if (conteudo == 'Feed') { carregarNoticias() }

    }



