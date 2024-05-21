// on updating data
$("#update").click(function () {
    $("input").each(function (el) {
        
            $(this).removeAttr('readonly');
            
        // console.log("abeer");
    })
})

// on saving data 
$("#save").click(function () {
    $("input").each(function (el) {

        $(this).attr('readonly', 'true');
            
        // console.log("abeer");
    })
})