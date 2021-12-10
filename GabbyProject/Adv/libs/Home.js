
function Clear(){
    
 
    var dict = {'message':null};
    console.log(dict);
    window.localStorage.setItem('current', JSON.stringify(dict));
}
function Enter(){
    var dict = JSON.parse(window.localStorage.getItem('current'));
  
    if(dict!=null){
        var message = dict['message']
        console.log(message);
    }
    Clear();
}
function Help(){
    console.log("Help is needed");
}
