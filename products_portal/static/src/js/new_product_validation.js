odoo.define("wb_portal.NewProductForm", function(require){
'use restrict';
console.log("Hi this is for the testing purpose log write down.");
var publicWidget = require("web.public.widget");

publicWidget.registry.NewProductForm = publicWidget.Widget.extend ({
     selector:"#new_product_creation",
     events:{
            'submit': "_onSubmitButton",

     },

     _onSubmitButton: function(evt){
        var productName = this.$("input[name='name']").val();
        var categoryName = this.$("select[name='category']");
        var category_name = ($categoryName.val() || '0');
        if(!productName){
            $("#product_client_side_validation_message").html("Please enter product name.");
            $("#product_client_side_validation_message").show();
            evt.preventDefault();
        }
        if(!categoryName || category_name == '0'){
            $("#product_client_side_validation_message").html("Please select product category.");
            $("#product_client_side_validation_message").show();
            evt.preventDefault();
        }
        if(!category_name.match(/^[0-9]+$/)){
            $("#product_client_side_validation_message").html("Please select product category option.");
            $("#product_client_side_validation_message").show();
            evt.preventDefault();
        }

//        console.log("Hello  This submit button clicked!");
//        alert("Hi")
     },

})

})