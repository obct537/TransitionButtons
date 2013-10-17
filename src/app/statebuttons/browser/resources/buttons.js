(function($) {
    $(document).ready(function() {

        // If the info viewlet isn't here, 
        // stop right away.
        if( $('#js_info').length < 1 )
        {
            return 0;
        }

        // This is needed since some URL's end in a slash,
        // and some don't
        function stripSlash(url) {
            if(url.substr(-1) == '/') {
                return url.substr(0, url.length - 1);
            }
            else
            {
                return url;
            }
        }

    	var base = stripSlash($("base").attr("href"));

        //Since this is referring to links generated internally, and not by a theme,
        //this shouldn't change anytime soon.
        var modify_url_string = "/content_status_modify?workflow_action=";

        //This works by grabbing every <a> that has an href matching the 
        //URI corresponding to the transition state methods
        var transitions = $("a[href^='" + base + modify_url_string + "']");
        var allowed_transitions = jQuery.parseJSON( $("#allowedTransitions").text() );

    	var buttons = [];
        var allowed = [];
        var transitionClassNames = [];

        var stateDescription = $("#stateDescription").text();
        var state = $('#wfState').text();
        var pageElement = '';
        var editUrl = $('a[href="' + base + '/edit"]');

        // Makes sure the pageElement property is set
        if( $('#pageElement').text() )
        {
            var name = $('#pageElement').text();

            // Checks the user-inputted page element
            if( $(name).length != 0 )
            {
                pageElement = $(name);
            }
            else
            {
                pageElement = $('#portal-breadcrumbs');
            }
        }        
        else
        {
            pageElement = $('#portal-breadcrumbs');
        }

        $(allowed_transitions).each(function() {
            allowed.push(base + modify_url_string + this);
        });

    	transitions.each(function() {

    		// if statement checks that the links text is allowed
    		if( $.inArray($(this).attr('href'), allowed) >= 0 )
    		{
                buttons.push( this );
    		}
    	});

        if( $(editUrl).length > 1 )
        {
            buttons.push($(editUrl));
        }

        if( buttons.length < 1 )
        {
            return 0;
        }



        var html ="<div id='transitionButtons'>";

        html = html + 
        '<h3>State: <span class="stateTitle" >' + state +'</span></h3>' +
        '<p class="tbText">' + stateDescription + '</p>' + 
        '<div class="button-row"></div></div>';

        $(html).insertBefore(pageElement);

    	$(buttons).each(function() {

            var thisButton =
            '<button class="button" ' +
            'onclick="window.location.href=\'' + $(this).attr('href') + '\'">' +
            $(this).text() +
            '</button>';

            $('.button-row').append($(thisButton));
	    })
   	
    });
})(jQuery);