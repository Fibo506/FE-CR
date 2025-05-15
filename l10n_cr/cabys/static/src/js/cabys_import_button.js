/** @odoo-module **/

import { registry } from "@web/core/registry";
import { ActionButton } from "@web/views/form/form_button";

class CabysImportButton extends ActionButton {
    onClick() {
        console.log("CABYS import button clicked");
    }
}

registry.category("view_buttons").add("cabys_import_button", CabysImportButton);
