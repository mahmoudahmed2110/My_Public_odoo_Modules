odoo.define("wb_pos.WBSampleButton", function(require){
"use strict";

    const PosComponent = require("point_of_sale.PosComponent");
    const ProductScreen = require("point_of_sale.ProductScreen");
    const Registries = require("point_of_sale.Registries");
    const { useListener } = require("@web/core/utils/hooks");
    const core = require("web.core");
    var _t = core._t;

    class WBSampleButton extends PosComponent {

        setup(){
            super.setup();
            useListener("click", this.wb_sample_button_click);
        }

        async wb_sample_button_click(){

//            var result = await this.rpc({
//                'model':"res.lang",
//                'method':"search_read",
//                'args':[[],['id','name','code']],
//            });

            var result = await this.rpc({
                route: '/pos/rpc/example',
                params: {}
            })

            console.log(result);

            result.forEach(function(value){
                console.log("Record---> ",value);
            })

//            this.showPopup("ErrorPopup", {
//                title: _t("Error Message"),
//                body: this.env._t("The simple Error message screen.")
//            });
//            var { confirmed }= await this.showPopup("ConfirmPopup",{
//                title:"Confirm Popup",
//                body:" Are you sure want to continue?",
//                confirmText:"yes",
//                cancelText:"No"
//            });

//             if(confirmed){
//                console.log("clicked to yes button");
//             }else{
//                console.log("clicked to No button");
//             }

//            this.showPopup("OfflineErrorPopup", {
//                title:"Odoo Error",
//                body:" Hey This is test popup screen, don't take seriously!"
//            });

//            const { confirmed, payload: selectionOption } = await this.showPopup("SelectionPopup", {
//                title:"This is Selection popup screen",
//                list: [
//                {'id':0,'label':"Yes",'item':"You pressed Yes"},
//                {'id':1,'label':"No",'item':"You pressed No"},
//                {'id':2,'label':"Not Sure",'item':"You pressed Not Sure"},
//                ]
//            });
//
//            console.log(confirmed);
//            console.log(selectionOption);

//            const info = await this.env.pos.getClosePosInfo();
//            this.showPopup("ClosePosPopup", {
//                info: info,
//                keepBehind: true,
//            });

            console.log("Hello this is button click event pressed .......");
        }

    }

    WBSampleButton.template = "WBSampleButton";
    ProductScreen.addControlButton({
        component: WBSampleButton,
        position: ["before", "OrderlineCustomerNoteButton"],
    });

    Registries.Component.add(WBSampleButton);

    return WBSampleButton;

});


/** @odoo-module **/
//import { PosGlobalState } from 'point_of_sale.models';
//import Registries from 'point_of_sale.Registries';
//
//const PosButtonRestrict = (PosGlobalState) => class PosButtonRestrict extends PosGlobalState{
//
//     async _processData(loadedData){
//        await super._processData(...arguments);
//        this.visible_backspace_btn = loadedData['visible_backspace_btn']
//    }
//}
//
//Registries.Model.extend(PosGlobalState, PosButtonRestrict);
