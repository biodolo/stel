(function($, key_field, key_type, form_id, submit_check) {

	var form_val = new Array();
	var selected_key = false;

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

	$(document)
			.ready(
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
							$('#'+form_id).submit(submit_check($));
					});

})(
		django.jQuery, 
		[ 'id_apparecchio', 'id_utente' ], 
		{
			'id_apparecchio' : 'Apparecchio',
			'id_utente' : 'Cliente'
		},
		'schedaritiro_form',
		function($) {
			return function(){
				if ($('#id_garanzia').is(':checked')){
					// se viene indicato che l'apparecchio è in garanzia
					if ($("#id_data_acquisto").val()==''){
						alert('Indicare data di acquisto');
						$("#id_data_acquisto").focus();
						return false;
					}
					if ($("#id_tipo_prova_acquisto").val()==''){
						alert('Indicare il tipo di prova d\'acquisto');
						$("#id_tipo_prova_acquisto").focus();
						return false;
					}
					//if ($"#)
				}
				return true;
			};
		}
	);