// :filename: ajacs/static/js/ajacs.js

// Display a debug message in console
function debug(msg) {
    console.log(msg);
}

// peek up the voice indicated by the user in the "nation" selection
//   ... and post it to web server
function chk_nation(){
    debug('> chk_nation');
    var select_box = document.getElementById("nation");
    var selected_value = select_box.options[select_box.selectedIndex].value;
    postJSON($SCRIPT_ROOT+'_get_nation_data',
             selected_value,
             set_nation_values);
}

// get response from web server, parse it and inject it in "txt_par"
function set_nation_values(r){
    debug('> set_nation_values(' + r +')');
    v = parse_response(r);
    var txt_par = document.getElementById('nation_values');
    txt_par.innerHTML = v;
}

// parsing server response
function parse_response(response){
    debug('>parse_request(' + response + ')')
    if (response.readyState === 4 && response.status === 200) {
        var type = response.getResponseHeader("Content-Type");    // Get the type of the response
        if (type.indexOf("xml") !== -1 && response.responseXML)   // Check type 
            return response.responseXML;                          //   Document response
        else if (type === "application/json")
            return JSON.parse(response.responseText);             //   JSON response
        else
            return response.responseText;
    }
}

// posting data to web server as JSON
function postJSON(url, data, callback) {
    debug('> postJSON(' + url + ', ' + data + ', ' + callback.name + ')')
    var request = new XMLHttpRequest();
    request.open("POST", url);                        // POST to the specified url
    request.onreadystatechange = function() {         // Simple event handler
        if (request.readyState === 4 && callback)     // When response is complete ...
            callback(request);                        // ... call the callback.
    };
    request.setRequestHeader("Content-Type", "application/json");
    request.send(JSON.stringify(data));
}

// hook chk_nation to "nation" select
document.getElementById("nation").onchange = chk_nation;

