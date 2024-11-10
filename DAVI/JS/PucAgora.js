
function AdicionarNoticia() {
    let Noticia = document.createElement('div')
    fetch('../HTML/Noticia.html')
        .then(resposta => resposta.text())
        .then(html => {Noticia.innerHTML = html; Noticia.classList.add("Noticia")})
        .catch(error => { console.error('Erro erro', error); });
    
    const feed = document.getElementById('AreaDeConteudo')
    feed.appendChild(Noticia)
    }




// ConteudoNoticia = document.getElementById("ConteudoNoticia")

// ModalNoticia    = document.getElementById("ModalNoticia")
// BotaoFechar     = document.getElementById("Noticia-IconCloseButton")


// function AbrirNoticia() {
//     ModalNoticia.style.display = 'flex'
//     }


// BotaoFechar.onclick = function() { ModalNoticia.style.display = 'none' }

// window.addEventListener('click', (event) => {
//     if (event.target == ModalNoticia) { ModalNoticia.style.display = 'none' }
//     }  )

