document.addEventListener('DOMContentLoaded', function(){
  // Example: smooth scroll to quote page if exists in nav
  const quoteBtn = document.querySelector('.btn-cta[href$="quote/"]');
  if(quoteBtn){
    quoteBtn.addEventListener('click', function(e){
      // default behaviour OK: it navigates to form page
    });
  }
});
