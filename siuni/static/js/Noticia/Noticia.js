
// Função que carrega uma quantidade de noticias no feed
function carregarNoticias() { // FEED
    foundAndExecute('Feed', async () => {    
        // Fetch no modelo de noticia em feed
        const response = await fetch('../HTML/Elementos/Noticia.html');
        const modeloNoticia = await response.text()

        for (var a = 0; a < 20; a++) {

            // Estruturação da notícia
            let Noticia = document.createElement('div')
            Noticia.innerHTML = modeloNoticia;  
            Noticia.classList.add("Noticia") 
            Noticia.setAttribute('data-testid', `${a}`)
            Noticia.addEventListener('click', () => abrirNoticia(Noticia) )

            carregarConteudoDaNoticia(Noticia)
            
            // Adiçao da noticia como filho de feed
            const feed = document.getElementById('Feed')
            feed.appendChild(Noticia)
            
            }
        })
    }
    
// Essa função abre uma notícia expandida em um modal
function abrirNoticia(noticia, event) {
    abrirModal()
    carregarNoticia(noticia)

    }


window.addEventListener("click", (event) => {
    event.stopPropagation()
    if (event.target = document.getElementById('ModalNoticia')) { fecharModal('ModalNoticia', event) }
    })
    
    
    
    
// Essa função carrega o mini conteúdo de uma noticía no feed
function carregarConteudoDaNoticia(Noticia) {
    
    }

    


// Essa função carrega o conteuda da noticia expandinda no modal
function carregarNoticia(noticia) {
    foundAndExecute('ModalConteudo', () => {
        document.getElementById('ModalConteudo').innerText = noticia.getAttribute('data-testid')

        })

    }





