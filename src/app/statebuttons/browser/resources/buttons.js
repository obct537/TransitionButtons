(function($) {
    $(document).ready(function() {

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
        
        // FUTURE:  Possible interface to select all allowed transitions?
        //          Also, include a "add to panel" button on create transition page?
        //          Prevent anyting from showing up if there's no selectable buttons.
    	

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

        if( buttons.length < 1 )
        {
            return 0;
        }

    	buttons.push($('a[href="' + base + '/edit"]'));

        var html ="<div id='transitionButtons'>";

        html = html + 
        '<h3>State: <span class="stateTitle" >' + state +'</span></h3>' +
        '<p>' + stateDescription + '</p>' + 
        '<div class="button-row">';

    	$(buttons).each(function() {

    		html = html +
            "<a href='" + $(this).attr('href') + "'>" + 
            "<div class='button'>" + $(this).text() + "</div>" +
	    	"</a>";

	    })

        html = html + '</div></div>';
        $('#portal-breadcrumbs').prepend(html);   	
    });
})(jQuery);