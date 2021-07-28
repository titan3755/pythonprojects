let passWord = 'pass'
let passW = prompt('Enter pass: ')
if (passW.toLowerCase() == passWord) {
    window.location = 'index.html'
}
else{
    window.location = 'incorrectPass.html'
}

