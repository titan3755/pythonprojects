const temp = document.getElementById('temp');
const pres = document.getElementById('pres')
const dist = document.getElementById('dist')
const area = document.getElementById('area')
const vol = document.getElementById('vol')
const weight = document.getElementById('weight')
const conFrom = document.getElementById('con-from')
const conTo = document.getElementById('con-to')
const mainInput = document.getElementById('num')
const submitBtn = document.getElementById('submit')

const converterFunction = (buttonId) => {
    conFrom.textContent = ''
    conTo.textContent = ''
    conFrom.innerHTML = ''
    conTo.innerHTML = ''
    switch (buttonId) {
        case 0:
            conFrom.innerHTML = 
            `
            <option value="celsius">Celsius</option>
            <option value="fahrenheit">Fahrenheit</option>
            <option value="kelvin">Kelvin</option>
            <option value="reaumur">Réaumur</option>
            <option value="rankine">Rankine</option>
            `
            conTo.innerHTML = 
            `
            <option value="celsius">Celsius</option>
            <option value="fahrenheit">Fahrenheit</option>
            <option value="kelvin">Kelvin</option>
            <option value="reaumur">Réaumur</option>
            <option value="rankine">Rankine</option>
            `
            break
        case 1:
            conFrom.innerHTML = 
            `
            <option value="pascal">Pascal</option>
            <option value="atm">Atmosphere</option>
            <option value="bar">Bar</option>
            <option value="psi">PSI</option>
            <option value="inhg">inHg</option>
            <option value="mmHg">mmHg</option>
            <option value="inh2o">inH<sub>2</sub>O</option>
            <option value="torr">Torr</option>
            `
            conTo.innerHTML = 
            `
            <option value="pascal">Pascal</option>
            <option value="atm">Atmosphere</option>
            <option value="bar">Bar</option>
            <option value="psi">PSI</option>
            <option value="inhg">inHg</option>
            <option value="mmHg">mmHg</option>
            <option value="inh2o">inH<sub>2</sub>O</option>
            <option value="torr">Torr</option>
            `
            break
        case 2:
            conFrom.innerHTML = 
            `
            <option value="meter">Meter</option>
            <option value="mile">Mile</option>
            <option value="yard">Yard</option>
            <option value="foot">Foot</option>
            <option value="inch">Inch</option>
            <option value="ly">Light Year</option>
            `
            conTo.innerHTML = 
            `
            <option value="meter">Meter</option>
            <option value="mile">Mile</option>
            <option value="yard">Yard</option>
            <option value="foot">Foot</option>
            <option value="inch">Inch</option>
            <option value="ly">Light Year</option>
            `
            break
        case 3:
            conFrom.innerHTML =
            `
            <option value="sqmt">Square Meter</option>
            <option value="sqkm">Square Kilometer</option>
            <option value="sqcm">Square Centimeter</option>
            <option value="sqmm">Square Milimeter</option>
            <option value="sqmc">Square Micrometer</option>
            <option value="hectare">Hectare</option>
            <option value="sqmi">Square Mile</option>
            <option value="sqyd">Square Yard</option>
            <option value="sqft">Square Foot</option>
            <option value="sqin">Square Inch</option>
            <option value="acre">Acre</option>
            `
            conTo.innerHTML = 
            `
            <option value="sqmt">Square Meter</option>
            <option value="sqkm">Square Kilometer</option>
            <option value="sqcm">Square Centimeter</option>
            <option value="sqmm">Square Milimeter</option>
            <option value="sqmc">Square Micrometer</option>
            <option value="hectare">Hectare</option>
            <option value="sqmi">Square Mile</option>
            <option value="sqyd">Square Yard</option>
            <option value="sqft">Square Foot</option>
            <option value="sqin">Square Inch</option>
            <option value="acre">Acre</option>
            `
            break
        case 4:
            conFrom.innerHTML =
            `
            <option value="cumt">Cubic Meter</option>
            <option value="cukm">Cubic Kilometer</option>
            <option value="cucm">Cubic Centimeter</option>
            <option value="cumm">Cubic Milimeter</option>
            <option value="liter">Liter</option>
            <option value="ml">Mililiter</option>
            <option value="cumi">Cubic Mile</option>
            <option value="cuyd">Cubic Yard</option>
            <option value="cuft">Cubic Foot</option>
            <option value="cuin">Cubic Inch</option>
            `
            conTo.innerHTML =
            `
            <option value="cumt">Cubic Meter</option>
            <option value="cukm">Cubic Kilometer</option>
            <option value="cucm">Cubic Centimeter</option>
            <option value="cumm">Cubic Milimeter</option>
            <option value="liter">Liter</option>
            <option value="ml">Mililiter</option>
            <option value="cumi">Cubic Mile</option>
            <option value="cuyd">Cubic Yard</option>
            <option value="cuft">Cubic Foot</option>
            <option value="cuin">Cubic Inch</option>
            `
            break
        case 5:
            conFrom.innerHTML =
            `
            <option value="kg">Kilogram</option>
            <option value="g">Gram</option>
            <option value="mg">Miligram</option>
            <option value="mt">Metric Ton</option>
            <option value="lt">Long Ton</option>
            <option value="st">Short Ton</option>
            <option value="lb">Pound</option>
            <option value="oz">Ounce</option>
            <option value="crt">Carrat</option>
            <option value="amu">Atomic Mass Unit</option>
            `
            conTo.innerHTML =
            `
            <option value="kg">Kilogram</option>
            <option value="g">Gram</option>
            <option value="mg">Miligram</option>
            <option value="mt">Metric Ton</option>
            <option value="lt">Long Ton</option>
            <option value="st">Short Ton</option>
            <option value="lb">Pound</option>
            <option value="oz">Ounce</option>
            <option value="crt">Carrat</option>
            <option value="amu">Atomic Mass Unit</option>
            `
            break
        default:
            console.log('Something went wrong!')
            break
    }
}




// const calculations = (btnId) => {
//     switch (btnId) {
//         case 0:
            
//             break
//         case 1:
        
//             break
//         case 2:

//             break
//         case 3:
        
//             break
//         case 4:

//             break
//         case 5:

//             break
//         default:
//             break
//     }
// }


temp.addEventListener('click', () => {
    converterFunction(0)
    
})
pres.addEventListener('click', () => {
    converterFunction(1)
    
})
dist.addEventListener('click', () => {
    converterFunction(2)
    
})
area.addEventListener('click', () => {
    converterFunction(3)
    
})
vol.addEventListener('click', () => {
    converterFunction(4)
    
})
weight.addEventListener('click', () => {
    converterFunction(5)
    
})
