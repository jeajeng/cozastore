from logging import error
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

null = None

class Home(Resource):
    def get(self):
        return{
            "data":[
                {
    "topbar":[
        {
            "left":{
                "deskripsi":" Free shipping for standard order over $100",
                "url":"null"
            },
            "right":[
                {
                    "deskripsi":"Help & FAQs",
                    "url": "https://preview.colorlib.com/theme/cozastore/index.html#"
                },
                {
                    "deskripsi":"My acount",
                    "url": "https://preview.colorlib.com/theme/cozastore/index.html#"
                },
                {
                    "deskripsi":"EN",
                    "url": "https://preview.colorlib.com/theme/cozastore/index.html#"
                },
                {
                    "deskripsi":"USD",
                    "url": "https://preview.colorlib.com/theme/cozastore/index.html#"
                }
            ]
        }
    ],
    "menu":[
        {
           "mainmenu":
           {
            "logo":{
                "image":"data:image/webp;base64,UklGRqACAABXRUJQVlA4TJQCAAAvhAAEEH8gEEhy2p9vhZmZmYlI6DigvP//GUle0ztpu8e2nducPHOy7Vneam0zy8ZxbdverNU87bF1WqaVLudz+P3Sz0T0fwLAe/XN9Zj3fflICVx1owlcc+MyrFf/cYvDg77v+5Ww+de3pgH3+/6VDlf5vu/D/LykWcCHkr51GZQJpNVk8WJpIwVJmoeXl8IKyEi6g0CSHAYkKXTxYknaOJ6iQkvfsxNaQ6dxQjR7gsNAz9HLcs9C5sThl1UWnJ0wYQIU1POPVEuf9FVBPc5VN974qjrBk1RmjNVBsQKiWpgfV8HmuIJMJWRqgrMA5xSWklaKrFazOVYF0K1N0KxQVUamFg64tufeBYjmWkbm2QKdhav0LnHowojqgJwqoFdPaJ4RzcVqDG8y3rvTMpQwqDrMzXoWCLQO9ulbINIRpYygp3wcUa1x1beWsVrbiGosV+lO4CrthX6tBXJy4k6jMR/uSEpb9nUaXqEieNf3lzN6MfIqg0a9S1YuwL6/tTshM472tuKzBJLOMpSwWU3Ac9rLVXoWuEopIlUY8LNKbWOWc0ahqYTg7IQJDl1aB5u/fGS+eoA+NTCiOUCgzi/zqrORq7GN1BvNTWQqn2uC4CxAs76F73QneVVBTlUUVAoMy9wL7C+FqN4W3Gn07SVT2RiXJsyXbn8g1lxG1XnFn5J7l+4EyFieBaJ6iOps58ISIFdDppJ0TQJpmeVcJTPFoEyK4fbt2+MQ6HoWctU2snfAh6FrvHdn0lVGCkhLCssT9ulZIKty8OJHPgvdhGZ1tGkDhhe6QWdbWxvQGusZF5j/l3qWk9Css0CkauCFWKtI4GPpMcdCpiaQJAegBPsWh4vsTQZoxLplCUAj0OgwYcKECQA="
            },
            "navbar":[
                {
                    "deskripsi":"Home",
                    "dropdown":[
                        {
                            "deskripsi":"Homepag1",
                            "url":"https://preview.colorlib.com/theme/cozastore/index.html",
                            "active":True
                        },
                        {
                            "deskripsi":"Homepage2",
                            "url":"https://preview.colorlib.com/theme/cozastore/home-02.html"
                        },
                        {
                            "deskripsi":"Homepage3",
                            "url":"https://preview.colorlib.com/theme/cozastore/home-03.html"
                        }   
                    ]
                },
                {
                    "deskripsi":"Shop",
                    "url":"https://preview.colorlib.com/theme/cozastore/product.html",
                    "content":[

                    ]
                },
                {
                    "deskripsi":"Features",
                    "url":"https://preview.colorlib.com/theme/cozastore/shoping-cart.html",
                    "label":"hot"
                },
                {
                    "deskripsi":"Blog",
                    "url":"https://preview.colorlib.com/theme/cozastore/blog.html"
                },
                {
                    "deskripsi":"About",
                    "url":"https://preview.colorlib.com/theme/cozastore/about.html"
                },
                {
                    "deskripsi":"Contact",
                    "url":"https://preview.colorlib.com/theme/cozastore/contact.html"
                }
            ]   
           }
           
        },
        {
            "iconheader":[
                {
                    "icon":"search",
                    "value":"null"
                },
                {
                    "icon":"cart",
                    "notif":2,
                    "cart_item":[
                        {
                            "image":"images/xitem-cart-01.jpg.pagespeed.ic.OR3SDRpeNa.webp",
                            "deskripsi":"White shirt pleat",
                            "qty":1,
                            "price":19.00,
                            "qurrency":"USD"
                            
                        },
                        {
                            "image":"images/xitem-cart-02.jpg.pagespeed.ic.i1QzWnpTT6.webp",
                            "deskripsi":"Converse all Star",
                            "qty":1,
                            "price":39.00,
                            "qurrency":"USD"
                            
                        },
                        {
                            "image":"images/xitem-cart-03.jpg.pagespeed.ic.oMriSJvVmo.webp",
                            "deskripsi":"Nixon Porter Leather",
                            "qty":1,
                            "price":17.00,
                            "qurrency":"USD"  
                        },
                        {
                            "Total":75.00,
                            "qurrency":"USD"
                        },
                        {
                            "viewcart":"https://preview.colorlib.com/theme/cozastore/shoping-cart.html",
                            "ceckout":"https://preview.colorlib.com/theme/cozastore/shoping-cart.html"
                        }
                    ]       
                },
                {
                    "icon":"favorite outline",
                    "notif":0,
                    "url":"https://preview.colorlib.com/theme/cozastore/contact.html"
                }
            ]
        }
    ],
    "body":[
        {
            "banner":[
                {
                    "image":"url(images/xslide-01.jpg.pagespeed.ic.XotvXKn0Mi.webp)",
                    "title":"Women Collection 2018",
                    "subtitle":"NEW SEASON",
                    "button":[
                        {
                            "text":"shop now",
                            "url":"product.html"
                        }
                    ]
                },
                {
                    "image":"url(images/xslide-02.jpg.pagespeed.ic.__MQeyG5T4.webp)",
                    "title":"men new season",
                    "subtitle":"Jackets & Coats",
                    "button":[
                        {
                            "text":"shop now",
                            "url":"product.html"
                        }
                    ]
                },
                {
                    "image":"url(images/xslide-03.jpg.pagespeed.ic.tP-L47NU9M.webp)",
                    "title":"Men Collection 2018",
                    "subtitle":"New arrivals",
                    "button":[
                        {
                            "text":"shop now",
                            "url":"product.html"
                        }
                    ]
                }
            ],
            "content1":[
                {
                    "image":"images/xbanner-01.jpg.pagespeed.ic.Uj5FE94mgU.webp",
                    "name":"Women",
                    "text":"Spring 2018",
                    "button":[
                        {
                            "text":"shop now",
                            "url":"product.html"
                        }
                    ]
                },
                {
                    "image":"images/xbanner-02.jpg.pagespeed.ic.MQuZq6F18q.webp",
                    "name":"Men",
                    "text":"Spring 2018",
                    "button":[
                        {
                            "text":"shop now",
                            "url":"product.html"
                        }
                    ]
                },
                {
                    "image":"images/xbanner-03.jpg.pagespeed.ic.1rqLomOaMb.webp",
                    "name":"Accessories",
                    "text":"New Trend",
                    "button":[
                        {
                            "text":"shop now",
                            "url":"product.html"
                        }
                    ]
                }
            ],
            "content2":[
                {
                    "title":"PRODUCT OVERVIEW"  
                },
                {
                    "left":[
                        {
                            "produk":[
                                {
                                    "allproduct":[
                                        {
                                            "id":1,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-01.jpg.pagespeed.ic.6WHvZRJRuO.webp",
                                            "name":"Esprit Ruffle Shirt",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":16.64,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                            
                                        },
                                        {
                                            "id":2,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-02.jpg.pagespeed.ic._mIojWDfEX.webp",
                                            "name":"Herschel supply",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":35.31,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":1,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-03.jpg.pagespeed.ic.eOHs429Gtb.webp",
                                            "name":"Only Check Trouser",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":25.50,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"men"
                                        },
                                        {
                                            "id":3,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-04.jpg.pagespeed.ic.1MaP4euDx9.webp",
                                            "name":"Classic Trench Coat",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":75.00,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":4,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-05.jpg.pagespeed.ic.GHcB3Nc9zp.webp",
                                            "name":"Front Pocket Jumper",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":34.75,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":1,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-06.jpg.pagespeed.ic.mU9c3gp9yp.webp",
                                            "name":"Vintage Inspired Classic",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":93.20,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"watches"
                                        },
                                        {
                                            "id":5,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-07.jpg.pagespeed.ic.wXz93SW1CF.webp",
                                            "name":"Shirt in Stretch Cotton",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":52.66,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":6,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-08.jpg.pagespeed.ic.zcR_ZfXlFq.webp",
                                            "name":"Shirt in Stretch Cotton",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":18.96,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":1,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-09.jpg.pagespeed.ic._ex9y9IVR9.webp",
                                            "name":"Converse All Star Hi Plimsolls",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":75.00,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"shoes"
                                        },
                                        {
                                            "id":7,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-10.jpg.pagespeed.ic.JKjq4oUn3E.webp",
                                            "name":"Femme T-Shirt In Stripe",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":25.85,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-11.jpg.pagespeed.ic.fJxJBqHZzv.webp",
                                            "name":"Herschel supply",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":63.16,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"men"
                                        },
                                        {
                                            "id":2,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-12.jpg.pagespeed.ic.Ft0-TDvq7W.webp",
                                            "name":"Herschel supply",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":63.16,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"men"
                                        },
                                        {
                                            "id":8,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-13.jpg.pagespeed.ic.jIjGx2QblE.webp",
                                            "name":"T-Shirt with Sleeve",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":18.49,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":9,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-14.jpg.pagespeed.ic.rUWpWgkkYK.webp",
                                            "name":"Pretty Little Thing",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":54.79,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":2,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-15.jpg.pagespeed.ic.LNG1pmoqOY.webp",
                                            "name":"Mini Silver Mesh Watch",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":86.85,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"watches"
                                        },
                                        {
                                            "id":10,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-16.jpg.pagespeed.ic.AbLwZITYaU.webp",
                                            "name":"Square Neck Back",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":29.64,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"


                                             
                                        }
                                       
                                    ],
                                    "Women":[
                                        {
                                            "id":1,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-01.jpg.pagespeed.ic.6WHvZRJRuO.webp",
                                            "name":"Esprit Ruffle Shirt",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":16.64,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                            
                                        },
                                        {
                                            "id":2,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-02.jpg.pagespeed.ic._mIojWDfEX.webp",
                                            "name":"Herschel supply",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":35.31,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":3,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-04.jpg.pagespeed.ic.1MaP4euDx9.webp",
                                            "name":"Classic Trench Coat",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":75.00,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":4,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-05.jpg.pagespeed.ic.GHcB3Nc9zp.webp",
                                            "name":"Front Pocket Jumper",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":34.75,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":5,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-07.jpg.pagespeed.ic.wXz93SW1CF.webp",
                                            "name":"Shirt in Stretch Cotton",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":52.66,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":6,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-08.jpg.pagespeed.ic.zcR_ZfXlFq.webp",
                                            "name":"Shirt in Stretch Cotton",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":18.96,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":7,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-10.jpg.pagespeed.ic.JKjq4oUn3E.webp",
                                            "name":"Femme T-Shirt In Stripe",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":25.85,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":9,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-13.jpg.pagespeed.ic.jIjGx2QblE.webp",
                                            "name":"T-Shirt with Sleeve",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":18.49,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":10,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-14.jpg.pagespeed.ic.rUWpWgkkYK.webp",
                                            "name":"Pretty Little Thing",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":54.79,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        }

                                    ],
                                    "men":[
                                        {
                                            "id":1,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-03.jpg.pagespeed.ic.eOHs429Gtb.webp",
                                            "name":"Only Check Trouser",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":25.50,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"men"
                                        },
                                        {
                                            "id":2,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-11.jpg.pagespeed.ic.fJxJBqHZzv.webp",
                                            "name":"Herschel supply",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":63.16,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"men"
                                        },
                                        {
                                            "id":3,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-12.jpg.pagespeed.ic.Ft0-TDvq7W.webp",
                                            "name":"Herschel supply",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":63.16,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"men"
                                        }
                                    ],
                                    "BAG":[
                                        {
                                            "VALUE":null
                                        }
                                    ],
                                    "Shoes":[
                                        {
                                            "id":1,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-09.jpg.pagespeed.ic._ex9y9IVR9.webp",
                                            "name":"Converse All Star Hi Plimsolls",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":75.00,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"shoes"
                                        }
                                    ],
                                    "Watches":[
                                        {
                                            "id":1,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-06.jpg.pagespeed.ic.mU9c3gp9yp.webp",
                                            "name":"Vintage Inspired Classic",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":93.20,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"watches"
                                        },
                                        {
                                            "id":2,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-15.jpg.pagespeed.ic.LNG1pmoqOY.webp",
                                            "name":"Mini Silver Mesh Watch",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":86.85,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"watches"
                                        }
                                    ]
                                },
                                {
                                    "button":{
                                        "text": "read more",
                                        "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                                    }
                                }
                            ]
                        }
                    ],
                    "right":[
                        {
                            "text":"filter",
                            "showfilter":{
                                "icon":"zmdi show filter",
                                "item":[
                                    {
                                        "sort by":[
                                            {
                                                "text":"default",
                                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                                            },
                                            {
                                                "text":"Popularity",
                                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                                            },
                                            {
                                                "text":"average rating",
                                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                                            },
                                            {
                                                "text":"newness",
                                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                "active":True
                                            },
                                            {
                                                "text":"Price: Low to High",
                                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                                            },
                                            {
                                                "text":"Price: High to Low",
                                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                                            }
                                        ],
                                        "Price":[
                                            {
                                                "text":"all",
                                                "active":True,
                                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                                            },
                                            {
                                                "price":"$0.00 - $50.00",
                                                "currency":"USD",
                                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#"   
                                            },
                                            {
                                                "price":"$50.00 - $100.00",
                                                "currency":"USD",
                                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#"   
                                            },
                                            {
                                                "price":"$100.00 - $150.00",
                                                "currency":"USD",
                                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#"   
                                            },
                                            {
                                                "price":"$150.00 - $200.00",
                                                "currency":"USD",
                                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#"   
                                            },
                                            {
                                                "price":"$200.00+",
                                                "currency":"USD",
                                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#"   
                                            }
                                            
                                        ],
                                        "color":[
                                            {
                                                "text":"black",
                                                "icon":"zimdi zimdi circle black"
                                            },
                                            {
                                                "text":"ble",
                                                "icon":"zimdi zimdi circle blue"
                                            },
                                            {
                                                "text":"grey",
                                                "icon":"zimdi zimdi circle grey"
                                            },
                                            {
                                                "text":"grenn",
                                                "icon":"zimdi zimdi circle green"
                                            },
                                            {
                                                "text":"red",
                                                "icon":"zimdi zimdi circle red"
                                            },
                                            {
                                                "text":"white",
                                                "icon":"zimdi zimdi circle white"
                                            }
                                           
                                        ],
                                        "tags":[
                                            {
                                                "textbutton":"Fashion",
                                                "url":"https://preview.colorlib.com/theme/cozastore/about.html"
                                            },
                                            {
                                                "textbutton":"Denim",
                                                "url":"https://preview.colorlib.com/theme/cozastore/about.html"
                                            },
                                            {
                                                "textbutton":"Crafts",
                                                "url":"https://preview.colorlib.com/theme/cozastore/about.html"
                                            },
                                            {
                                                "textbutton":"lifestyle",
                                                "url":"https://preview.colorlib.com/theme/cozastore/about.html"
                                            },
                                            {
                                                "textbutton":"streetstyle",
                                                "url":"https://preview.colorlib.com/theme/cozastore/about.html"
                                            }
                                        ]
                                           
                                        
                                    }
                                ]

                            }
                           
                        },
                        {
                            "search":{
                                "placeholder":"search",
                                "icon":"zimdi zimdi search",
                                "hover":{
                                    "icon":"zimdi zimdi search",
                                    "placeholder":"search",
                                    "value":null
                                }
                            }
                        }
                    ]
                }
                
                
            ]
        }
    ],
    "footer":[
        {
            "categories":[
                {
                    "text":"women",
                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                },
                {
                    "text":"men",
                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                },
                {
                    "text":"shoes",
                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                },
                {
                    "text":"watches",
                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                }
                
            ],
            "HELP":[
                {
                    "text":"TRACK ORDER",
                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                },
                {
                    "text":"returns",
                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                },
                {
                    "text":"Shipping",
                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                },
                {
                    "text":"FAQs",
                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                }
            ],
            "GET IN TOUCH":{
                "Text":"Any questions? Let us know in store at 8th floor, 379 Hudson St, New York, NY 10018 or call us on (+1) 96 716 6879",
                "sosmed":[
                    {
                        "icon":"zimdi zimdi facebook",
                        "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                    },
                    {
                        "icon":"zimdi zimdi instagram",
                        "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                    },
                    {
                        "icon":"zimdi zimdi twitter",
                        "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                    }
                ]
                
            },
            "NEWSLETTER":[
                {
                    "email":"email@example.com",
                    "url":null
                },
                {
                    "textbutton":"subscribe",
                    "url":"https://preview.colorlib.com/theme/cozastore/index.html?email=#"
                }
            ]
            
        }
    ],
    "subfooter":[
        {
            "image":"data:image/webp;base64,UklGRlgEAABXRUJQVlA4TEsEAAAvIoAFELXImrbtjKRv7d0z2zy0j2zbtm3btm3btr1J99qtpD14xzP5B2Oz8Xal6qv6JEiSbdpW7r3P0/xnpG/z2rZ974El27ZpZ5y86BmxbdtO/tP/fujqHLi1batWvkT+gQLcIo8dOnDrRdvQ84mhEgpwaeDgmk2Fbds2YJLucUdwGbo7sNGWzTasS9GBnXpMBwdXZcqTb4BUi9kNXsGR5EQj/2lpzOUczbAgKiox0XdfVGASfefxBx8Z6JtJG42QCBVkegZnEmiAX3rE2+N9z/lj9523x9uRI9MzMINAETpYYoSIppBoISCSRUYyJubYrKkCKjaPWBIlLJIxrcAcI0zGj2Q6BqYRqAXT4O153P1907vbGLSGSAiJOUYuLYSALU4XMEj+58G7fd2rbcPf2xBQECCGxBgjl16kugV3Fj1fTyMAH0g6lQCogFun07Ktn1T4f6F461a//ib3WAGRGuhErcSFuKK+rsnLk35fz3X5eO1gb47TfFcKj8ULkwk1Xt+93DbgW5JOIfB/AFuU9pUuXcPFrXnElbGDFSN7Gzq3d4zor9s6mzKws+mXAFR6DLftnk0Y9PnCqvo6wNAfp1q8PTg7nTS/tG1OYcfswo5/l5rNrWWdPtzQpQjwmkzHwGQChawipEqFL+dq/zm1fzmlfOtSk/qhG4u28ZM1fdtbciyftKvsyb56pjjVrJ7Myrp5cG3d1fHtzorqutP9OfWfX2xtL3m/q1td3bC4vKXq+09nphNmFnbNKuwCfwAvyXQMTCQAHjF3/1hXtHarTvVYvdaxcct193Z1w5Yb1u5mTe8vKVa9dXbb0aRwYEBrQ4H2vQfHUe82TY1enkz9u2/M70NHuzM+nkYsLG07Ppy2ub2s28dr1xY9XT9fOzycBf544DlJJxAAnNxdQpx4eRqFOG2whFh1dD7QpbUj9+CBeyqNra0iDgztrMMB3881fXlius+BH7i6vqZQ89u1ec+Mwp5h308dGU2r/vbl2aHO+JCx4ilJxxMohsqG6ZSh0w2/YqLKSrpQenAa13u5ZfRg1djRqp2TCYBGtQN5+veErCDEaHl93YHBLO1d4XtAlUqRC0pbVtfXxNxcdVyc9yytbsKfKTLjMUnHEYBPAl1WAJmvEj4PuBwH+Ge5yzBcPp9BfDg17gA5DuJjRnz8p8gDJbg8+JuVTI9/dA+ZBPV97ldWMT79+SphBjwg6VgCwEMBRcBmk21KiZz4TXRu33Lt2qDKSom2RAVsNhsvSOQDsiwnyoocAfdJOoYAfIIPDj6juLgPefAvFcSU4UPyQRAXEecjIsLfd7S4Q9JRBH6ARGrcIulI2h54h9i38KkBnPMZhcXG+v9H2D/c5CUdg1O4wJd4DT/eIIBzFJGif7/whP90jLTmEGABkwYPcE2oEwb7cXmIx808buRBit08r+YqJ8uEMqFF6CPME5YIC0EXzQiLhFFCF6ECAA==",
            "url":"https://preview.colorlib.com/theme/cozastore/index.html?email=#"
        },
        {
            "image":"https://preview.colorlib.com/theme/cozastore/index.html?email=#",
            "url":"data:image/webp;base64,UklGRkIFAABXRUJQVlA4TDUFAAAvIoAFEFVI37btbJ/nN9u2V862bdv7ZNs2v9m2bdtbUttGmjRtn3nrf9C+kSNJsmo7OedChEzcgkKmfFoE27K1YVmf8dG9/zGdc6TZ2nZsy/HoM7Jt27Zt27brNdKvJtAE+oaUXa+f+/Fz33Br21at/MgNTd2hiJ9ycOiCVJ/gkrl1QuRQCTE16MxUFfRuwel23G/BVTLbcLsNZy0xDSgURMOJT4RkEd8SDNVGmxAekosDmYB1OWYQCAv/wUE69WcUEEYhk2GWELaYotnEFZPAVh0DAlMRDSkhwofEUuIRE9JhGoaGDwnFSFyMgTAIHCUhEo9YBMLAAsJwpFIEiYPtlc3ehfz7NoFtJ3bVjMm6ICUEyIVFCIQUpAiJEPwVDAUpyOVoFHsCEriIBAIsCYUSbMghBCsYQBiGRIqIV8QyqPcfnfvW4/ifR07/eOLy5w+8x2bsWYMcixdL1SqnzX9Z4U3p0HJ7WpPVWS/PfSDlzG6UTtsjyjzeV2zySLPhtE+lQwwSISwalmp4OKv1+oRXuZcYKQQIw5BIEVHgKvxHi7ut2/Lhs0n/3tn794xPr6sQKJacuxRwz879RJfPA4BHsp6yTClycD8BSAI5ouubyk7vA3lPz30gXM+DgASQBZ7asZsOxQKAMBSJBMECE/CEgnD1Zp0CY8rs7699+/gewvLVAuAF0d1tsaZk3XoOkND94RBn3yC+vQ4kDZ9sg8q4tu5Z7sNKg2xDH3cAORWu7gMFk4c1kM0PCEOQSBBhIE4IRijY18j/v5XhtDufeiTYGlxfBF6YNyyHhMGzXVJj51tEmqraD1eAFNnkqpVlLn+xoRASntd2edYJNW+umLhcLaMWtb45zts4QimGMBiJGBGEANjAToOqZg5LgDdml0lu9JqM+lqBMeFDNOFSRdO7M0DSzHElJNzNfVVZ3QEyQEql1R0Pcm/INX1YCTy1bJzP2ZcVXjxXdPrES+1ijYAwGIkY4QMPWMBCgyoOHsfIqEWNLi7r9HQAyBj6sAOqeadJpes7QM7mzQxIINbiW5YXEk1uAildJofoWpfo+obsh7RVm9meM8gvrwIFR48joTqEQUjECDe4wAgmCDSuD2Gpdn1L/pekotNnsh2zTh6HQcK502C5tml51imXz/1QgZe5HfoL/dBnugfI6DfZaet+vBz7nAJjCigAGYUWL2QqRQtfFkIlCAOQiBAucIIBiJkS7Co6Px0CMkBW05sz3G0DKlu1mQM8V/b2PkXraTk5AeR1fDqs/v15mUoBeGXlbobGj6eAtDYPx80al5s+rNTi8RSQ0OLxBH9bgzAAiQhhBxtoIaWl4dqSjbsZSuWHSueHdu7Hi6e/2FSyYLVY8XzXwNku5qZu/LBJnm1KplKUa5tRb3XR6e0gZ3N/ZcYHKu/vuFm7of9QyenzIKXyXS2nJ1GhQeiPpDrCAmZQQVoNRBuhL0X5liVDChBlaD5Xw6eioZOkDsmYPO+K4W7p9DDa6bnY7q/PTG+TRXGO6FNITaMJaEW+ZnwIA00Xp/RDUh1hAiMoQBDoqtGKWcJnTj4NiaYR9BGyhscYAZpGQ7Iml7OxOZKgjwhdddqIWcJjDp+KQtMIGpIlPKbwqYGDvkiqIQygBwr+SQOh4G8KiEAfJNUxpwMNfIHkvkEI+iIXY8kLCvgEyX0EhEE4yI3BG/hC4CACybBAvuKvDNqAYj6szsbDXHxMxwshZDqefxEyHa//nI2PRXgsjzVAHVABdAL6ABOAccDoH4AxgQAm/wWYAgwDugE1AA=="

        },
        {
            "image":"data:image/webp;base64,UklGRkIFAABXRUJQVlA4TDUFAAAvIoAFEFVI37btbJ/nN9u2V862bdv7ZNs2v9m2bdtbUttGmjRtn3nrf9C+kSNJsmo7OedChEzcgkKmfFoE27K1YVmf8dG9/zGdc6TZ2nZsy/HoM7Jt27Zt27brNdKvJtAE+oaUXa+f+/Fz33Br21at/MgNTd2hiJ9ycOiCVJ/gkrl1QuRQCTE16MxUFfRuwel23G/BVTLbcLsNZy0xDSgURMOJT4RkEd8SDNVGmxAekosDmYB1OWYQCAv/wUE69WcUEEYhk2GWELaYotnEFZPAVh0DAlMRDSkhwofEUuIRE9JhGoaGDwnFSFyMgTAIHCUhEo9YBMLAAsJwpFIEiYPtlc3ehfz7NoFtJ3bVjMm6ICUEyIVFCIQUpAiJEPwVDAUpyOVoFHsCEriIBAIsCYUSbMghBCsYQBiGRIqIV8QyqPcfnfvW4/ifR07/eOLy5w+8x2bsWYMcixdL1SqnzX9Z4U3p0HJ7WpPVWS/PfSDlzG6UTtsjyjzeV2zySLPhtE+lQwwSISwalmp4OKv1+oRXuZcYKQQIw5BIEVHgKvxHi7ut2/Lhs0n/3tn794xPr6sQKJacuxRwz879RJfPA4BHsp6yTClycD8BSAI5ouubyk7vA3lPz30gXM+DgASQBZ7asZsOxQKAMBSJBMECE/CEgnD1Zp0CY8rs7699+/gewvLVAuAF0d1tsaZk3XoOkND94RBn3yC+vQ4kDZ9sg8q4tu5Z7sNKg2xDH3cAORWu7gMFk4c1kM0PCEOQSBBhIE4IRijY18j/v5XhtDufeiTYGlxfBF6YNyyHhMGzXVJj51tEmqraD1eAFNnkqpVlLn+xoRASntd2edYJNW+umLhcLaMWtb45zts4QimGMBiJGBGEANjAToOqZg5LgDdml0lu9JqM+lqBMeFDNOFSRdO7M0DSzHElJNzNfVVZ3QEyQEql1R0Pcm/INX1YCTy1bJzP2ZcVXjxXdPrES+1ijYAwGIkY4QMPWMBCgyoOHsfIqEWNLi7r9HQAyBj6sAOqeadJpes7QM7mzQxIINbiW5YXEk1uAildJofoWpfo+obsh7RVm9meM8gvrwIFR48joTqEQUjECDe4wAgmCDSuD2Gpdn1L/pekotNnsh2zTh6HQcK502C5tml51imXz/1QgZe5HfoL/dBnugfI6DfZaet+vBz7nAJjCigAGYUWL2QqRQtfFkIlCAOQiBAucIIBiJkS7Co6Px0CMkBW05sz3G0DKlu1mQM8V/b2PkXraTk5AeR1fDqs/v15mUoBeGXlbobGj6eAtDYPx80al5s+rNTi8RSQ0OLxBH9bgzAAiQhhBxtoIaWl4dqSjbsZSuWHSueHdu7Hi6e/2FSyYLVY8XzXwNku5qZu/LBJnm1KplKUa5tRb3XR6e0gZ3N/ZcYHKu/vuFm7of9QyenzIKXyXS2nJ1GhQeiPpDrCAmZQQVoNRBuhL0X5liVDChBlaD5Xw6eioZOkDsmYPO+K4W7p9DDa6bnY7q/PTG+TRXGO6FNITaMJaEW+ZnwIA00Xp/RDUh1hAiMoQBDoqtGKWcJnTj4NiaYR9BGyhscYAZpGQ7Iml7OxOZKgjwhdddqIWcJjDp+KQtMIGpIlPKbwqYGDvkiqIQygBwr+SQOh4G8KiEAfJNUxpwMNfIHkvkEI+iIXY8kLCvgEyX0EhEE4yI3BG/hC4CACybBAvuKvDNqAYj6szsbDXHxMxwshZDqefxEyHa//nI2PRXgsjzVAHVABdAL6ABOAccDoH4AxgQAm/wWYAgwDugE1AA==",
            "url":"https://preview.colorlib.com/theme/cozastore/index.html?email=#"
        },
        {
            "image":"data:image/webp;base64,UklGRkIFAABXRUJQVlA4TDUFAAAvIoAFEFVI37btbJ/nN9u2V862bdv7ZNs2v9m2bdtbUttGmjRtn3nrf9C+kSNJsmo7OedChEzcgkKmfFoE27K1YVmf8dG9/zGdc6TZ2nZsy/HoM7Jt27Zt27brNdKvJtAE+oaUXa+f+/Fz33Br21at/MgNTd2hiJ9ycOiCVJ/gkrl1QuRQCTE16MxUFfRuwel23G/BVTLbcLsNZy0xDSgURMOJT4RkEd8SDNVGmxAekosDmYB1OWYQCAv/wUE69WcUEEYhk2GWELaYotnEFZPAVh0DAlMRDSkhwofEUuIRE9JhGoaGDwnFSFyMgTAIHCUhEo9YBMLAAsJwpFIEiYPtlc3ehfz7NoFtJ3bVjMm6ICUEyIVFCIQUpAiJEPwVDAUpyOVoFHsCEriIBAIsCYUSbMghBCsYQBiGRIqIV8QyqPcfnfvW4/ifR07/eOLy5w+8x2bsWYMcixdL1SqnzX9Z4U3p0HJ7WpPVWS/PfSDlzG6UTtsjyjzeV2zySLPhtE+lQwwSISwalmp4OKv1+oRXuZcYKQQIw5BIEVHgKvxHi7ut2/Lhs0n/3tn794xPr6sQKJacuxRwz879RJfPA4BHsp6yTClycD8BSAI5ouubyk7vA3lPz30gXM+DgASQBZ7asZsOxQKAMBSJBMECE/CEgnD1Zp0CY8rs7699+/gewvLVAuAF0d1tsaZk3XoOkND94RBn3yC+vQ4kDZ9sg8q4tu5Z7sNKg2xDH3cAORWu7gMFk4c1kM0PCEOQSBBhIE4IRijY18j/v5XhtDufeiTYGlxfBF6YNyyHhMGzXVJj51tEmqraD1eAFNnkqpVlLn+xoRASntd2edYJNW+umLhcLaMWtb45zts4QimGMBiJGBGEANjAToOqZg5LgDdml0lu9JqM+lqBMeFDNOFSRdO7M0DSzHElJNzNfVVZ3QEyQEql1R0Pcm/INX1YCTy1bJzP2ZcVXjxXdPrES+1ijYAwGIkY4QMPWMBCgyoOHsfIqEWNLi7r9HQAyBj6sAOqeadJpes7QM7mzQxIINbiW5YXEk1uAildJofoWpfo+obsh7RVm9meM8gvrwIFR48joTqEQUjECDe4wAgmCDSuD2Gpdn1L/pekotNnsh2zTh6HQcK502C5tml51imXz/1QgZe5HfoL/dBnugfI6DfZaet+vBz7nAJjCigAGYUWL2QqRQtfFkIlCAOQiBAucIIBiJkS7Co6Px0CMkBW05sz3G0DKlu1mQM8V/b2PkXraTk5AeR1fDqs/v15mUoBeGXlbobGj6eAtDYPx80al5s+rNTi8RSQ0OLxBH9bgzAAiQhhBxtoIaWl4dqSjbsZSuWHSueHdu7Hi6e/2FSyYLVY8XzXwNku5qZu/LBJnm1KplKUa5tRb3XR6e0gZ3N/ZcYHKu/vuFm7of9QyenzIKXyXS2nJ1GhQeiPpDrCAmZQQVoNRBuhL0X5liVDChBlaD5Xw6eioZOkDsmYPO+K4W7p9DDa6bnY7q/PTG+TRXGO6FNITaMJaEW+ZnwIA00Xp/RDUh1hAiMoQBDoqtGKWcJnTj4NiaYR9BGyhscYAZpGQ7Iml7OxOZKgjwhdddqIWcJjDp+KQtMIGpIlPKbwqYGDvkiqIQygBwr+SQOh4G8KiEAfJNUxpwMNfIHkvkEI+iIXY8kLCvgEyX0EhEE4yI3BG/hC4CACybBAvuKvDNqAYj6szsbDXHxMxwshZDqefxEyHa//nI2PRXgsjzVAHVABdAL6ABOAccDoH4AxgQAm/wWYAgwDugE1AA==",
            "url":"https://preview.colorlib.com/theme/cozastore/index.html?email=#"
        },
        {
            "image":"data:image/webp;base64,UklGRkIFAABXRUJQVlA4TDUFAAAvIoAFEFVI37btbJ/nN9u2V862bdv7ZNs2v9m2bdtbUttGmjRtn3nrf9C+kSNJsmo7OedChEzcgkKmfFoE27K1YVmf8dG9/zGdc6TZ2nZsy/HoM7Jt27Zt27brNdKvJtAE+oaUXa+f+/Fz33Br21at/MgNTd2hiJ9ycOiCVJ/gkrl1QuRQCTE16MxUFfRuwel23G/BVTLbcLsNZy0xDSgURMOJT4RkEd8SDNVGmxAekosDmYB1OWYQCAv/wUE69WcUEEYhk2GWELaYotnEFZPAVh0DAlMRDSkhwofEUuIRE9JhGoaGDwnFSFyMgTAIHCUhEo9YBMLAAsJwpFIEiYPtlc3ehfz7NoFtJ3bVjMm6ICUEyIVFCIQUpAiJEPwVDAUpyOVoFHsCEriIBAIsCYUSbMghBCsYQBiGRIqIV8QyqPcfnfvW4/ifR07/eOLy5w+8x2bsWYMcixdL1SqnzX9Z4U3p0HJ7WpPVWS/PfSDlzG6UTtsjyjzeV2zySLPhtE+lQwwSISwalmp4OKv1+oRXuZcYKQQIw5BIEVHgKvxHi7ut2/Lhs0n/3tn794xPr6sQKJacuxRwz879RJfPA4BHsp6yTClycD8BSAI5ouubyk7vA3lPz30gXM+DgASQBZ7asZsOxQKAMBSJBMECE/CEgnD1Zp0CY8rs7699+/gewvLVAuAF0d1tsaZk3XoOkND94RBn3yC+vQ4kDZ9sg8q4tu5Z7sNKg2xDH3cAORWu7gMFk4c1kM0PCEOQSBBhIE4IRijY18j/v5XhtDufeiTYGlxfBF6YNyyHhMGzXVJj51tEmqraD1eAFNnkqpVlLn+xoRASntd2edYJNW+umLhcLaMWtb45zts4QimGMBiJGBGEANjAToOqZg5LgDdml0lu9JqM+lqBMeFDNOFSRdO7M0DSzHElJNzNfVVZ3QEyQEql1R0Pcm/INX1YCTy1bJzP2ZcVXjxXdPrES+1ijYAwGIkY4QMPWMBCgyoOHsfIqEWNLi7r9HQAyBj6sAOqeadJpes7QM7mzQxIINbiW5YXEk1uAildJofoWpfo+obsh7RVm9meM8gvrwIFR48joTqEQUjECDe4wAgmCDSuD2Gpdn1L/pekotNnsh2zTh6HQcK502C5tml51imXz/1QgZe5HfoL/dBnugfI6DfZaet+vBz7nAJjCigAGYUWL2QqRQtfFkIlCAOQiBAucIIBiJkS7Co6Px0CMkBW05sz3G0DKlu1mQM8V/b2PkXraTk5AeR1fDqs/v15mUoBeGXlbobGj6eAtDYPx80al5s+rNTi8RSQ0OLxBH9bgzAAiQhhBxtoIaWl4dqSjbsZSuWHSueHdu7Hi6e/2FSyYLVY8XzXwNku5qZu/LBJnm1KplKUa5tRb3XR6e0gZ3N/ZcYHKu/vuFm7of9QyenzIKXyXS2nJ1GhQeiPpDrCAmZQQVoNRBuhL0X5liVDChBlaD5Xw6eioZOkDsmYPO+K4W7p9DDa6bnY7q/PTG+TRXGO6FNITaMJaEW+ZnwIA00Xp/RDUh1hAiMoQBDoqtGKWcJnTj4NiaYR9BGyhscYAZpGQ7Iml7OxOZKgjwhdddqIWcJjDp+KQtMIGpIlPKbwqYGDvkiqIQygBwr+SQOh4G8KiEAfJNUxpwMNfIHkvkEI+iIXY8kLCvgEyX0EhEE4yI3BG/hC4CACybBAvuKvDNqAYj6szsbDXHxMxwshZDqefxEyHa//nI2PRXgsjzVAHVABdAL6ABOAccDoH4AxgQAm/wWYAgwDugE1AA==",
            "url":"https://preview.colorlib.com/theme/cozastore/index.html?email=#"
        }
    ]
    
}


            ]
        }

class Shop(Resource):
    def get(self):
        return{
            "data":[
                {
    "left":[
        {
            "produk":[
                {
                    "allproduct":[
                        {
                            "id":1,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-01.jpg.pagespeed.ic.6WHvZRJRuO.webp",
                            "name":"Esprit Ruffle Shirt",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":16.64,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                            
                        },
                        {
                            "id":2,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-02.jpg.pagespeed.ic._mIojWDfEX.webp",
                            "name":"Herschel supply",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":35.31,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        },
                        {
                            "id":1,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-03.jpg.pagespeed.ic.eOHs429Gtb.webp",
                            "name":"Only Check Trouser",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":25.50,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"men"
                        },
                        {
                            "id":3,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-04.jpg.pagespeed.ic.1MaP4euDx9.webp",
                            "name":"Classic Trench Coat",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":75.00,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        },
                        {
                            "id":4,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-05.jpg.pagespeed.ic.GHcB3Nc9zp.webp",
                            "name":"Front Pocket Jumper",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":34.75,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        },
                        {
                            "id":1,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-06.jpg.pagespeed.ic.mU9c3gp9yp.webp",
                            "name":"Vintage Inspired Classic",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":93.20,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"watches"
                        },
                        {
                            "id":5,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-07.jpg.pagespeed.ic.wXz93SW1CF.webp",
                            "name":"Shirt in Stretch Cotton",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":52.66,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        },
                        {
                            "id":6,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-08.jpg.pagespeed.ic.zcR_ZfXlFq.webp",
                            "name":"Shirt in Stretch Cotton",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":18.96,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        },
                        {
                            "id":1,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-09.jpg.pagespeed.ic._ex9y9IVR9.webp",
                            "name":"Converse All Star Hi Plimsolls",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":75.00,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"shoes"
                        },
                        {
                            "id":7,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-10.jpg.pagespeed.ic.JKjq4oUn3E.webp",
                            "name":"Femme T-Shirt In Stripe",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":25.85,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        },
                        {
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-11.jpg.pagespeed.ic.fJxJBqHZzv.webp",
                            "name":"Herschel supply",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":63.16,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"men"
                        },
                        {
                            "id":2,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-12.jpg.pagespeed.ic.Ft0-TDvq7W.webp",
                            "name":"Herschel supply",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":63.16,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"men"
                        },
                        {
                            "id":8,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-13.jpg.pagespeed.ic.jIjGx2QblE.webp",
                            "name":"T-Shirt with Sleeve",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":18.49,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        },
                        {
                            "id":9,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-14.jpg.pagespeed.ic.rUWpWgkkYK.webp",
                            "name":"Pretty Little Thing",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":54.79,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        },
                        {
                            "id":2,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-15.jpg.pagespeed.ic.LNG1pmoqOY.webp",
                            "name":"Mini Silver Mesh Watch",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":86.85,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"watches"
                        },
                        {
                            "id":10,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-16.jpg.pagespeed.ic.AbLwZITYaU.webp",
                            "name":"Square Neck Back",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":29.64,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"


                             
                        }
                       
                    ],
                    "Women":[
                        {
                            "id":1,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-01.jpg.pagespeed.ic.6WHvZRJRuO.webp",
                            "name":"Esprit Ruffle Shirt",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":16.64,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                            
                        },
                        {
                            "id":2,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-02.jpg.pagespeed.ic._mIojWDfEX.webp",
                            "name":"Herschel supply",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":35.31,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        },
                        {
                            "id":3,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-04.jpg.pagespeed.ic.1MaP4euDx9.webp",
                            "name":"Classic Trench Coat",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":75.00,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        },
                        {
                            "id":4,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-05.jpg.pagespeed.ic.GHcB3Nc9zp.webp",
                            "name":"Front Pocket Jumper",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":34.75,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        },
                        {
                            "id":5,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-07.jpg.pagespeed.ic.wXz93SW1CF.webp",
                            "name":"Shirt in Stretch Cotton",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":52.66,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        },
                        {
                            "id":6,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-08.jpg.pagespeed.ic.zcR_ZfXlFq.webp",
                            "name":"Shirt in Stretch Cotton",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":18.96,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        },
                        {
                            "id":7,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-10.jpg.pagespeed.ic.JKjq4oUn3E.webp",
                            "name":"Femme T-Shirt In Stripe",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":25.85,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        },
                        {
                            "id":9,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-13.jpg.pagespeed.ic.jIjGx2QblE.webp",
                            "name":"T-Shirt with Sleeve",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":18.49,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        },
                        {
                            "id":10,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-14.jpg.pagespeed.ic.rUWpWgkkYK.webp",
                            "name":"Pretty Little Thing",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":54.79,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        }

                    ],
                    "men":[
                        {
                            "id":1,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-03.jpg.pagespeed.ic.eOHs429Gtb.webp",
                            "name":"Only Check Trouser",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":25.50,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"men"
                        },
                        {
                            "id":2,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-11.jpg.pagespeed.ic.fJxJBqHZzv.webp",
                            "name":"Herschel supply",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":63.16,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"men"
                        },
                        {
                            "id":3,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-12.jpg.pagespeed.ic.Ft0-TDvq7W.webp",
                            "name":"Herschel supply",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":63.16,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"men"
                        }
                    ],
                    "BAG":[
                        {
                            "VALUE":null
                        }
                    ],
                    "Shoes":[
                        {
                            "id":1,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-09.jpg.pagespeed.ic._ex9y9IVR9.webp",
                            "name":"Converse All Star Hi Plimsolls",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":75.00,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"shoes"
                        }
                    ],
                    "Watches":[
                        {
                            "id":1,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-06.jpg.pagespeed.ic.mU9c3gp9yp.webp",
                            "name":"Vintage Inspired Classic",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":93.20,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"watches"
                        },
                        {
                            "id":2,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-15.jpg.pagespeed.ic.LNG1pmoqOY.webp",
                            "name":"Mini Silver Mesh Watch",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":86.85,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"watches"
                        }
                    ]
                },
                {
                    "button":{
                        "text": "read more",
                        "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                    }
                }
            ]
        }
    ],
    "right":[
        {
            "text":"filter",
            "showfilter":{
                "icon":"zmdi show filter",
                "item":[
                    {
                        "sort by":[
                            {
                                "text":"default",
                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                            },
                            {
                                "text":"Popularity",
                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                            },
                            {
                                "text":"average rating",
                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                            },
                            {
                                "text":"newness",
                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                "active":True
                            },
                            {
                                "text":"Price: Low to High",
                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                            },
                            {
                                "text":"Price: High to Low",
                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                            }
                        ],
                        "Price":[
                            {
                                "text":"all",
                                "active":True,
                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#"
                            },
                            {
                                "price":"$0.00 - $50.00",
                                "currency":"USD",
                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#"   
                            },
                            {
                                "price":"$50.00 - $100.00",
                                "currency":"USD",
                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#"   
                            },
                            {
                                "price":"$100.00 - $150.00",
                                "currency":"USD",
                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#"   
                            },
                            {
                                "price":"$150.00 - $200.00",
                                "currency":"USD",
                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#"   
                            },
                            {
                                "price":"$200.00+",
                                "currency":"USD",
                                "url":"https://preview.colorlib.com/theme/cozastore/index.html#"   
                            }
                            
                        ],
                        "color":[
                            {
                                "text":"black",
                                "icon":"zimdi zimdi circle black"
                            },
                            {
                                "text":"ble",
                                "icon":"zimdi zimdi circle blue"
                            },
                            {
                                "text":"grey",
                                "icon":"zimdi zimdi circle grey"
                            },
                            {
                                "text":"grenn",
                                "icon":"zimdi zimdi circle green"
                            },
                            {
                                "text":"red",
                                "icon":"zimdi zimdi circle red"
                            },
                            {
                                "text":"white",
                                "icon":"zimdi zimdi circle white"
                            }
                           
                        ],
                        "tags":[
                            {
                                "textbutton":"Fashion",
                                "url":"https://preview.colorlib.com/theme/cozastore/about.html"
                            },
                            {
                                "textbutton":"Denim",
                                "url":"https://preview.colorlib.com/theme/cozastore/about.html"
                            },
                            {
                                "textbutton":"Crafts",
                                "url":"https://preview.colorlib.com/theme/cozastore/about.html"
                            },
                            {
                                "textbutton":"lifestyle",
                                "url":"https://preview.colorlib.com/theme/cozastore/about.html"
                            },
                            {
                                "textbutton":"streetstyle",
                                "url":"https://preview.colorlib.com/theme/cozastore/about.html"
                            }
                        ]
                           
                        
                    }
                ]

            }
           
        },
        {
            "search":{
                "placeholder":"search",
                "icon":"zimdi zimdi search",
                "hover":{
                    "icon":"zimdi zimdi search",
                    "placeholder":"search",
                    "value":null
                }
            }
        }
    ]
}
            ]
        }


class Allproduct(Resource):
    def get(self):
        return{
            "data":[
                {
                                    "allproduct":[
                                        {
                                            "id":1,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-01.jpg.pagespeed.ic.6WHvZRJRuO.webp",
                                            "name":"Esprit Ruffle Shirt",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":16.64,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                            
                                        },
                                        {
                                            "id":2,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-02.jpg.pagespeed.ic._mIojWDfEX.webp",
                                            "name":"Herschel supply",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":35.31,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":1,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-03.jpg.pagespeed.ic.eOHs429Gtb.webp",
                                            "name":"Only Check Trouser",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":25.50,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"men"
                                        },
                                        {
                                            "id":3,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-04.jpg.pagespeed.ic.1MaP4euDx9.webp",
                                            "name":"Classic Trench Coat",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":75.00,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":4,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-05.jpg.pagespeed.ic.GHcB3Nc9zp.webp",
                                            "name":"Front Pocket Jumper",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":34.75,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":1,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-06.jpg.pagespeed.ic.mU9c3gp9yp.webp",
                                            "name":"Vintage Inspired Classic",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":93.20,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"watches"
                                        },
                                        {
                                            "id":5,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-07.jpg.pagespeed.ic.wXz93SW1CF.webp",
                                            "name":"Shirt in Stretch Cotton",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":52.66,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":6,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-08.jpg.pagespeed.ic.zcR_ZfXlFq.webp",
                                            "name":"Shirt in Stretch Cotton",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":18.96,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":1,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-09.jpg.pagespeed.ic._ex9y9IVR9.webp",
                                            "name":"Converse All Star Hi Plimsolls",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":75.00,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"shoes"
                                        },
                                        {
                                            "id":7,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-10.jpg.pagespeed.ic.JKjq4oUn3E.webp",
                                            "name":"Femme T-Shirt In Stripe",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":25.85,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-11.jpg.pagespeed.ic.fJxJBqHZzv.webp",
                                            "name":"Herschel supply",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":63.16,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"men"
                                        },
                                        {
                                            "id":2,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-12.jpg.pagespeed.ic.Ft0-TDvq7W.webp",
                                            "name":"Herschel supply",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":63.16,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"men"
                                        },
                                        {
                                            "id":8,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-13.jpg.pagespeed.ic.jIjGx2QblE.webp",
                                            "name":"T-Shirt with Sleeve",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":18.49,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":9,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-14.jpg.pagespeed.ic.rUWpWgkkYK.webp",
                                            "name":"Pretty Little Thing",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":54.79,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":2,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-15.jpg.pagespeed.ic.LNG1pmoqOY.webp",
                                            "name":"Mini Silver Mesh Watch",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":86.85,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"watches"
                                        },
                                        {
                                            "id":10,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-16.jpg.pagespeed.ic.AbLwZITYaU.webp",
                                            "name":"Square Neck Back",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":29.64,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"


                                             
                                        }
                                       
                                    ],
                                    "Women":[
                                        {
                                            "id":1,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-01.jpg.pagespeed.ic.6WHvZRJRuO.webp",
                                            "name":"Esprit Ruffle Shirt",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":16.64,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                            
                                        },
                                        {
                                            "id":2,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-02.jpg.pagespeed.ic._mIojWDfEX.webp",
                                            "name":"Herschel supply",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":35.31,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":3,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-04.jpg.pagespeed.ic.1MaP4euDx9.webp",
                                            "name":"Classic Trench Coat",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":75.00,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":4,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-05.jpg.pagespeed.ic.GHcB3Nc9zp.webp",
                                            "name":"Front Pocket Jumper",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":34.75,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":5,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-07.jpg.pagespeed.ic.wXz93SW1CF.webp",
                                            "name":"Shirt in Stretch Cotton",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":52.66,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":6,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-08.jpg.pagespeed.ic.zcR_ZfXlFq.webp",
                                            "name":"Shirt in Stretch Cotton",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":18.96,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":7,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-10.jpg.pagespeed.ic.JKjq4oUn3E.webp",
                                            "name":"Femme T-Shirt In Stripe",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":25.85,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":9,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-13.jpg.pagespeed.ic.jIjGx2QblE.webp",
                                            "name":"T-Shirt with Sleeve",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":18.49,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        },
                                        {
                                            "id":10,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-14.jpg.pagespeed.ic.rUWpWgkkYK.webp",
                                            "name":"Pretty Little Thing",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":54.79,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"women"
                                        }

                                    ],
                                    "men":[
                                        {
                                            "id":1,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-03.jpg.pagespeed.ic.eOHs429Gtb.webp",
                                            "name":"Only Check Trouser",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":25.50,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"men"
                                        },
                                        {
                                            "id":2,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-11.jpg.pagespeed.ic.fJxJBqHZzv.webp",
                                            "name":"Herschel supply",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":63.16,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"men"
                                        },
                                        {
                                            "id":3,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-12.jpg.pagespeed.ic.Ft0-TDvq7W.webp",
                                            "name":"Herschel supply",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":63.16,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"men"
                                        }
                                    ],
                                    "BAG":[
                                        {
                                            "VALUE":null
                                        }
                                    ],
                                    "Shoes":[
                                        {
                                            "id":1,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-09.jpg.pagespeed.ic._ex9y9IVR9.webp",
                                            "name":"Converse All Star Hi Plimsolls",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":75.00,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"shoes"
                                        }
                                    ],
                                    "Watches":[
                                        {
                                            "id":1,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-06.jpg.pagespeed.ic.mU9c3gp9yp.webp",
                                            "name":"Vintage Inspired Classic",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":93.20,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"watches"
                                        },
                                        {
                                            "id":2,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-15.jpg.pagespeed.ic.LNG1pmoqOY.webp",
                                            "name":"Mini Silver Mesh Watch",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":86.85,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"watches"
                                        }
                                    ]
                                }
            ]
        }

class Women(Resource):
    def get(self):
        return{
            "data":[
                {
                    "Women":[
                        {
                            "id":1,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-01.jpg.pagespeed.ic.6WHvZRJRuO.webp",
                            "name":"Esprit Ruffle Shirt",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":16.64,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                            
                        },
                        {
                            "id":2,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-02.jpg.pagespeed.ic._mIojWDfEX.webp",
                            "name":"Herschel supply",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":35.31,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        },
                        {
                            "id":3,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-04.jpg.pagespeed.ic.1MaP4euDx9.webp",
                            "name":"Classic Trench Coat",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":75.00,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        },
                        {
                            "id":4,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-05.jpg.pagespeed.ic.GHcB3Nc9zp.webp",
                            "name":"Front Pocket Jumper",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":34.75,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        },
                        {
                            "id":5,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-07.jpg.pagespeed.ic.wXz93SW1CF.webp",
                            "name":"Shirt in Stretch Cotton",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":52.66,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        },
                        {
                            "id":6,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-08.jpg.pagespeed.ic.zcR_ZfXlFq.webp",
                            "name":"Shirt in Stretch Cotton",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":18.96,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        },
                        {
                            "id":7,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-10.jpg.pagespeed.ic.JKjq4oUn3E.webp",
                            "name":"Femme T-Shirt In Stripe",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":25.85,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        },
                        {
                            "id":9,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-13.jpg.pagespeed.ic.jIjGx2QblE.webp",
                            "name":"T-Shirt with Sleeve",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":18.49,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        },
                        {
                            "id":10,
                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-14.jpg.pagespeed.ic.rUWpWgkkYK.webp",
                            "name":"Pretty Little Thing",
                            "button":[
                                {
                                    "text":"quick view",
                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                    "afterclick":[
                                        {
                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                            "name":"Lightweight Jacket",
                                            "price":"$58.79",
                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                            "size":{
                                                "option":["Size S","Size M","Size L","size XL"]
                                            },
                                            "color":["red","blue","white","grey"],
                                            "numbproduct":[
                                                {
                                                    "icon1":"zmdi minus",
                                                    "type":"number",
                                                    "value":1,
                                                    "icon2":"zmdi plus"
                                                }
                                            ]
                                        },
                                        {
                                            "button":{
                                                "text":"ad to cart"
                                            }
                                        },
                                        {
                                            "icon":"love",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"addto wishlist"
                                        },
                                        {
                                            "icon":"facebook",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"facebook"
                                        },
                                        {
                                            "icon":"twiter",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"twiter"
                                        },
                                        {
                                            "icon":"google plus",
                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "respon":"Google Plus"
                                        }
                                    ]
                                }
                                
                            ],
                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                            "price":54.79,
                            "currency":"USD",
                            "icon":"favorite",
                            "category":"women"
                        }

                    ],
                }
            ]
        }

class Men(Resource):
    def get(self):
        return{
            "data":[
                {
                    "men":[
                                        {
                                            "id":1,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-03.jpg.pagespeed.ic.eOHs429Gtb.webp",
                                            "name":"Only Check Trouser",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":25.50,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"men"
                                        },
                                        {
                                            "id":2,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-11.jpg.pagespeed.ic.fJxJBqHZzv.webp",
                                            "name":"Herschel supply",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":63.16,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"men"
                                        },
                                        {
                                            "id":3,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-12.jpg.pagespeed.ic.Ft0-TDvq7W.webp",
                                            "name":"Herschel supply",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":63.16,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"men"
                                        }
                                    ],
                }
            ]
        }

class Watches(Resource):
    def get(self):
        return{
            "data":[
                {
                    "Watches":[
                                        {
                                            "id":1,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-06.jpg.pagespeed.ic.mU9c3gp9yp.webp",
                                            "name":"Vintage Inspired Classic",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":93.20,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"watches"
                                        },
                                        {
                                            "id":2,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-15.jpg.pagespeed.ic.LNG1pmoqOY.webp",
                                            "name":"Mini Silver Mesh Watch",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":86.85,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"watches"
                                        }
                                    ]
                }
            ]
        }

    def post(self):
        some_json = request.get_json()
        return {'You sent : ': some_json}, 201

class Shoes(Resource):
    def get(self):
        return{
            "data"[
                {
                     "Shoes":[
                                        {
                                            "id":1,
                                            "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-09.jpg.pagespeed.ic._ex9y9IVR9.webp",
                                            "name":"Converse All Star Hi Plimsolls",
                                            "button":[
                                                {
                                                    "text":"quick view",
                                                    "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                    "afterclick":[
                                                        {
                                                            "image":["https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-01.jpg.pagespeed.ic.p3moSJxG7I.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-02.jpg.pagespeed.ic.1bDtXoN8v6.webp","https://preview.colorlib.com/theme/cozastore/images/xproduct-detail-03.jpg.pagespeed.ic.-rPS2k8YRO.webp"],
                                                            "name":"Lightweight Jacket",
                                                            "price":"$58.79",
                                                            "deskripsi":"Nulla eget sem vitae eros pharetra viverra. Nam vitae luctus ligula. Mauris consequat ornare feugiat.",
                                                            "size":{
                                                                "option":["Size S","Size M","Size L","size XL"]
                                                            },
                                                            "color":["red","blue","white","grey"],
                                                            "numbproduct":[
                                                                {
                                                                    "icon1":"zmdi minus",
                                                                    "type":"number",
                                                                    "value":1,
                                                                    "icon2":"zmdi plus"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "button":{
                                                                "text":"ad to cart"
                                                            }
                                                        },
                                                        {
                                                            "icon":"love",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"addto wishlist"
                                                        },
                                                        {
                                                            "icon":"facebook",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"facebook"
                                                        },
                                                        {
                                                            "icon":"twiter",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"twiter"
                                                        },
                                                        {
                                                            "icon":"google plus",
                                                            "url":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                                            "respon":"Google Plus"
                                                        }
                                                    ]
                                                }
                                                
                                            ],
                                            "butoonurl":"https://preview.colorlib.com/theme/cozastore/index.html#",
                                            "nameurl":"https://preview.colorlib.com/theme/cozastore/product-detail.html",
                                            "price":75.00,
                                            "currency":"USD",
                                            "icon":"favorite",
                                            "category":"shoes"
                                        }
                                    ],
                }
            ]
        }

class Features(Resource):
    def get(self):
        return{
            "data":[
                {
    "pesanan":[
        {
            "product":[
                {
                    "image":"data:image/webp;base64,UklGRsADAABXRUJQVlA4ILQDAABwEQCdASo8AFAAPmkqj0WkIqEbOb4AQAaEswBiSkeDkH5edQG+iDbL87d6Hehp9W70AOlsn3bPnwF2ly/Hztvl9Zv/Q8wP1GoYsJap2Lhc43wNlFyZAhrRlF8iv1w+ahHHgV0GEIkU0+63ze2u2TK1yq8KeZRROJSaS8aY0Ij8urQGWUp6og46e+XghkuJ8/70ilEAAP78hrCiyAIvxF0XyGBx73TyVMtmk0dc9WVfPa+jU4vlFw7PJomDFITtXM7F/GBwa8XIH+H6u6Lww27AW2WQuLBA5lx1u75hz98IkGtIkJh85Gigg3zfP/NAeRrEBahAO8Jfw5y+RY/ovATT7O/d7xzXjykR6Pinq1sz/G6BtcKmd+ecF8YbwUGPqTbpo5Qo/y/T+n/HuKieqP+T5AWFjbqMuywwYbJbqm8SnoXH/2JVkzq62L+a1l0hLcOJXEOv8ggnsYSjtKj6gzNWA+RwwjGDpzuK0c9MitwIqUIKfECYtvhXVwYBB2Cylkno/E3upBw9kFw3oqmEeBX84hIpfYf1q/4LaUL0qUCIzQ/RcJVy5iu1hE6a1TYrIeNMgkFb8BHxx/RjRqprK2QOmnnlH/iHsKREmeEd1ZtWkNoQB1FlF503MkyiooHYLeBPxYESX/5jdcuzx1liiZ6e3K1mxgxx41RUYHYy91RYlH6LoGl/td42wUdZPOKHpPyiGt9vczsMMOCn9B/P3hau4Ibdoh1wtebjPv6/RwaJiSzUdxzynosQkyMuFLkp8tYmWLk3Y4GVssI9Tukq/tQp8mIRM+u+S1BjtVg28WmnbsW4PK+O2ako+T3i6/V32ozKfYqq/yd2F/7QXuABF+qMJtPL1fs5Ah9J4tc/tsiAoefyrgfEt9sVeyvPLDMT/a8sZMPqoBmfxKyxVWQ/RZH8oN6TczEwvlEqSB2BNq+aaptYpNQORkicVy6j1QTJUMn9cbFT9KOv/omxydNSo++uJMmURi005a00kVjrHuK9iF1YynB0gzr8b/mATy0N8Tv5jv2uBFtXWd9VUs3BZvPittxx9m23fylkJhB+J1BLtseFHSazcV0pJakJrstHSi7glV5F3TLgtbBz9EYE04onvlcixah+fv1A5Q0cw7Dej7uWUefw3oajgXbqmPxsB0YzC+6uIa4FfGtA0A6aRPDyz96EWes4P6Ahp9YGru4Un7csa3+lt12dcH+XD+hswImC8oxdg+AyKrW0HK2GTAEm+3z+uc7wsPQgIdfBZykpXsIwAAA=",
                    "name":"Fresh Strawberries"
                },
                {
                    "image":"data:image/webp;base64,UklGRgAEAABXRUJQVlA4IPQDAADQEQCdASo8AFAAPm0ukkYkIqGhKbVeQIANiWMAybx2C1K8+uIfhfhvYX2py/uB3bAci7GR/yPVC/2vNh9I+wR+sf/K4HdTkquYOvczsm8gIogwYDdBbaYF8/kfCzimbMQuj/yAgr7EO7OKlxCH1YmtRbt3YxRHUfOjrXm4bczkvcvIc5EDRjFzT+5d/GSia7/9eOcljuLAAP77EuqFb+W2AFW5/euNW/ltcQp6Bcm/jtOzUOWTU5bqunq5n0/tpK/3WCaqjW9JU3j9hJlMUlGO/LLvA1rPCT+M/1MeYRFm2oEYbd1GfC+FWh4m9cNYjfC2nG5J28D9R1eWBD0wFCABiSBeXIupWax9R7aPdhXxoXSJwUUp0AoXwrErFoc7qtU2wPLYYV+EAbXBhdi2Uq9t64zNU94l3JIuXxOtDuekNYt2IUNoCSeLR837+E616GHJHoe0yBVQOldp751yDP+2vOoMk3J333h/qjWktZBBYHHjH+dIFEIosfMcTRBbqe2LBbVPNsXn3v8c9B4hUFfjmD95GNYkoCa5xC4Cwg8rQqH5bHox+xaWfqua3vgMB10AI+AmYN28/Ob9PW0Oq00r6ImECSjO2mu/xX4Z/uRTrpdzB1aaTAx3hs3ek2dhtWEMPm2oEzJ0MS+OuNEfz4kL1SoEsV6gGgza1moR7TPOaqi7L/8mQdOl4Oqaiy/TZ344TBicI8jq8c75f7sw8/eU0FPm+93g5UbyBGDA0iHdbWklqUsNZKItFcMQUwfAb6FrIihz/SAjsALqWLjtw56Yekk2XTdu3wfXRljd6flcIk3zV68z7zylEVR2rY8CbKyI6eucCete0eXx31UnLMiLDasTeOa1tA+knlRDm7oYSNfzwtuCFeGu38B4WpZJo3ps3e1cE/O3IQv7Dc5MwY4m9kwSrunZUUlv20+84MvB/Lzh1ERGfKoL0oJDTft8s2FW/fDKSY+N2v3ueQHpvsOdaIZWayGZ/V8oLVdo5KX6vC/dafqjMgaIocxLOdKnHteZ6RhAZAqBipmQOv/cDnznEMxe4gNhk+MpZRdc/JKWds0h4RqPG36ZmsTaAAVHCgy8QWbgwgmoM4eG2qse1mW/sy452iHZ6H0OR/NP9LR+01KwA+q6lUlRQ9GTJb2OEmXwVaYwjuI5DrtVbEEw3RXimsoOc8X80XviSHYA77VEAMexAIsLlt22qTUxmwju/Km5pT2tuoSR5DNS35uMWfUWOoGu9InP8QXI0Nwi5Xn6TVPzYWs0NFvEb4sDvgOQ3MiKLbLvq5z9R+9rZuwj1wbpMXL9VIhrA3ofuYUr5RPjPT9OyprPHfXNuDjC4INzYJgOoAAA",
                    "name":"Lightweight Jacket"
                }
            ],
            "price":["36.00","16.00"],
            "qty":["1","1"],
            "total":["36.00","16.00"],
            "input":{
                "placeholder":"Coupen code"
            },
            "button":[
                {
                    "text":"apply coupon"
                },
                {
                    "text":"update cart"
                }
            ]
           
        
            
        }
    ],
    "cart total":[
        {
            "subtotal":79.65,
            "Shipping":"There are no shipping methods available. Please double check your address, or contact us if you need any help.",
            "calculating shipping":[
                {
                    "option country":["usa","uk"]
                },
                {
                    "input":{
                        "placeholder":"state country"

                    }
                    
                }
            ]
        },
        {
            "button":{
                "text":"update total"
            }
        },
        {
            "total":"79.65"
        },
        {
            "button2":{
                "text":"proceed to checkout"
            }
        }
    ]
}
            ]
        }

class Blog(Resource):
     def get(self):
         return{
              "data" : [
                {
    "banner":{
        "image":"data:image/webp;base64,UklGRqACAABXRUJQVlA4TJQCAAAvhAAEEH8gEEhy2p9vhZmZmYlI6DigvP//GUle0ztpu8e2nducPHOy7Vneam0zy8ZxbdverNU87bF1WqaVLudz+P3Sz0T0fwLAe/XN9Zj3fflICVx1owlcc+MyrFf/cYvDg77v+5Ww+de3pgH3+/6VDlf5vu/D/LykWcCHkr51GZQJpNVk8WJpIwVJmoeXl8IKyEi6g0CSHAYkKXTxYknaOJ6iQkvfsxNaQ6dxQjR7gsNAz9HLcs9C5sThl1UWnJ0wYQIU1POPVEuf9FVBPc5VN974qjrBk1RmjNVBsQKiWpgfV8HmuIJMJWRqgrMA5xSWklaKrFazOVYF0K1N0KxQVUamFg64tufeBYjmWkbm2QKdhav0LnHowojqgJwqoFdPaJ4RzcVqDG8y3rvTMpQwqDrMzXoWCLQO9ulbINIRpYygp3wcUa1x1beWsVrbiGosV+lO4CrthX6tBXJy4k6jMR/uSEpb9nUaXqEieNf3lzN6MfIqg0a9S1YuwL6/tTshM472tuKzBJLOMpSwWU3Ac9rLVXoWuEopIlUY8LNKbWOWc0ahqYTg7IQJDl1aB5u/fGS+eoA+NTCiOUCgzi/zqrORq7GN1BvNTWQqn2uC4CxAs76F73QneVVBTlUUVAoMy9wL7C+FqN4W3Gn07SVT2RiXJsyXbn8g1lxG1XnFn5J7l+4EyFieBaJ6iOps58ISIFdDppJ0TQJpmeVcJTPFoEyK4fbt2+MQ6HoWctU2snfAh6FrvHdn0lVGCkhLCssT9ulZIKty8OJHPgvdhGZ1tGkDhhe6QWdbWxvQGusZF5j/l3qWk9Css0CkauCFWKtI4GPpMcdCpiaQJAegBPsWh4vsTQZoxLplCUAj0OgwYcKECQA=",
        "title":"BLOG"
    },
    "Body":[
        {
            "image":"data:image/webp;base64,UklGRqACAABXRUJQVlA4TJQCAAAvhAAEEH8gEEhy2p9vhZmZmYlI6DigvP//GUle0ztpu8e2nducPHOy7Vneam0zy8ZxbdverNU87bF1WqaVLudz+P3Sz0T0fwLAe/XN9Zj3fflICVx1owlcc+MyrFf/cYvDg77v+5Ww+de3pgH3+/6VDlf5vu/D/LykWcCHkr51GZQJpNVk8WJpIwVJmoeXl8IKyEi6g0CSHAYkKXTxYknaOJ6iQkvfsxNaQ6dxQjR7gsNAz9HLcs9C5sThl1UWnJ0wYQIU1POPVEuf9FVBPc5VN974qjrBk1RmjNVBsQKiWpgfV8HmuIJMJWRqgrMA5xSWklaKrFazOVYF0K1N0KxQVUamFg64tufeBYjmWkbm2QKdhav0LnHowojqgJwqoFdPaJ4RzcVqDG8y3rvTMpQwqDrMzXoWCLQO9ulbINIRpYygp3wcUa1x1beWsVrbiGosV+lO4CrthX6tBXJy4k6jMR/uSEpb9nUaXqEieNf3lzN6MfIqg0a9S1YuwL6/tTshM472tuKzBJLOMpSwWU3Ac9rLVXoWuEopIlUY8LNKbWOWc0ahqYTg7IQJDl1aB5u/fGS+eoA+NTCiOUCgzi/zqrORq7GN1BvNTWQqn2uC4CxAs76F73QneVVBTlUUVAoMy9wL7C+FqN4W3Gn07SVT2RiXJsyXbn8g1lxG1XnFn5J7l+4EyFieBaJ6iOps58ISIFdDppJ0TQJpmeVcJTPFoEyK4fbt2+MQ6HoWctU2snfAh6FrvHdn0lVGCkhLCssT9ulZIKty8OJHPgvdhGZ1tGkDhhe6QWdbWxvQGusZF5j/l3qWk9Css0CkauCFWKtI4GPpMcdCpiaQJAegBPsWh4vsTQZoxLplCUAj0OgwYcKECQA=",
            "date":"22 jan 2018",
            "title":"8 Inspiring Ways to Wear Dresses in the Winter",
            "deskripsi":"Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Fusce eget dictum tortor. Donec dictum vitae sapien eu varius",
            "author":"By admin",
            "categpry":["StreetStyle","Fashion","Couple"],
            "usercomment":"8 coment",
            "continueread":[
                {
                    "url":"blog-detail.html",
                    "deskripsi":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc sit amet est vel orci luctus sollicitudin. Duis eleifend vestibulum justo, varius semper lacus condimentum dictum. Donec pulvinar a magna ut malesuada. In posuere felis diam, vel sodales metus accumsan in. Duis viverra dui eu pharetra pellentesque. Donec a eros leo. Quisque sed ligula vitae lorem efficitur faucibus. Praesent sit amet imperdiet ante. Nulla id tellus auctor, dictum libero a, malesuada nisi. Nulla in porta nibh, id vestibulum ipsum. Praesent dapibus tempus erat quis aliquet. Donec ac purus id sapien condimentum feugiat.Praesent vel mi bibendum, finibus leo ac, condimentum arcu. Pellentesque sem ex, tristique sit amet suscipit in, mattis imperdiet enim. Integer tempus justo nec velit fringilla, eget eleifend neque blandit. Sed tempor magna sed congue auctor. Mauris eu turpis eget tortor ultricies elementum. Phasellus vel placerat orci, a venenatis justo. Phasellus faucibus venenatis nisl vitae vestibulum. Praesent id nibh arcu. Vivamus sagittis accumsan felis, quis vulputate",
                    "tags":[
                        {
                            "button":[
                                {
                                    "text":"stretstyle",
                                    "url":"https://preview.colorlib.com/theme/cozastore/blog-detail.html"
    
                                },
                                {
                                    "text":"crafts",
                                    "url":"https://preview.colorlib.com/theme/cozastore/blog-detail.html"
    
                                }
                            ]
                            
                        }
                    ]
                }
            ],
            "Leave a comment":[
                {
                    "title":"LEAVE A COMMENT",
                    "subtitle":"Your email address will not be published. Required fields are marked *",
                    "inputcomment":{
                        "placeholder":"comment",
                        "type":"text"
                    },
                    "inputname":{
                        "placeholder":"name",
                        "type":"text"
                    },
                    "inputemail":{
                        "placeholder":"email",
                        "type":"email"
                    },
                    "inputweb":{
                        "placeholder":"website",
                        "type":"text"
                    }
                }
            ],
            "button":{
                "text":"post comment"
            }

        },
        {
            "image":"https://preview.colorlib.com/theme/cozastore/images/xblog-05.jpg.pagespeed.ic.IHqPduvAcv.webp",
            "date":"18 jan 2018",
            "title":"The Great Big List of Men’s Gifts for the Holidays",
            "deskripsi":"Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Fusce eget dictum tortor. Donec dictum vitae sapien eu varius",
            "author":"By admin",
            "categpry":["StreetStyle","Fashion","Couple"],
            "usercomment":"8 coment",
            "continueread":[
                {
                    "url":"blog-detail.html",
                    "deskripsi":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc sit amet est vel orci luctus sollicitudin. Duis eleifend vestibulum justo, varius semper lacus condimentum dictum. Donec pulvinar a magna ut malesuada. In posuere felis diam, vel sodales metus accumsan in. Duis viverra dui eu pharetra pellentesque. Donec a eros leo. Quisque sed ligula vitae lorem efficitur faucibus. Praesent sit amet imperdiet ante. Nulla id tellus auctor, dictum libero a, malesuada nisi. Nulla in porta nibh, id vestibulum ipsum. Praesent dapibus tempus erat quis aliquet. Donec ac purus id sapien condimentum feugiat.Praesent vel mi bibendum, finibus leo ac, condimentum arcu. Pellentesque sem ex, tristique sit amet suscipit in, mattis imperdiet enim. Integer tempus justo nec velit fringilla, eget eleifend neque blandit. Sed tempor magna sed congue auctor. Mauris eu turpis eget tortor ultricies elementum. Phasellus vel placerat orci, a venenatis justo. Phasellus faucibus venenatis nisl vitae vestibulum. Praesent id nibh arcu. Vivamus sagittis accumsan felis, quis vulputate",
                    "tags":[
                        {
                            "button":[
                                {
                                    "text":"stretstyle",
                                    "url":"https://preview.colorlib.com/theme/cozastore/blog-detail.html"
    
                                },
                                {
                                    "text":"crafts",
                                    "url":"https://preview.colorlib.com/theme/cozastore/blog-detail.html"
    
                                }
                            ]
                            
                        }
                    ]
                }
            ],
            "Leave a comment":[
                {
                    "title":"LEAVE A COMMENT",
                    "subtitle":"Your email address will not be published. Required fields are marked *",
                    "inputcomment":{
                        "placeholder":"comment",
                        "type":"text"
                    },
                    "inputname":{
                        "placeholder":"name",
                        "type":"text"
                    },
                    "inputemail":{
                        "placeholder":"email",
                        "type":"email"
                    },
                    "inputweb":{
                        "placeholder":"website",
                        "type":"text"
                    }
                }
            ],
            "button":{
                "text":"post comment"
            }

        },
        {
            "image":"https://preview.colorlib.com/theme/cozastore/images/xblog-06.jpg.pagespeed.ic.1HaKHRaKYn.webp",
            "date":"16 jan 2018",
            "title":"5 Winter-to-Spring Fashion Trends to Try Now",
            "deskripsi":"Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Fusce eget dictum tortor. Donec dictum vitae sapien eu varius",
            "author":"By admin",
            "categpry":["StreetStyle","Fashion","Couple"],
            "usercomment":"8 coment",
            "continueread":[
                {
                    "url":"blog-detail.html",
                    "deskripsi":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc sit amet est vel orci luctus sollicitudin. Duis eleifend vestibulum justo, varius semper lacus condimentum dictum. Donec pulvinar a magna ut malesuada. In posuere felis diam, vel sodales metus accumsan in. Duis viverra dui eu pharetra pellentesque. Donec a eros leo. Quisque sed ligula vitae lorem efficitur faucibus. Praesent sit amet imperdiet ante. Nulla id tellus auctor, dictum libero a, malesuada nisi. Nulla in porta nibh, id vestibulum ipsum. Praesent dapibus tempus erat quis aliquet. Donec ac purus id sapien condimentum feugiat.Praesent vel mi bibendum, finibus leo ac, condimentum arcu. Pellentesque sem ex, tristique sit amet suscipit in, mattis imperdiet enim. Integer tempus justo nec velit fringilla, eget eleifend neque blandit. Sed tempor magna sed congue auctor. Mauris eu turpis eget tortor ultricies elementum. Phasellus vel placerat orci, a venenatis justo. Phasellus faucibus venenatis nisl vitae vestibulum. Praesent id nibh arcu. Vivamus sagittis accumsan felis, quis vulputate",
                    "tags":[
                        {
                            "button":[
                                {
                                    "text":"stretstyle",
                                    "url":"https://preview.colorlib.com/theme/cozastore/blog-detail.html"
    
                                },
                                {
                                    "text":"crafts",
                                    "url":"https://preview.colorlib.com/theme/cozastore/blog-detail.html"
    
                                }
                            ]
                            
                        }
                    ]
                }
            ],
            "Leave a comment":[
                {
                    "title":"LEAVE A COMMENT",
                    "subtitle":"Your email address will not be published. Required fields are marked *",
                    "inputcomment":{
                        "placeholder":"comment",
                        "type":"text"
                    },
                    "inputname":{
                        "placeholder":"name",
                        "type":"text"
                    },
                    "inputemail":{
                        "placeholder":"email",
                        "type":"email"
                    },
                    "inputweb":{
                        "placeholder":"website",
                        "type":"text"
                    }
                }
            ],
            "button":{
                "text":"post comment"
            }

        }
        
    ],
    "aside":[
        {
            "search":{
                "placeholder":"search",
                "icon":"zmdi search"
            }
        },
        {
            "title":"Category",
            "category":[
                {
                    "text":"Fashion",
                    "url":"https://preview.colorlib.com/theme/cozastore/blog.html#"
                },
                {
                    "text":"Beauty",
                    "url":"https://preview.colorlib.com/theme/cozastore/blog.html#"
                },
                {
                    "text":"streetstyle",
                    "url":"https://preview.colorlib.com/theme/cozastore/blog.html#"
                },
                {
                    "text":"life style",
                    "url":"https://preview.colorlib.com/theme/cozastore/blog.html#"
                },
                {
                    "text":"diy & craft",
                    "url":"https://preview.colorlib.com/theme/cozastore/blog.html#"
                }
            ]
        },
        {
            "title":"Feature Product",
            "feature product":[
                {
                    "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-min-01.jpg.pagespeed.ic.lHpPZvVsGp.webp",
                    "name":"White Shirt With Pleat Detail Back",
                    "price":"19.00"
                },
                {
                    "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-min-02.jpg.pagespeed.ic.D3se8y8f4Q.webp",
                    "name":"Converse All Star Hi Black Canvas",
                    "price":"39.00"
                },
                {
                    "image":"https://preview.colorlib.com/theme/cozastore/images/xproduct-min-03.jpg.pagespeed.ic.-T7SdAcFBv.webp",
                    "name":"Nixon Porter Leather Watch In Tan",
                    "price":"17.00"
                }
            ]

        },
        {
            "title":"Archive",
            "archive":[
                {
                    "date":"juli 2018",
                    "jumlah":9
                },
                {
                    "date":"juni 2018",
                    "jumlah":39
                },
                {
                    "date":"may 2018",
                    "jumlah":29
                },
                {
                    "date":"april 2018",
                    "jumlah":35
                },
                {
                    "date":"march 2018",
                    "jumlah":22
                },
                {
                    "date":"february 2018",
                    "jumlah":32
                },
                {
                    "date":"januari 2018",
                    "jumlah":21
                },
                {
                    "date":"desember 2017",
                    "jumlah":26
                }
            ]
            
        },
        {
            "title":"tags",
            "tags":[
                {
                    "button":[
                        {
                            "text":"Fashion",
                            "url":"https://preview.colorlib.com/theme/cozastore/blog.html#"
                        },
                        {
                            "text":"lifestyle",
                            "url":"https://preview.colorlib.com/theme/cozastore/blog.html#"
                        },
                        {
                            "text":"denim",
                            "url":"https://preview.colorlib.com/theme/cozastore/blog.html#"
                        },
                        {
                            "text":"streetstyle",
                            "url":"https://preview.colorlib.com/theme/cozastore/blog.html#"
                        },
                        {
                            "text":"crafts",
                            "url":"https://preview.colorlib.com/theme/cozastore/blog.html#"
                        }
                    ]    
                }
            ]
        }
    ]


} 
            ]
        }

class About(Resource):
    def get(self):
        return {
            "data" : [
                {
    "banner":{
        "image":"data:image/webp;base64,UklGRqACAABXRUJQVlA4TJQCAAAvhAAEEH8gEEhy2p9vhZmZmYlI6DigvP//GUle0ztpu8e2nducPHOy7Vneam0zy8ZxbdverNU87bF1WqaVLudz+P3Sz0T0fwLAe/XN9Zj3fflICVx1owlcc+MyrFf/cYvDg77v+5Ww+de3pgH3+/6VDlf5vu/D/LykWcCHkr51GZQJpNVk8WJpIwVJmoeXl8IKyEi6g0CSHAYkKXTxYknaOJ6iQkvfsxNaQ6dxQjR7gsNAz9HLcs9C5sThl1UWnJ0wYQIU1POPVEuf9FVBPc5VN974qjrBk1RmjNVBsQKiWpgfV8HmuIJMJWRqgrMA5xSWklaKrFazOVYF0K1N0KxQVUamFg64tufeBYjmWkbm2QKdhav0LnHowojqgJwqoFdPaJ4RzcVqDG8y3rvTMpQwqDrMzXoWCLQO9ulbINIRpYygp3wcUa1x1beWsVrbiGosV+lO4CrthX6tBXJy4k6jMR/uSEpb9nUaXqEieNf3lzN6MfIqg0a9S1YuwL6/tTshM472tuKzBJLOMpSwWU3Ac9rLVXoWuEopIlUY8LNKbWOWc0ahqYTg7IQJDl1aB5u/fGS+eoA+NTCiOUCgzi/zqrORq7GN1BvNTWQqn2uC4CxAs76F73QneVVBTlUUVAoMy9wL7C+FqN4W3Gn07SVT2RiXJsyXbn8g1lxG1XnFn5J7l+4EyFieBaJ6iOps58ISIFdDppJ0TQJpmeVcJTPFoEyK4fbt2+MQ6HoWctU2snfAh6FrvHdn0lVGCkhLCssT9ulZIKty8OJHPgvdhGZ1tGkDhhe6QWdbWxvQGusZF5j/l3qWk9Css0CkauCFWKtI4GPpMcdCpiaQJAegBPsWh4vsTQZoxLplCUAj0OgwYcKECQA=",
        "title":"ABOUT"
    },
    "content":[
        {
            "title":"Our story",
            "deskripsi":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris consequat consequat enim, non auctor massa ultrices non. Morbi sed odio massa. Quisque at vehicula tellus, sed tincidunt augue. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Maecenas varius egestas diam, eu sodales metus scelerisque congue. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas gravida justo eu arcu egestas convallis. Nullam eu erat bibendum, tempus ipsum eget, dictum enim. Donec non neque ut enim dapibus tincidunt vitae nec augue. Suspendisse potenti. Proin ut est diam. Donec condimentum euismod tortor, eget facilisis diam faucibus et. Morbi a tempor elit.Donec gravida lorem elit, quis condimentum ex semper sit amet. Fusce eget ligula magna. Aliquam aliquam imperdiet sodales. Ut fringilla turpis in vehicula vehicula. Pellentesque congue ac orci ut gravida. Aliquam erat volutpat. Donec iaculis lectus a arcu facilisis, eu sodales lectus sagittis. Etiam pellentesque, magna vel dictum rutrum, neque justo eleifend elit, vel tincidunt erat arcu ut sem. Sed rutrum, turpis ut commodo efficitur, quam velit convallis ipsum, et maximus enim ligula ac ligula.Any questions? Let us know in store at 8th floor, 379 Hudson St, New York, NY 10018 or call us on (+1) 96 716 6879",
            "image":"https://preview.colorlib.com/theme/cozastore/images/xabout-01.jpg.pagespeed.ic.uzAXsYw1Qn.webp"
            
        },
        {
            "title":"Our mission",
            "deskripsi":"Mauris non lacinia magna. Sed nec lobortis dolor. Vestibulum rhoncus dignissim risus, sed consectetur erat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nullam maximus mauris sit amet odio convallis, in pharetra magna gravida. Praesent sed nunc fermentum mi molestie tempor. Morbi vitae viverra odio. Pellentesque ac velit egestas, luctus arcu non, laoreet mauris. Sed in ipsum tempor, consequat odio in, porttitor ante. Ut mauris ligula, volutpat in sodales in, porta non odio. Pellentesque tempor urna vitae mi vestibulum, nec venenatis nulla lobortis. Proin at gravida ante. Mauris auctor purus at lacus maximus euismod. Pellentesque vulputate massa ut nisl hendrerit, eget elementum libero iaculis.",
            "image":"https://preview.colorlib.com/theme/cozastore/images/xabout-02.jpg.pagespeed.ic.-BA0jt5hGo.webp",
            "quote":"Creativity is just connecting things. When you ask creative people how they did something, they feel a little guilty because they didn't really do it, they just saw something. It seemed obvious to them after a while.",
            "author":"Steve Job’s"
            
        }
    ]
}
            ]
        }

class Contact(Resource):
    def get(self):
        return {
            "data" : [
               {
    "banner":{
        "image":"data:image/webp;base64,UklGRqACAABXRUJQVlA4TJQCAAAvhAAEEH8gEEhy2p9vhZmZmYlI6DigvP//GUle0ztpu8e2nducPHOy7Vneam0zy8ZxbdverNU87bF1WqaVLudz+P3Sz0T0fwLAe/XN9Zj3fflICVx1owlcc+MyrFf/cYvDg77v+5Ww+de3pgH3+/6VDlf5vu/D/LykWcCHkr51GZQJpNVk8WJpIwVJmoeXl8IKyEi6g0CSHAYkKXTxYknaOJ6iQkvfsxNaQ6dxQjR7gsNAz9HLcs9C5sThl1UWnJ0wYQIU1POPVEuf9FVBPc5VN974qjrBk1RmjNVBsQKiWpgfV8HmuIJMJWRqgrMA5xSWklaKrFazOVYF0K1N0KxQVUamFg64tufeBYjmWkbm2QKdhav0LnHowojqgJwqoFdPaJ4RzcVqDG8y3rvTMpQwqDrMzXoWCLQO9ulbINIRpYygp3wcUa1x1beWsVrbiGosV+lO4CrthX6tBXJy4k6jMR/uSEpb9nUaXqEieNf3lzN6MfIqg0a9S1YuwL6/tTshM472tuKzBJLOMpSwWU3Ac9rLVXoWuEopIlUY8LNKbWOWc0ahqYTg7IQJDl1aB5u/fGS+eoA+NTCiOUCgzi/zqrORq7GN1BvNTWQqn2uC4CxAs76F73QneVVBTlUUVAoMy9wL7C+FqN4W3Gn07SVT2RiXJsyXbn8g1lxG1XnFn5J7l+4EyFieBaJ6iOps58ISIFdDppJ0TQJpmeVcJTPFoEyK4fbt2+MQ6HoWctU2snfAh6FrvHdn0lVGCkhLCssT9ulZIKty8OJHPgvdhGZ1tGkDhhe6QWdbWxvQGusZF5j/l3qWk9Css0CkauCFWKtI4GPpMcdCpiaQJAegBPsWh4vsTQZoxLplCUAj0OgwYcKECQA=",
        "title":"ABOUT"
    },
    "body":[
        {
            "left":[
                {
                    "title":"Send Us A Message",
                    "massage":[
                        {
                            "email":{
                                "icon":"zmd message",
                                "placeholder":"your email address"
                            }
                        },
                        {
                            "feedback":{
                                "placeholder":"how can we help?"
                            }
                        }
                    ]
                    
                },
                {
                    "button":{
                        "text":"submit",
                        "url":"https://preview.colorlib.com/theme/cozastore/contact.html?email=&msg="
                    }
                }
            ]
            
        },
        {
            "right":[
                {
                    "alamat":{
                        "icon":"zmdi loaction",
                        "text":"address",
                        "deskripsi":"Coza Store Center 8th floor, 379 Hudson St, New York, NY 10018 US"
                    }
                },
                {
                    "lets talk":{
                        "icon":"zmdi telepon",
                        "telepon":"+1 800 1236879"
                        
                    }
                },
                {
                    "sale suport":{
                        "icon":"zmdi massage",
                        "email":"contact@example.com"  
                    }
                }
            ]
        }
        
    ],
    "maps":"https://maps.googleapis.com/maps/api/js?key=AIzaSyAKFWBqlKAGCeS1rMVoaNlwyayu0e0YRes"
}
            ]
        }
           

api.add_resource(Home, '/v1/Home/')
api.add_resource(Shop, '/v1/Shop//')
api.add_resource(Allproduct, '/v1/Allproduct/')
api.add_resource(Women, '/v1/Women/')
api.add_resource(Men, '/v1/men/')
api.add_resource(Watches, '/v1/Watches/')
api.add_resource(Features, '/v1/features/')
api.add_resource(Blog, '/v1/blog/')
api.add_resource(About, '/v1/about/')
api.add_resource(Contact, '/v1/contact/')



@app.errorhandler(404)
def page_not_found(e):
    return {"error":"not found end point"}, 404

if __name__ == '__main__':
    app.run(debug=True)