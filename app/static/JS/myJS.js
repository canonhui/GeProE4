$(document).ready(function() {
    $('li.active').removeClass('active');
    current_path = '/' + location.pathname.split('/')[1];
    $('a[href="' + current_path + '"]').closest('li').addClass('active');
    
    if(location.pathname == '/') {
        $('a[href="/index"]').closest('li').addClass('active');
    }


    $('.affiche-div').on('click', '.group-link', function(){
        var info = $(this).attr('id').split('link-')[1];
        var page_height = $(document).height(); //html page height
        $('.fond').css('height', page_height);
        var position = $(this).offset().top;
        $('.UI').css('margin-top', position);
        $('#' + info).fadeIn(300);
    });
    
    var $complet = $('td.complet:contains("Complet")').parent();
    $complet.css('color', 'grey');
    $complet.find('input[type=radio]').attr('disabled', true);

    $('tr.attribue').css('color', 'grey');
    $('tr.attribue').find('input[type=radio]').attr('disabled', true);
    $('tr.attribue').find('select').attr('disabled', true);

    /*
    $('.btnEdit_pic_info').click(function(){
        $('#edit_pic_info').fadeIn(700);
    });
    */
    $('#btnName_modify').click(function(){
        $('#name_modify').fadeIn(700);
    });

    $('#btnPassword_modify').click(function(){
        $('#password_modify').fadeIn(700);
    });

    $('#btnEmail_modify').click(function(){
        $('#email_modify').fadeIn(700);
    });

    $('#btnUnregister').click(function(){
        $('#unregister').fadeIn(700);
    });
/*
    $(function(){
        $(".btnEdit_album img").bind("click",function(){
            //this就是当前点击的对象
            var idAlbum = $(this).attr("id");
            //alert('#'.concat(win));
            $('#edit_album [action]').attr("action", "user_manage.php?idAlbum=".concat(idAlbum));
            $('#edit_album').fadeIn(700);
        })
    })

    $(function(){
        $(".btnEdit_pic_info").bind("click",function(){
            $('#edit_pic_info').fadeIn(700);
            //this就是当前点击的对象
            var idPicture = $(this).attr("id");
            //alert(idPicture);
            $('#edit_pic_info [action]').attr("action", "user_manage.php?idPicture=".concat(idPicture));
        })
    })
*/
    // UI BOUTONS INSCRIP/CONNECTION
    $('.affiche-div').on('click', '.fond', function(){
        $(this).parent().fadeOut(300);
    });
    $('.affiche-div').on('click', '.UI', function(e){
        e.stopPropagation();
    });

    //BOUTON DECONNECTION
    $('#btnDeconnection').click(function(){
    	window.location = "deconnection.php";
    });

});