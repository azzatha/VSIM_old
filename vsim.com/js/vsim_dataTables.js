
var filename = $('#myscript').attr("filename");
alert(filename)
$('#table_id').dataTable( {
  "ajax": {
        url: "https://raw.githubusercontent.com/azaa21/ideogramTest/master/positions.json",
        "cache": true,
        "dataSrc": function ( json ) {
            var return_data=[];
            
            $.each(json.annots, function() {
                console.log(this);
                var chr=this.chr;
                $.each(this.annots, function() {
                    var name=this[0].split("<br />");
                    //console.log(name);
                    return_data.push([chr, this[1] , name[0]+"</br>"+name[1]+"</br>"+name[3],name[2].split(":")[1]]);
                });
                
            });
      return return_data;
    }
  }
} );