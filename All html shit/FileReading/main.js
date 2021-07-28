const fs = require('fs');

console.log('start');
fs.readFile('./subfolder/testfolder/akij.txt', 'utf8', (err, data) => {
    if (err) {
        return null
    }
    console.log('weed');
    console.log(data);
})
fs.writeFile('./subfolder/testfolder/akij.txt', 'Aho Vatija Aho!', (err, data) => {
    if (err) {
        console.log('Error Occured!');
        return null
    }
    console.log(data);
    console.log('Middle');
});
console.log('End');