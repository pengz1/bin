"use strict"
var http = require('http');
var url = require('url');

http.createServer(function (request, response) {
    response.writeHead(200, {'Content-Type': 'text/plain'});
    response.end('Hello World\n');
    var pathName= url.parse(request.url).pathname;
    console.log(pathName);
    console.log(request.headers);
    console.log(request.method);
    console.log(request.connection.remoteAddress);
}).listen(8080);

console.log('Server running at http://127.0.0.1:8888/');
