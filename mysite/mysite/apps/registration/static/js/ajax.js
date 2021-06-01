

// $(document).ready(function(){
  $(".btn-like").click(function(e){
    e.preventDefault();
    var id = $(this).attr('data-sid');
    var ur = $(this).attr('data-url');
    let csr = $('input[name=csrfmiddlewaretoken]').val();
    // alert(id);
    // alert(ur);
    alert("The paragraph was clicked.");
    let mydata = { sid: id, csrfmiddlewaretoken: csr };
    $.ajax({
        url: ur,
        method: "POST",
        data: mydata,
        success: function(data){
            alert(data);
        }
    });
  });
  // alert("hello");
// });

