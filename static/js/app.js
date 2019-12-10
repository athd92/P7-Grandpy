let content = false;

$(document).ready(function(){
        $('#reloadMessage').hide();
        $('#newSearch').hide();
        $('#elements').hide();  
        $('#notFound').hide();
        $('#getData').on('click', function(){  // send ajax          
            send_ajax_request();        
    });
});

$(document).on('keypress',function(e) { // listen enter key
    if(e.which == 13) {
        if($('#message').val() == ""){
            alert('Aucune demande??')
        }else if($('#message').val().length < 3){
            alert('Moins de trois lettres??')
        }else{
            send_ajax_request();
        }        
    }
});

$('#newSearch').click(function(){   // reload page for new search
    location.reload();
    $('#message').val('');
})

function initMap(latitude, longitude){  // initialisation of googlemaps    

    // map options    
    var options = {
        zoom:10,
        center:{lat: latitude, lng: longitude},
    }    

    // new map
    var map = new google.maps.Map(document.getElementById('map'), options);   

    // add marker
    var marker = new google.maps.Marker({
        position:{lat: latitude, lng: longitude},
        map:map
    });
};


function display_map(latitude, longitude){    // setting render on DOM
        $('#elements').fadeIn(5000);          
        $('.divmap').append('<div id="map"></div>');
        $('.divmap').hide();
        $('.divstory').fadeIn(1000);
        $('.divmap').fadeIn(1000);                       
        initMap(latitude, longitude);        
    };
    


function send_ajax_request(){   // the ajax request function

    let entry = {
        message: $('#message').val(),
    };

    $.ajax({                    // ajax request from input data
        type:'POST',
        url:`${window.origin}/entry`,
        data:JSON.stringify(entry),            
        contentType: 'application/json;charset=UTF-8',

        beforeSend:function(){            
            $('#loader img').show();
        },

        complete:function(){
            $('#loader img').hide();
        },

        success:function(data){      
            if(content == false){       // no city understand by googlemaps
                if(data.localisation == 'no localisation possible'){
                    $('#getData').hide();
                    $('#reloadMessage').show();
                    $('#notFound').show();
                    $('#newSearch').show();
                }
                else{                
                    console.log(data);   // success request display maps
                    $('#getData').hide();
                    $('#newSearch').show();
                    $('.divstory').append('<div id="mess"><p>' + data.data + '</p></div>');   
                    display_map(data.localisation.lat, data.localisation.lng);
                    content = true;
                }
            }else{

            }
        },

        error:function(e){
            console.error(e);
            if(content == false){
                $('#getData').hide();
                $('#reloadMessage').show();
                $('#notFound').show();
                $('#newSearch').show();
                content = true;                
            }                
        }
   });
};