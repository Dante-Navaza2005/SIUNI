

function construirMeuCurso() {
    isConstruido = true
    console.log('Construindo MeuCurso')

    meuCursoAdicionarCelulas()
    meuCursoAjustarCelulas()

    }


function meuCursoAdicionarCelulas() {
    var grade = document.getElementById('MeuCursoAreaGradeGrade')
    var rows = 5 + 1
    var cols = 20 + 1

    grade.style.gridTemplateColumns=`repeat(${cols}, 1fr)`
    grade.style.gridAutoRows=`1fr`

    for (var row = 0; row < rows; row++) {
        for (var col = 0; col < cols; col ++) {
            let celula = document.createElement('div')
            celula.classList.add('MeuCursoAreaGradeGradeCelula')
            celula.setAttribute('data-row', row)
            celula.setAttribute('data-col', col)
            //celula.addEventListener('click', (event) => { celula.style.backgroundColor='red' })    
            grade.appendChild(celula)

            }
        }
    }

 
function meuCursoAjustarCelulas() {
    var celulasDeDias = document.querySelectorAll('[data-row="0"]')
    for (var i = 1; i < celulasDeDias.length; i++) { 
        celulasDeDias[i].classList.add('CelulaDiaDaSemana')
        celulasDeDias[i].innerHTML = diaEmPortugues(i) 
        celulasDeDias[i].setAttribute('data-day', diaEmPortugues(i))
    }

    var celulasDeHoras = document.querySelectorAll('[data-col="0"]')
    for (var i = 1; i < celulasDeHoras.length; i++) { 
        celulasDeHoras[i].classList.add('CelulaHora')
        celulasDeHoras[i].innerHTML = `Hora ${i}` }


    }

function diaEmPortugues(numeroDia) {

    switch (numeroDia) {
        case 0 : return 'DOM'
        case 1 : return 'SEG'
        case 2 : return 'TER'
        case 3 : return 'QUA'
        case 4 : return 'QUI'
        case 5 : return 'SEX'
        case 6 : return 'SAB'
        default: return 'NTF'
        }

    }





function meuCursoAdicionarMateterias() {


    }








