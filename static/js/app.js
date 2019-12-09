let content = false;

$(document).ready(function(){
        $('#reloadMessage').hide();
        $('#newSearch').hide();
        $('#elements').hide();  
        $('#notFound').hide();
        $('#getData').on('click', function(){
            console.log("click");
            let entry = {
                    message: $('#message').val(),
                };

        $.ajax({                    // ajax request from input data
            type:'POST',
            url:`${window.origin}/entry`,
            data:JSON.stringify(entry),            
            contentType: 'application/json;charset=UTF-8',

            beforeSend:function(){
                console.log("before", entry);
                $('#loader img').show();
            },

            complete:function(){
                $('#loader img').hide();
            },

            success:function(data){      
                if(content == false){                    
                    $('#getData').hide();
                    $('#newSearch').show();
                    $('.divstory').append('<div id="mess"><p>' + data.data + '</p></div>');   
                    
         
                    display_map(data.localisation.lat, data.localisation.lng);
                    content = true;
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
                    console.log(content);
                }                
            }
       });
    });
});

$('#newSearch').click(function(){
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
    


function display_chart(){
    var data = {
        
        labels:["mon", "tue", "wed","thu","fri"],
        series:[15,40,6,10]
    };

    var options = {
        width:800,
        height:600
    };

    var mychart = new Chart.Line('.ct-chart', data, options);
};

display_chart();