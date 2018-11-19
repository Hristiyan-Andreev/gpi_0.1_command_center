src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"

 $(document).ready(function() {
        $('form').submit(function (e) {
			// var form_id = $(this).attr('id')
			// var url = "{{ url_for(${form_id}) }}"; // send the form data here
            var url = "{{ url_for('form') }}"; // send the form data here.
            $.ajax({
                type: "POST",
                url: url,
                data: $('form').serialize(), // serializes the form's elements.
                success: function (data) {
                    console.log(data)  // display the returned data in the console.
                }
            });
            e.preventDefault(); // block the traditional submission of the form.
        });
        // Inject our CSRF token into our AJAX request.
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", "{{ form.csrf_token._value() }}")
                }
            }
        })
    });