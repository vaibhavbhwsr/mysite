$(document).ready(function() {

    // Like Post Ajax
    $(".btn-like").click(function(e) {
        e.preventDefault();
        var id = $(this).attr('id');
        var ur = $(this).attr('data-url');
        let csr = $('input[name=csrfmiddlewaretoken]').val();
        // alert(id);
        // alert(ur);
        // console.log("liked button clicked.");
        let mydata = { csrfmiddlewaretoken: csr };
        $.ajax({
            url: ur,
            method: "POST",
            data: mydata,
            dataType: 'json',
            success: function(data) {
                if (data.liked) {
                    // console.log(data)
                    $('#' + id).html('<i class="fas fa-2x fa-thumbs-up" style="color:royalblue;"></i> ' + data.count)
                } else {
                    // console.log(data)
                    $('#' + id).html('<i class="fas fa-2x fa-thumbs-up"></i> ' + data.count)
                }
            },
        });
    });

    // Comment Post Ajax
    $(".button_comment").click(function(e) {
        e.preventDefault();
        // console.log('Button Clicked!')
        let post_id = $(this).attr('data-postId')
        let path = $(this).attr('data-url');
        let csr = $('input[name=csrfmiddlewaretoken]').val();
        let comment = $("#exampleModal_" + post_id).find('textarea').val();
        $.ajax({
            method: 'POST',
            url: path,
            data: { comment_text: comment, csrfmiddlewaretoken: csr },
            dataType: 'json',
            success: function(data) {
                $('#added_comment_' + data.post).html('<h5>' + data.user + '</h5><p>' + data.comment_text + '</p>')
                $('#comment_' + data.post + '_count').html(data.comment_count + ' comments')
                $('#comment_icon_' + data.post).css("color", "royalblue");
                $('#comment_' + data.post + '_icon_count').html(data.comment_count);
                $("#exampleModal_" + post_id).find('textarea').val('');
            },
            error: function(data) {
                alert('Ajax failed!')
            }
        });
    });

    // Create Group Ajax
    $(".button_new_group").click(function(e) {
        e.preventDefault();
        let path = $(this).attr('data-url');
        let csr = $('input[name=csrfmiddlewaretoken]').val();
        let name = $("#exampleModal").find('textarea').val();
        $.ajax({
            method: 'POST',
            url: path,
            data: { name: name, csrfmiddlewaretoken: csr },
            dataType: 'json',
            success: function(data) {
                alert(data.data.name + " group created successfully!");
                $('.add-new-group').prepend('<a class="btn btn-primary btn-lg" href="/group/chat/'+ data.data.name +'/"><h5>'+ data.data.name +'</h5></a>');
                $("#exampleModal").find('textarea').val('');
                $("#exampleModal").modal('hide');
            },
            error: function(data) {
                alert(data.responseJSON.data.name[0] + ' Choose a unique name.')
                $("#exampleModal").find('textarea').val('');
            }
        });
    });
});