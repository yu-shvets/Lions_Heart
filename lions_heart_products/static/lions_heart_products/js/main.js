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

  $('#cart__summ').on('keydown keyup', function(e){
    if ($(this).val() > 100
        && e.keyCode != 46 // delete
        && e.keyCode != 8 // backspace
       ) {
       e.preventDefault();
       $(this).val(100);
    }
  });

  $('.product__button_cart').on('click', function(){
    var img = $(this).parent().parent().find('.product__link').find('.product__img'),
        imgWidth = img.width(),
        cart = $('.cart__length');

    img.clone().css({
      'width': imgWidth,
      'position': 'absolute',
      'z-index': '9999',
      top: img.offset().top,
      left: img.offset().left
    }).appendTo('body').animate({
      opacity: 0.05,
      left: cart.offset()['left'],
      top: cart.offset()['top'],
      width: 20
    }, 1000, function() {
      $(this).remove();
    })
  })

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

