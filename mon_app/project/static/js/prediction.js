/*
  prediction.js
  Get data on click on reservations.html 
  and sends them to main.predictions
*/

$(document).ready(function(){
    $('.item').on('click',function(){
        var data_item = $(this).data('item');
        // console.log(data_item);

      $.ajax({

        type: "POST",
        url : "/processing",
        data: JSON.stringify(data_item),
        contentType: "application/json; charset=utf-8",

        success: function(response) {
        window.location.replace('/predictions');
        // document.location.href='/predictions';
        },

      });   

   });
 });

