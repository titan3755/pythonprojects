const viewMsg = document.getElementById('view')
const modalMain = document.getElementsByClassName('modal-bg')[0]
const modalClose = document.getElementById('close')
const modalFunction = () => {
    modalMain.classList.add('modal-active')
}
const modalCloseFunction = () => {
    modalMain.classList.remove('modal-active')
}
viewMsg.addEventListener('click', modalFunction)
modalClose.addEventListener('click', modalCloseFunction)