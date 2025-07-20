console.log("Carregou o js");
document.addEventListener('DOMContentLoaded', function(){
    //API ViaCep
    const cepInput = document.getElementById("cep")
    cepInput.addEventListener("blur",function() {

        //retira caracteres nao numerciso - ok
        console.log("passou aqui") //assim que eu faco testes para achar erros
        const cep = cepInput.value.replace(/\D/g,'')
        if(cep.length === 8 ){

            //link api
            fetch(`https://viacep.com.br/ws/${cep}/json/`)
            .then(response => response.json())
            .then(data =>{
                if(!data.erro){

                    console.log("passou aqui")

                    //colocar valores certo
                    document.getElementById('rua').value = data.logradouro;
                    document.getElementById('bairro').value = data.bairro;
                    document.getElementById('cidade').value = data.localidade;
                    document.getElementById('estado').value = data.uf
                }else{
                    alert("CEP não encontrado ):")
                }
            })
            //se der erro na api..
            .catch(error => console.log("erro na busca", error))

        }
    })

    //ADICIONAR PRODUTO NA TABELA - CORACAO DA APLICACAO

    const addProdutoBtn = document.getElementById("add-produto-btn")
    const produtoSelect = document.getElementById("produto-select")
    const quantidadeInput = document.getElementById("quantidade")
    const tabelaItens = document.getElementById("tabela-itens")
    const subtotalVenda = document.getElementById("subtotal-venda")
    const itensVendaInput = document.getElementById("itens_venda_input")
    
    let itensDaVenda = [] 

    addProdutoBtn.addEventListener('click', function(){
        console.log("passou aqui no formualario")
      const selectedOption = produtoSelect.options[produtoSelect.selectedIndex]; //primeiro indice comecar com -1

      if(!selectedOption.value) return // nao faz nada nao estiver escolhido

      const produtoId = selectedOption.value
      const produtoNome = selectedOption.getAttribute("data-nome");
      const produtoValor = parseFloat(selectedOption.getAttribute("data-valor"));
      const quantidade = parseInt(quantidadeInput.value);

      //verificar se os itens estao na tabela
        //fiz isso pq estava dando erro em enviar valores, "tabela estava devolvendo vazia"
        const itensTabela = itensDaVenda.find(item => item.produto_id === produtoId)

        if(itensTabela){
            alert("produto ja adicionado, se voce cometeu algum erro de quantidade só excluir e adicionar novamente. :)")
            return
        }

        const subTotal =  produtoValor * quantidade

        //adiconar o item no array de venda

        itensDaVenda.push({
            produto_id: produtoId,
            quantidade: quantidade,
            preco_unitario: produtoValor,
            subTotal: subTotal,
        })

        //Parte que vai criar uma nova linha na tabela em HTML

        const newRow = tabelaItens.insertRow()
        newRow.setAttribute("data-produto-id", produtoId)

        //se der tempo colocar o ajax para api do fornecedores

            newRow.innerHTML = `
            <td>${produtoNome}</td>
            <td>...</td> 
            <td>${quantidade}</td>
            <td>${produtoValor.toFixed(2)}</td>
            <td>${subtotalItem.toFixed(2)}</td>
            <td><button type="button" class="btn btn-danger btn-sm remover-item-btn">Remover</button></td>
        `;

        atualizarTudo();

        //limpar campos
        produtoSelect.selectedIndex = 0
        quantidadeInput.value = 1
    })

    //remover item
    tabelaItens.addEventListener('click', function(event){
        if(event.target.classList.contais("remover-item-btn")){
            const row = event.target.closest("tr")
            const produtoId = row.getAttribute("data-produto-id")

            //remove da lista
            itensDaVenda = itensDaVenda.filter(item=> item.produto_id !== produtoId)

            //remove da tabela no html
            row.remove()
            atualizarTudo();
        }
    })

    //function que atualiza tudo
 function atualizarTudo() {
        // Atualiza o subtotal geral
        const subtotalGeral = itensDaVenda.reduce((total, item) => total + item.subtotal, 0);
        subtotalVenda.textContent = subtotalGeral.toFixed(2);
        
        // Atualiza o input hidden com os dados em formato JSON
        itensVendaInput.value = JSON.stringify(itensDaVenda);
    }
})