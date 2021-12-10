function add(input){

    var dict = JSON.parse(window.localStorage.getItem('current'));

    if(dict != null){
        if(dict['message'] != null){  
            s = String(dict['message']);
            if(String(s).endsWith(' ')){
                dict['message'] = dict['message'] + input + " "; 
            }else{
                dict['message'] = dict['message'] + " " +input + " "; 
            }
           
        }else{
            dict['message'] = input+" ";
        }
    }else{
        dict = {};
        dict['message'] = input + " ";
    }


    window.localStorage.setItem('current', JSON.stringify(dict));
}
function addL(input){

    var dict = JSON.parse(window.localStorage.getItem('current'));

    if(dict != null){
        if(dict['message'] != null){  
       
         
            dict['message'] = dict['message'] + input; 
        }else{
            dict['message'] = input;
        }
    }else{
        dict = {};
        dict['message'] = input;
    }


    window.localStorage.setItem('current', JSON.stringify(dict));
}