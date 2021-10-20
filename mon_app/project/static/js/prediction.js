$(document).ready(function(){
    $('.item').on('click',function(){
        console.log("item clicked");
        var data_item = $(this).data('item');
        var lead_time = $(this)
        console.log(data_item);
        var value = {'id': JSON.stringify(data_item)};

      $.ajax({

        type: "POST",
        url : "/predictions_test",
        // data: {'data_item':data_item},
        data: JSON.stringify(data_item),
        contentType: "application/json; charset=utf-8",

      //   success: function(response) {
      //   // window.location.replace('/predictions_test');
      //   console.log("item sent");
      //   // document.location.href='/predictions';
      //  },
      });   

   });
 });

