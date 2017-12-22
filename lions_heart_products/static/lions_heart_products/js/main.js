$('document').ready(function(){


    $('.owl-carousel').owlCarousel({
    loop:false,
    margin:10,
    dots: true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:3
        }
    }
  })
  var galeries = $("div[id^='gallery']");
  $.each(galeries, function(){
      $('#' + $(this).attr('id')).photobox('a');
  });

    var update_q = $('.update_q');

    update_q.on('input', function(e){

        var form = $(this).parent('form');
        var id = form.attr('id').split('-')[1];

        $.ajax({
            url : form.attr('action'),
            type : "POST",
            data : form.serialize(),

            success: function(json){
                $('#quantity-' + id).text(json.quantity);
                $('#sum-' + id).text(json.sum);
                $('#total_price').text(json.total_price);
            },
            error: function(e){
                console.log(e);
            }
        });

    });


});