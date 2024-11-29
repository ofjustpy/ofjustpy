js  files
---------
#. /static/{csr_bundle_dir}style.css
#. /templates/js/comm_channel.js
   - uses the javascript raw manipuation to update -- unlike svelte based used in CSR
#. /templates/js/event_handler_ssr.js


#. There is bunch of duplicate between
   - comm_channel.js
     and
   - justpy_core.js
     
For csr -- the justpy_core.js code are being used.

We need a massive cleanup.

