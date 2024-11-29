import ofjustpy as oj

cart_items_cookie_cfg = oj.cookie_cfg("cart_items",
           )

user_prefs_cookie_cfg = oj.cookie_cfg("user_prefs",
           )



app  = oj.build_app(cookie_cfg_iter= [cart_items_cookie_cfg,
                                      user_prefs_cookie_cfg
                                      ],

                    cookie_signer_secret_keys = ["dummydummydummydummy", "dummydummydummydummy"]
                    )
