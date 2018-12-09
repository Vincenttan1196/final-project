$(document).ready(function() {
    $('#content').load('content/Weekly.php');


    //handle menu clicks

    $('button.dropbtn li a').click(function() {
        var page = $(this).attr('href');
        $('#content').load('../content/'+ page + '.php');
        return false;
    });
});