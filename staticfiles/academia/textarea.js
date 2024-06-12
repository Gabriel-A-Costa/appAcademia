document.addEventListener('DOMContentLoaded', function () {
  const messageInput = document.querySelector('textarea[name="message"]')
  const charCount = document.getElementById('charCount')
  const maxLength = parseInt(messageInput.getAttribute('maxlength'))

  // Função para atualizar a contagem de caracteres restantes
  function updateCharCount() {
    const currentLength = messageInput.value.length
    const remaining = maxLength - currentLength
    charCount.textContent = `${remaining} caracteres restantes`
  }

  // Atualizar a contagem ao carregar a página com o valor inicial
  updateCharCount()

  // Atualizar a contagem ao digitar
  messageInput.addEventListener('input', updateCharCount)
})
