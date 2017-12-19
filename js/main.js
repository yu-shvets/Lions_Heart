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
	
});