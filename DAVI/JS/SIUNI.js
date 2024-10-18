function LoadPageContent(Page) {
    fetch(Page)
        .then(response => response.text())
        .then(data => { document.getElementById("Conteudo").innerHTML = data } )
        .catch(error => console.log("Não foi possivel carregar: ", error ) )
    }



    