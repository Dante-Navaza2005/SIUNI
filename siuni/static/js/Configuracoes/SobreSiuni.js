
function AbrirSobreSiuni(event) {

    abrirModal(event, 'ConteudoSobreSiuni')

    const apiUrl = 'https://restcountries.com/v3.1/name/brazil';
    const jokeApiUrl = 'https://official-joke-api.appspot.com/random_joke';
    carregarConteudoModal('ConteudoSobreSiuni')

    }

