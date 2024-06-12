let menuToggle = document.querySelector('.menuToggle')
let sidebar = document.querySelector('.sidebar')
menuToggle.onclick = function () {
  menuToggle.classList.toggle('active')
  sidebar.classList.toggle('active')
}

let Menulist = document.querySelectorAll('.Menulist li')

Menulist.forEach(item =>
  item.addEventListener('click', () => {
    Menulist.forEach(item => item.classList.remove('active'))
    this.classList.add('active')
  })
)
