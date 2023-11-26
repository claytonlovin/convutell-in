document.addEventListener('DOMContentLoaded', function() {

  (function($) {
    "use strict";

    var isMenuHidden = localStorage.getItem('isMenuHidden') === 'true';

    if (isMenuHidden) {
      $("body").addClass("sidebar-toggled");
      $(".sidebar").addClass("toggled");
    }

    $("#sidebarToggle, #sidebarToggleTop").on('click', function(e) {
      isMenuHidden = !isMenuHidden;

      localStorage.setItem('isMenuHidden', isMenuHidden);

      $("body").toggleClass("sidebar-toggled", isMenuHidden);
      $(".sidebar").toggleClass("toggled", isMenuHidden);

      if (isMenuHidden) {
        $('.sidebar .collapse').collapse('hide');
      };
    });

    $(window).resize(function() {
      if ($(window).width() < 768) {
        $('.sidebar .collapse').collapse('hide');
      };

      if ($(window).width() < 480 && !isMenuHidden) {
        $("body").addClass("sidebar-toggled");
        $(".sidebar").addClass("toggled");
        $('.sidebar .collapse').collapse('hide');
      };
    });

    $('body.fixed-nav .sidebar').on('mousewheel DOMMouseScroll wheel', function(e) {
      if ($(window).width() > 768) {
        var e0 = e.originalEvent,
          delta = e0.wheelDelta || -e0.detail;
        this.scrollTop += (delta < 0 ? 1 : -1) * 30;
        e.preventDefault();
      }
    });

    $(document).on('scroll', function() {
      var scrollDistance = $(this).scrollTop();
      if (scrollDistance > 100) {
        $('.scroll-to-top').fadeIn();
      } else {
        $('.scroll-to-top').fadeOut();
      }
    });

    $(document).on('click', 'a.scroll-to-top', function(e) {
      var $anchor = $(this);
      $('html, body').stop().animate({
        scrollTop: ($($anchor.attr('href')).offset().top)
      }, 1000, 'easeInOutExpo');
      e.preventDefault();
    });

  })(jQuery);
});
