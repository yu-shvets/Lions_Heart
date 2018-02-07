$('document').ready(function(){
  $('.owl-carousel').owlCarousel({
    loop:false,
    margin:10,
    dots: true,
    // responsive:{
    //     0:{
    //         items:1
    //     },
    //     768:{
    //         items:3
    //     },
    //     1000:{
    //         items:3
    //     }
    // }
  })

  //mobile menu
  $('.header__mobile').click(function(){
    $('.header__nav').toggleClass('header__nav_active');
    $('.header__mobile').toggleClass('header__mobile_active');
  });
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
  $('#cart__summ').on('keydown keyup', function(e){
    if ($(this).val() > 100 
        && e.keyCode != 46 // delete
        && e.keyCode != 8 // backspace
       ) {
       e.preventDefault();
       $(this).val(100);
    }
  });
});

(function (){
  var swiper = new Swiper('.swiper-container', {
    effect: 'flip',
    slidesPerView:'auto',
    loop: true,
    autoplay: {
      delay: 5000
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  }); 
})();


// document.getElementById('cart__summ').addEventListener('keyup',function(e){
//     if (e.which == 13) this.blur();
// });