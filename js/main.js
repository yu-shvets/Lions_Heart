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
  //gallery 
  var galeries = $("div[id^='gallery']");
  $.each(galeries, function(){
      $('#' + $(this).attr('id')).photobox('a'); 
  });
  // plus/minus button
  $(".cart__table-btn").on("click", function() {
    var $button = $(this);
    var $input = $button.closest('.cart__table-quantity').find(".cart__table-result");
    $input.val(function(i, value) {
      return +value + (1 * +$button.data('step'));
    });
  });
});