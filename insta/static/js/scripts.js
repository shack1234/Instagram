$(".clickme").click(function () {
  $(".hideme").toggle();
  $(".showme").toggle();
});

$(".clickcomment").click(function () {
  $(".showcomment").toggle();
  $(".showme").toggle();
});
