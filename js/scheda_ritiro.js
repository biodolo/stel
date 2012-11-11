(function($){
	var form_val = new Array();
	var selected_key = false;
	var form_readonly = false;
	var key_field=[ 'id_apparecchio', 'id_utente' ];
	var key_type={
			'id_apparecchio' : 'Apparecchio',
			'id_utente' : 'Cliente'
		};
	var form_id='schedaritiro_form';



	function isEmpty(id){
		return $("#"+id).val()=='';
	}
	
	function isChecked(id){
		return $("#"+id).is(':checked');
	}
	
	
	function mustFill(id,message){
		if (isEmpty(id)){
			alert(message);
			$("#"+id).focus();
			return true;
		}
		return false;
	}
	
	function mustCheck(id,message){
		if (!isChecked(id)){
			alert(message);
			$("#"+id).focus();
			return true;
		}
		return false;
	}
	
	
	function mostraRelated(id) {
		var value = $('#' + id).val();
		var classe = key_type[id];
		if (value != form_val[id]) {
			form_val[id] = value;
			$.get('/api/get_str/' + classe + '/' + value + '/', function(data) {
				var lookup = $('#lookup_' + id);
				var strong = lookup.nextAll("strong");
				if (strong.length == 0) {
					lookup.after('<strong>&nbsp;</strong>');
					strong = lookup.nextAll("strong");
				}
				strong.text(data);
			});
		}
	}

	function setupRelated(id) {
		var obj = $('#' + id);
		obj.hide();
		form_val[id] = obj.val();
		$('#lookup_' + id).click(function() {
			selected_key = id;
		});
	}

	$(document).ready(
		function() {
			var functionBackup = new Array();
			functionBackup['dismissRelatedLookupPopup'] = dismissRelatedLookupPopup;
			dismissRelatedLookupPopup = function(win, val) {
				functionBackup['dismissRelatedLookupPopup'](win,
						val);
				if (selected_key) {
					mostraRelated(selected_key);
					selected_key = false;
				}
			};
			for (i = 0; i < key_field.length; i++) {
				setupRelated(key_field[i]);
			}
			if (submit_check)
				$('#'+form_id).submit(submit_check);
			if ($('#id_riconsegnato_da').val()!=''){
				form_readonly=true;
			}

		});
	
	function submit_check(){
		if (form_readonly) {
			if (
					(prompt("L'apparecchio e' gia' stato ritirato, inserire la password di conferma")!='qui ci metto la password di conferma')&&
					(prompt("L'apparecchio e' gia' stato ritirato, inserire la password di conferma")!='qui ci metto la password di conferma')&&
					(prompt("L'apparecchio e' gia' stato ritirato, inserire la password di conferma")!='qui ci metto la password di conferma')){
				alert("Impossibile modificare la scheda ritiro, il tentativo e' stato registrato");
				return false;
			}
		}
		if (isChecked('id_garanzia')){
			if (	// APPARECCHIO IN GARANZIA
					mustCheck("id_acquisizione_garanzia","Non e' possibile ritirare apparecchiature in garanzia senza prova d'acquisto") ||
					mustFill("id_data_acquisto","Indicare data di acquisto") ||
					mustFill("id_tipo_prova_acquisto","Indicare il tipo di prova d'acquisto")
				)
			{
				return false;	
			}
		}else{
			// APPARECCHIO FUORI GARANZIA
			if (
					mustFill("id_acconto","Non e' possibile ritirare apparecchiature fuori garanzia senza acconto") ||
					mustFill("id_scontrino_acconto","Indicare il numero dello scontrino dell'acconto")
				)
			{
				return false;	
			}
			if (isChecked("id_preventivo_ok") && mustFill("id_importo_preventivo","Non e' possibile ritirare apparecchiature fuori garanzia senza indicare l'importo del preventivo")){
				return false;
			}			
		}
		if (
				( 
					$('#id_riconsegnato_da').val()!='' &&
					(
							mustFill("id_data_riconsegna","Indicare data di riconsegna") 
					)
				) || ( 
					false
				)
			){
			return false;
		}
		return true;
	}
})(django.jQuery);