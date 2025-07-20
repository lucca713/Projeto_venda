console.log("Carregou o js");

document.addEventListener('DOMContentLoaded', function() {
    //  Seleciona todos os elementos do DOM 
    const cepInput = document.getElementById("cep");
    const addProdutoBtn = document.getElementById("add-produto-btn");
    const produtoSelect = document.getElementById("produto-select");
    const quantidadeInput = document.getElementById("quantidade");
    const tabelaItens = document.getElementById("tabela-itens");
    const subtotalVendaSpan = document.getElementById("subtotal-venda");
    const itensVendaInput = document.getElementById("itens_venda_input");
    
    // Array qye guarda os estados
    let itensDaVenda = []; 

   // Funcao que atualiza tudo a cada alteracao
    function atualizarTudo() {
        //Calcula o subtotal somando a propriedade 'subtotal' de cada item.
        const subtotalGeral = itensDaVenda.reduce((total, item) => total + item.subtotal, 0);
        
        //Exibe o valor formatado na tela.
        subtotalVendaSpan.textContent = subtotalGeral.toFixed(2);
        
        // Atualiza o campo escondido com os dados em formato json para enviar ao Django.
        itensVendaInput.value = JSON.stringify(itensDaVenda);
        console.log("Input Hidden Atualizado:", itensVendaInput.value);
    }

  

    // API CEP
    cepInput.addEventListener("blur", function() {
        const cep = cepInput.value.replace(/\D/g, '');
        if (cep.length === 8) {
            fetch(`https://viacep.com.br/ws/${cep}/json/`)
                .then(response => response.json())
                .then(data => {
                    if (!data.erro) {
                        document.getElementById('rua').value = data.logradouro;
                        document.getElementById('bairro').value = data.bairro;
                        document.getElementById('cidade').value = data.localidade;
                        document.getElementById('estado').value = data.uf;
                    } else {
                        alert("CEP não encontrado.");
                    }
                })
                .catch(error => console.error("Erro na busca do CEP:", error));
        }
    });

    // Adiciona produto na tabela
    addProdutoBtn.addEventListener('click', function() {
        const selectedOption = produtoSelect.options[produtoSelect.selectedIndex];

        if (!selectedOption.value) return;

        const produtoId = selectedOption.value;
        const produtoNome = selectedOption.getAttribute("data-nome");
        const produtoValor = parseFloat(selectedOption.getAttribute("data-valor"));
        const quantidade = parseInt(quantidadeInput.value);

        // Verifica se o item ja foi adicionado
        const itemExistente = itensDaVenda.find(item => item.produto_id === produtoId);
        if (itemExistente) {
            alert("Produto já adicionado. Para alterar a quantidade, remova o item e adicione-o novamente.");
            return;
        }

        const subtotalItem = produtoValor * quantidade;

        // Adiciona o novo item
      
        itensDaVenda.push({
            produto_id: produtoId,
            quantidade: quantidade,
            preco_unitario: produtoValor,
            subtotal: subtotalItem, 
        });

        // Cria a nova linha no html
        const newRow = tabelaItens.insertRow();
        newRow.setAttribute("data-produto-id", produtoId);

        newRow.innerHTML = `
            <td>${produtoNome}</td>
            <td>...</td> 
            <td>${quantidade}</td>
            <td>R$ ${produtoValor.toFixed(2)}</td>
            <td>R$ ${subtotalItem.toFixed(2)}</td>
            <td><button type="button" class="btn btn-danger btn-sm remover-item-btn">Remover</button></td>
        `;

        // Funcao que atualiza os totais
        atualizarTudo();

        // Limpa os capos
        produtoSelect.selectedIndex = 0;
        quantidadeInput.value = 1;
    });

    // Remover itens da tabela
    tabelaItens.addEventListener('click', function(event) {
       
        if (event.target.classList.contains("remover-item-btn")) {
            const row = event.target.closest("tr");
            const produtoId = row.getAttribute("data-produto-id");

            // Remover o item do array 
            itensDaVenda = itensDaVenda.filter(item => item.produto_id !== produtoId);

            // Removre a linha 
            row.remove();
            
            // Atualiza os totais
            atualizarTudo();
        }
    });
});