$( document ).ready(function() {
    $("a").click(function(event){
        event.preventDefault();
        href = $(this).attr("href");

       $.get( href + "",  function( data ) {
             $("#content_area").html(data);
        });


    });
});