

const copyBtns = [...document.getElementsByClassName('copy-btn')]
console.log(copyBtns)

copyBtns.forEach(btn=>btn.addEventListener('click', ()=>{
    console.log('click')
    const color = btn.getAttribute('data-hex')
    console.log(color)
    navigator.clipboard.writeText(color)
    btn.textContent = 'copied image link'
}))

