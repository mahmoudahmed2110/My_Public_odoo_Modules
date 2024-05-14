# -*- coding: utf-8 -*-

from odoo.addons.portal.controllers.portal import CustomerPortal, pager
from odoo.http import request
from odoo import http, _
from odoo.tools import groupby as groupbylem
from operator import itemgetter
class MyproductsPortal(CustomerPortal):

    @http.route(["/new/product"], type="http", methods=["POST","GET"], auth="user", website=True)
    def registerProdtuctDetails(self, **kw):
        category_list = request.env['product.category'].search([])
        vals = {'categories': category_list, 'page_name': "register_product"}
        if request.httprequest.method == "POST":
            print(kw)
            error_list = []
            if not kw.get("name"):
                error_list.append("Name field is Mandatory")
            if not kw.get("category"):
                error_list.append("Category field is Mandatory.")
            if not kw.get("category").isdigit():
                error_list.append("invalid Category field.")
            # if not request.env['product.category'].search([('id', '=', int(kw.get("category")))]):
            #     error_list.append("invalid Category field selected value.")
            if not error_list:
                request.env['product.template'].create({"name": kw.get("name"),
                                                    "categ_id": int(kw.get("category"))})
                success = "Successfully Product Registered!"
                vals['success_msg'] = success
            else:
                vals['error_list'] = error_list
        else:
            print("GET Method ..................")
        return request.render("products_portal.new_products_form_view_portal", vals)

    def _prepare_home_portal_values(self, counters):
        rtn = super(MyproductsPortal, self)._prepare_home_portal_values(counters)
        print("_prepare_portal_layout_values called", rtn)
        rtn['product_counts'] = request.env['product.template'].search_count([])
        return rtn

    @http.route(['/my/products', '/my/products/page/<int:page>'], type='http', auth="user", website=True)
    def myproductsListView(self, page=1, sortby='id', search="", search_in="All", groupby="none", **kw):

        if not groupby:
            groupby = 'none'
        sorted_list = {
            'id': {'label': 'ID', 'order': 'id'},
            'id_desc': {'label': 'ID Desc', 'order': 'id desc'},
            'name': {'label': 'Name', 'order': 'name'},
            'categ_id': {'label': 'Product Category', 'order': 'categ_id'}
        }

        search_list = {
            'All': {'label': 'All', 'input': 'All', 'domain':[]},
            'Name': {'label': 'Product Name', 'input': 'Name', 'domain':[('name','ilike',search)]},
            'Category': {'label': 'Category', 'input': 'Category', 'domain':[('categ_id.name','ilike',search)]}
        }

        groupby_list = {
            'none': {'input':'none', 'label':_("None"), "order":1},
            'categ_id': {'input':'categ_id', 'label':_("Product Category"), "order":1},
        }
        product_group_by = groupby_list.get(groupby, {})
        search_domain = search_list[search_in]['domain']
        default_order_by = sorted_list[sortby]['order']
        if groupby in ("categ_id"):
            product_group_by = product_group_by.get("input")
            default_order_by = product_group_by+","+default_order_by
        else:
            product_group_by = ''
        product_obj = request.env['product.template']
        total_products = product_obj.sudo().search_count(search_domain)
        product_url = '/my/products'
        page_detail = pager(url=product_url,
                            total=total_products,
                            page=page,
                            url_args={'sortby': sortby, 'search_in': search_in, 'search': search, 'groupby':groupby},
                            step=10)
        products = product_obj.sudo().search([], limit=10, order=default_order_by, offset=page_detail['offset'])
        if product_group_by:
            products_group_list = [{product_group_by:k, 'products':product_obj.concat(*g)} for k,g in groupbylem(products, itemgetter(product_group_by))]
        else:
            products_group_list = [{'products':products}]
        print(products_group_list)
        vals = {
                #'products': products,
                'group_products': products_group_list,
                'page_name':'products_list_view', 'pager':page_detail,
                'default_url':product_url,
                'groupby': groupby,
                'sortby':sortby,
                'searchbar_sortings':sorted_list,
                'searchbar_groupby':groupby_list,
                'search_in':search_in,
                'searchbar_inputs':search_list,
                'search':search,
                }
        return request.render("products_portal.my_products_list_view_portal", vals)

    @http.route(['/my/product/<model("product.template"):product_id>'], auth="user", type='http', website=True)
    def myProductsFormView(self, product_id, **kw):
        vals = {"product": product_id,  'page_name':'products_form_view'}
        product_records = request.env['product.template'].search([])
        product_ids = product_records.ids
        product_index = product_ids.index(product_id.id)
        if product_index != 0 and product_ids[product_index-1]:
            vals['prev_record'] = '/my/product/{}'.format(product_ids[product_index-1])
        if product_index < len(product_ids) and product_ids[product_index+1]:
            vals['next_record'] = '/my/product/{}'.format(product_ids[product_index+1])
        return request.render("products_portal.my_products_form_view_portal", vals)



    @http.route(['/my/product/print/<model("product.template"):product_id>'], auth="user", type="http", website=True)
    def myProductsReportPrint(self, product_id, **kw):
        print("Hello this is called", product_id)
        return