const operatingSys = require('os')


const architecture = operatingSys.arch()
const cpu = operatingSys.cpus()
const host = operatingSys.hostname()
const platform = operatingSys.platform()
const release = operatingSys.release()
const totalMem = operatingSys.totalmem()
const nameOs = operatingSys.type()
const user = operatingSys.userInfo()

console.log('test');

module.exports = {architecture, cpu, host, platform, release, totalMem, nameOs, user}

    
    
