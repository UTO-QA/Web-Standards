var gemini = require('gemini');

gemini.suite('asu-header', function(suite) {
    suite
    	.before(function(actions, find) {
        actions.sendKeys(find('#username'),'**enter ASURITE ID here**');
        actions.sendKeys(find('#password'),'**enter ASURITE password here**');
        actions.click(find('#login_submit > input'))
        	   .wait(2000);
    	})
    	.setUrl('/')
        .setCaptureElements('#asu_hdr')
        .capture('plain');
});


gemini.suite('asu-footer', function(suite) {
    suite.setUrl('/')
        .setCaptureElements('#asu_footer')
        .capture('footer');
});