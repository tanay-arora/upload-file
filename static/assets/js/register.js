(function($) {
    "use strict";

    jQuery(document).ready(function($) { // wait until the document is ready

        $('#register_send').on('click', function(e) { 
            e.preventDefault();
            $('.error').fadeOut('slow'); 
            var error = false;
            // get input data
            const rtype = $('input#rtype').val();
            const rcompany_name = $('input#rcompany_name').val();
            const rtotal_employees = $('input#rtotal_employees').val();
            const rcompany_category = $('input#rcompany_category').val();
            const rindustry = $('input#rindustry').val();
            const rwhere_you_know = $('select#rwhere_you_know').val();
            const rshowcasing_product = $('select#rshowcasing_product').val();
            const rcu_passout = $('select#rcu_passout').val();
            const rhiring_interns = $('select#rhiring_interns').val();
            const rhiring_professionals = $('select#rhiring_professionals').val();
            const rdescribe_one_sentence = $('textarea#rdescribe_one_sentence').val();
            const rcore_problem = $('textarea#rcore_problem').val();
            const rbiggest_competitors = $('textarea#rbiggest_competitors').val();
            const rwhy_unique = $('textarea#rwhy_unique').val();
            const rraise_capital = $('textarea#rraise_capital').val();
            const rincubator_program = $('input#rincubator_program').val();
            const rhave_revenue = $('select#rhave_revenue').val();
            const ris_proprietary = $('select#ris_proprietary').val();
            const rname = $('input#rname').val();
            const remail = $('input#remail').val();
            const rmobile = $('input#rmobile').val();
            const rgender = $('select#rgender').val();
            const rcountry = $('input#rcountry').val();
            const rtshirt_size = $('select#rtshirt_size').val();
            const rcollege = $('input#rcollege').val();
            const rlinkedin = $('input#rlinkedin').val();
            // validators variables
            const email_compare = /^([a-z0-9_.-]+)@([da-z.-]+).([a-z.]{2,6})$/;
            console.log(rwhere_you_know)
            // validators conditions
            if(!rcompany_name?.length){ $('#err-rcompany_name').fadeIn('slow'); error=true;}
            if(!rtotal_employees?.length){ $('#err-rtotal_employees').fadeIn('slow'); error=true;}
            if(!rwhere_you_know?.length){ $('#err-rwhere_you_know').fadeIn('slow'); error=true;}
            if(!rshowcasing_product?.length){ $('#err-rshowcasing_product').fadeIn('slow'); error=true;}
            if(!rcu_passout?.length){ $('#err-rcu_passout').fadeIn('slow'); error=true;}
            if(!rhiring_interns?.length){ $('#err-rhiring_interns').fadeIn('slow'); error=true;}
            if(!rhiring_professionals?.length){ $('#err-rhiring_professionals').fadeIn('slow'); error=true;}
            if(!rdescribe_one_sentence?.length){ $('#err-rdescribe_one_sentence').fadeIn('slow'); error=true;}
            if(!rcore_problem?.length){ $('#err-rcore_problem').fadeIn('slow'); error=true;}
            if(!rbiggest_competitors?.length){ $('#err-rbiggest_competitors').fadeIn('slow'); error=true;}
            if(!rwhy_unique?.length){ $('#err-rwhy_unique').fadeIn('slow'); error=true;}
            if(!rraise_capital?.length){ $('#err-rraise_capital').fadeIn('slow'); error=true;}
            if(!rincubator_program?.length){ $('#err-rincubator_program').fadeIn('slow'); error=true;}
            if(!rhave_revenue?.length){ $('#err-rhave_revenue').fadeIn('slow'); error=true;}
            if(!ris_proprietary?.length){ $('#err-ris_proprietary').fadeIn('slow'); error=true;}
            if(!rname?.length){ $('#err-rname').fadeIn('slow'); error=true;}
            if(!remail?.length){ $('#err-remail').fadeIn('slow'); error=true;}
            if(!email_compare.test(remail)){ $('#err-remail-nvalid'); error=true;}
            if(!rmobile?.length){ $('#err-rmobile').fadeIn('slow'); error=true;}
            if(!rcountry?.length){ $('#err-rcountry').fadeIn('slow'); error=true;}
            if(!rgender?.length){ $('#err-rgender').fadeIn('slow'); error=true;}
            if(!rtshirt_size?.length){ $('#err-rtshirt_size').fadeIn('slow'); error=true;}
            if(!rcollege?.length){ $('#err-rcollege').fadeIn('slow'); error=true;}
            if(!rlinkedin?.length){ $('#err-rlinkedin').fadeIn('slow'); error=true;}

                
                var data_string = $('#registration_form').serialize(); // Collect data from form
                const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
                const purl = 'api/form/register_startup';
                // if(rtype == 'startup') purl = 'api/form/register_startup';
                // else if(rtype == 'attende') purl = 'api/form/register_attende';
                $.ajax({
                    type: "POST",
                    url: purl,
                    headers: {'X-CSRFToken': csrftoken},
                    mode: 'same-origin',
                    data: data_string,
                    error: function(request, error) {
                            $('#err-state').slideDown('slow');
                            $("#err-state").html('An error occurred: ' + error + '');
                    },
                    success: function(req) {
                        if(req.success){
                        }
                        if(req.error) $("#err-state").html(req.error);
                    }
                });
                return false; 
            
        }); 
    });

})(jQuery);