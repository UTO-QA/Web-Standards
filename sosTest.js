var gemini = require('gemini');

gemini.suite('asu-header',function(suite) {
    suite.setUrl('/')
        .setCaptureElements('#asu_hdr')
        .capture('plain');
});

gemini.suite('asu-footer',function(suite) {
    suite.setUrl('/')
        .setCaptureElements('#asu_footer')
        .capture('footer');
});