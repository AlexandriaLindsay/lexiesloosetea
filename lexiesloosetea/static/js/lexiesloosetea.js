jQuery(document).ready(function($) {

    window.onload = function(){
        if(window.innerWidth >= 992) {
          var rellax = new Rellax('.rellax', {opt: 1});
        }
    }

    $('.slick-carousel').slick({
      arrows: true,
      centerPadding: "0px",
      dots: true,
      slidesToShow: 3,
      infinite: true
    });

    $('.test-carousel').slick({
      arrows: false,
      centerPadding: "0px",
      dots: true,
      slidesToShow: 1,
      infinite: true
    });

    $('.product-carousel').slick({
      arrows: true,
      centerPadding: "0px",
      dots: true,
      slidesToShow: 4,
      infinite: true
    });


//*** Smooth Scroll ***
  $(function() {
    $('a[href*="#"]:not([href="#"])').click(function() {
      if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
        if (target.length) {
          $('html, body').animate({
            scrollTop: target.offset().top - 70
          }, 1000);
          return false;
        }
      }
    });
  });//End Smooth Scroll


//*** Scroll to Top *** use with less *** use with html ***
  $(window).scroll(function() {
      if ($(this).scrollTop() >= 50) {        // If page is scrolled more than 50px
          $('#return-to-top').fadeIn(200);    // Fade in the arrow
      } else {
          $('#return-to-top').fadeOut(200);   // Else fade out the arrow
      }
  });

  $('#return-to-top').click(function() {      // When arrow is clicked
      $('body,html').animate({
          scrollTop : 0                       // Scroll to top of body
      }, 500);
  });//End Scroll to Top

  $('#toggle').click(function() {
    $(this).toggleClass('active');
    $('#overlay').toggleClass('open');
   });
 
 
 // Closes overlay menu after clicking on the menu link
   $('#site-navigation3 ul li a').on("click", function (e) {
   $('#toggle').click();
 });

 $(function() {
  if (typeof Storage != "undefined") {
    if (!localStorage.getItem("done")) {
      setTimeout(function() {
        document.getElementById('modal-content').style.display = 'block';
      }, 3000);
    }
    localStorage.setItem("done", true);
  }
});

$('.close').click(function() {
  document.getElementById('modal-content').style.display = 'none';
});
 


});