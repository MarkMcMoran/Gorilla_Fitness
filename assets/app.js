document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var options;
    var instances = M.Sidenav.init(elems, options);
  });



  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.carousel');
    var options =({

        indicators: true
      });
            
    var instances = M.Carousel.init(elems, options);
  });

  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var options;
    var instances = M.FormSelect.init(elems, options);
  });