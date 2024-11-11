
function AdicionarNoticia() {
    let Noticia = document.createElement('div')
    fetch('../HTML/Elementos/Noticia.html')
        .then(resposta => resposta.text())
        .then(html => {Noticia.innerHTML = html; Noticia.classList.add("Noticia")})
        .catch(error => { console.error('Erro erro', error); });
    
    const feed = document.getElementById('AreaDeConteudo')
    feed.appendChild(Noticia)
    }




