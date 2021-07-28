const http = require('http')
http.createServer(function (req, res){
    res.write('akij')
    res.end()
}).listen(3000, function(err){
    if(err){
        throw err
    }
    else{
        console.log('Success');
    }
})