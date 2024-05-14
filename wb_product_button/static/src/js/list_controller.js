/** @odoo-module **/

import { ListController } from "@web/views/list/list_controller";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";

patch(ListController.prototype, "wb_product_button",{

    setup(){
        this._super.apply();
        this.action = useService("action");
    },

    wbButtonClickEvent(){
        this.action.doAction({
            type:"ir.actions.act_window",
            name:"Product Details Update",
            view_mode:"form",
            target:"new",
            res_model:"product.template",
            views:[[false, "form"]],
            context:'{"default_product_ids":['+ this.model.root.selection.map((datapoint) => datapoint.res_id)+']}'
        })
    }
});

//it work on wizard form and many2one field