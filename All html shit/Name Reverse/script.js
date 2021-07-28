const nameInput = document.getElementById('name')
const submitBtn = document.getElementById('submit')
const resultRev = document.getElementById('result')

const reverseFunction = () => {
    let mainValue = nameInput.value.split('').reverse().join().replaceAll(',', '')
    resultRev.textContent = mainValue
}
submitBtn.addEventListener('click', reverseFunction)