//Import DOM elements
const colors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
const contentBox = document.getElementsByClassName('content-box')
const buttonColor = document.getElementById('color-change')
const hexHeader = document.getElementById('hex-header')
const hexValue = document.getElementById('hex-value')
const mainBody = document.body

const buttonFunction = () => {
    setTimeout(function () {
        buttonColor.textContent = 'Change background!'
        buttonColor.style.background = 'red'
        buttonColor.style.padding = '10px'
        buttonColor.style.border = '3px #000000 solid'
        buttonColor.style.width = '550px'
    }, 100)

}
const buttonFunctionOut = () => {
    setTimeout(function () {
        buttonColor.textContent = 'Click to change background!'
        buttonColor.style.background = '#00519c'
        buttonColor.style.padding = null
        buttonColor.style.border = null
        buttonColor.style.width = '550px'
    }, 100)

}
const randomizerColor = () => {
    let colorHexOne = colors[Math.floor(Math.random() * colors.length)]
    let colorHexTwo = colors[Math.floor(Math.random() * colors.length)]
    let colorHexThree = colors[Math.floor(Math.random() * colors.length)]
    let colorHexFour = colors[Math.floor(Math.random() * colors.length)]
    let colorHexFive = colors[Math.floor(Math.random() * colors.length)]
    let colorHexSix = colors[Math.floor(Math.random() * colors.length)]

    let finalHex = '#' + colorHexOne + colorHexTwo + colorHexThree + colorHexFour + colorHexFive + colorHexSix
    console.log(finalHex);
    return finalHex
}
const inverter = (hex) => {
    let invert = '#' + (Number(`0x1${hex}`) ^ 0xFFFFFF).toString(16).substr(1).toUpperCase()
    console.log(invert); 
    return invert
}

const colorClick = () => {
    let randomHex = randomizerColor()
    let invertedColor = inverter(toString(randomHex))
    mainBody.style.background = randomHex
    hexValue.textContent = randomHex
    hexValue.style.color = invertedColor
    console.log(invertedColor)
    console.log(randomHex)
}


