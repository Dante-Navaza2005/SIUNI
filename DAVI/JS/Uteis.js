



function foundAndExecute(elementoId, funcao) {
    var observador = new MutationObserver( (mutationList) => {

        for (mutation in mutationList) {
            var elemento = document.getElementById(elementoId)
            if (elemento) {
                funcao()
                observador.disconnect()
                }            
            }
        })
    
    observador.observe(document.body, { childList:true, subtree:true })

    }




function achou() {
    console.log('DADADAFADFASFAFk')
    }
