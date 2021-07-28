let passWord = 'abcd'
let mainHeader = document.getElementsByClassName('header')
let panel = document.getElementsByClassName('link-nav')
let loginInput = document.getElementsByClassName('in-1')
let invisibleOne = document.getElementsByClassName('success-box')

function formFunction() {
    return null
}
function helpFunc() {
    alert('The pass is "abcd"')
}
function submitForm() {
    if (loginInput[0].value == passWord) {
        invisibleOne[0].style.display = 'block'
        setTimeout(submitTimeout, 1000)
    }
    else if (loginInput[0].value == '') {
        alert("Username can't be blank!")
        loginInput[0].value == ''
    }
    else {
        alert('Incorrect Username!')
    }
}
function submitTimeout() {
    // alert('Username Valid!')
    window.location = 'home.html'
}

