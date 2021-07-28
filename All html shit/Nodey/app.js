const names = require('./primary')
const functionFile = require('./functions')
const alter = require('./alternative')
const exportsTesting = require('./exportTest')
console.log(functionFile);

const myData = require('./data')
console.log(myData[3].weight);

functionFile(names.akij)
functionFile(names.ganza)
functionFile(names.str1)
functionFile(names.str2)
functionFile(names.secret)
console.log(exportsTesting.v1);


console.log(alter.list);
console.log(alter.email);

