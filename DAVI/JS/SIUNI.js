
let botaoAnterior = null;

function LoadPageContent(Page, event) {
    fetch(Page)
        .then(response => response.text())
        .then(data => { document.getElementById("Conteudo").innerHTML = data } )
        .catch(error => console.log("Não foi possivel carregar: ", error ) )

    let botaoAtual = event.currentTarget
    if (botaoAnterior) { botaoAnterior.style.backgroundColor = ''; }
    botaoAtual.style.backgroundColor = 'rgba(255, 255, 255, 0.1)';
    botaoAnterior = botaoAtual;


    }



    