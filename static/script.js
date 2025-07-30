function exibirMensagem(texto, tipo = 'sucesso') {
  const divMsg = document.getElementById('mensagem');
  divMsg.textContent = texto;
  divMsg.className = `mensagem ${tipo}`;
  divMsg.style.display = 'block';

  setTimeout(() => {
    divMsg.style.display = 'none';
  }, 4000); // esconde após 4s
}

// Preenche endereço a partir do CEP
document.getElementById('cep').addEventListener('blur', function () {
  const cep = this.value.replace(/\D/g, '');
  if (cep.length === 8) {
    fetch(`/buscar_cep/${cep}`)
      .then(response => response.json())
      .then(data => {
        if (!data.erro) {
          document.getElementById('rua').value = data.logradouro || '';
          document.getElementById('cidade').value = data.localidade || '';
          document.getElementById('estado').value = data.uf || '';
        }
      });
  }
});

// Envio do formulário via fetch
document.getElementById('formPessoa').addEventListener('submit', async function (event) {
  event.preventDefault();

  const form = event.target;
  const formData = new FormData(form);

  try {
    const response = await fetch('/add', {
      method: 'POST',
      body: formData
    });

    const message = await response.text();

    if (response.ok) {
      exibirMensagem(message, 'sucesso');
      form.reset();
      setTimeout(() => location.reload(), 1000); // recarrega para atualizar tabela
    } else {
      exibirMensagem(message, 'erro');
    }

  } catch (error) {
    exibirMensagem('Erro ao enviar dados.', 'erro');
  }
});
