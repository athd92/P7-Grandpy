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

function initMap(latitude, longitude, data){  // initialisation of googlemaps   
    
    // map options    
    var options = {
        zoom:11,
        center:{lat: latitude, lng: longitude},
    } 
    
    // new map
    var map = new google.maps.Map(document.getElementById('map'), options);   

    // add marker
    var marker = new google.maps.Marker({
        position:{lat: latitude, lng: longitude},
        map:map
    });

    var infowindow = new google.maps.InfoWindow();
    infowindow.setContent(data.address);
    infowindow.open(map, marker);
    

};


function display_map(latitude, longitude, data){    // setting render on DOM
        $('#elements').fadeIn(5000);          
        $('.divmap').append('<div id="map"></div>');
        $('.divmap').hide();
        $('.divstory').fadeIn(1000);
        $('.divmap').fadeIn(1000);                       
        initMap(latitude, longitude, data);        
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
                    $('#message').css({ "opacity": 0.1 });
                    $('#message').prop('disabled', true);
                    $('#getData').hide();
                    $('#reloadMessage').show();
                    $('#notFound').show();
                    $('#newSearch').show();
                }
                else{                
                    $('#message').css({ "opacity": 0.1 }); // success request display maps
                    $('#message').prop('disabled', true);
                    $('#getData').hide();
                    $('#newSearch').show();
                    $('.divstory').append('<div id="mess"><h3>Bien sûr mon poussin... Voici:<br></h3><p>' + data.data + '</p></div>');   
                    display_map(data.localisation.lat, data.localisation.lng, data);
                    content = true;
                }
            }
        },

        error:function(e){            
            if(content == false){
                $('#message').css({ "opacity": 0.1 });
                $('#message').prop('disabled', true);
                $('#getData').hide();
                $('#reloadMessage').show();
                $('#notFound').show();
                $('#newSearch').show();
                content = true;                
            }                
        }
   });
};