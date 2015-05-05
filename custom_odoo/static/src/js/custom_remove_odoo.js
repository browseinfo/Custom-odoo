(function() {

var instance = openerp;
openerp.web.chrome = {};

var QWeb = instance.web.qweb,
    _t = instance.web._t;


instance.web.WebClient.include({
    _title_changed: function() {
        var parts = _.sortBy(_.keys(this.get("title_part")), function(x) { return x; });
        var tmp = "";
        _.each(parts, function(part) {
            var str = this.get("title_part")[part];
            console.log('call');
            if (str) {
                tmp = tmp ? tmp : str;
            }
        }, this);
        document.title = tmp;
    },
});

})();