(function($){
        var form_val = new Array();
        var key_field = ['id_apparecchio','id_utente'];
        var key_type = ['Apparecchio','Cliente'];

        function mostraRelated(id,classe){
                var value=$('#'+id).val();
        if (value != form_val[id]){
                form_val[id] = value;
                $.get('/api/get_str/'+classe+'/'+value+'/',function(data){
                        var lookup=$('#lookup_'+id);
                        var strong=lookup.nextAll("strong");
                        if (strong.length == 0){
                                lookup.after('<strong>&nbsp;</strong>');
                                strong=lookup.nextAll("strong");
                        }
                                strong.text(data);

                });
        }
        }

    $(document).ready(function(){
        var functionBackup = new Array();
        functionBackup['dismissRelatedLookupPopup']=dismissRelatedLookupPopup;
        dismissRelatedLookupPopup=function(win,val){
            functionBackup['dismissRelatedLookupPopup'](win,val);
            for(i=0;i<key_field.length;i++){
                mostraRelated(key_field[i],key_type[i]);
            }
        };
        for(i=0;i<key_field.length;i++){
                $('#'+key_field[i]).hide();
                form_val[key_field[i]]=$('#'+key_field[i]).val();
        }
    });

})(django.jQuery);