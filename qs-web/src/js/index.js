$(document).ready(function(){

  initialize();
  var listOfDisplayedStocks = [];

  function initialize(){
    /*
      Step 1: Make sure to create a UniqueID or Session Key
      Step 2: Make an API call on server with the above UniqueID to create a PublishStream on Crossbar
      Step 3: Subscribe to the PublishStream created above
      Step 4: Fetch the StockPrice Packets from the Queue
      Step 5: Open the packet, parse the type and update coresponding DOM elements
      Step 5.1 : If type, UserPicks -create the Column Entry
      Step 5.2 : If type, Trends - update the Trending table
      Step 5.3 : If type, Toppicks - update the Top Picks table
    */
    /*Typeahead Scripts*/

    var stockPicks = [
                          "Honeywell International Inc.",
                          "Apple Inc.",
                          "Alphabet Inc.",
                          "Microsoft Corporation",
                          "Facebook Inc.",
                          "Intel Corporation",
                          "Oracle Corporation"
                      ];
    $('#search-stocks').typeahead({source:stockPicks, items:4});

    /*Initialize Alertify*/
    alertify.set('notifier','position', 'top-right');
    alertify.set('notifier','delay', 3);

    // Register for Google Cloud Messaging Notifications
    if ('serviceWorker' in navigator) {
      console.log('Service Worker is supported');
      navigator.serviceWorker.register('pushserviceworker.js').then(function(reg){
            console.log('Registered Service Worker', reg);
            reg.pushManager.subscribe({
                        userVisibleOnly: true //This tells the browser that a notification will always be shown when a push message is received. Currently it’s mandatory to show a notification.
                      }).then(function(sub) {
                        console.log('endpoint:', sub.endpoint);
                      });
                  }).catch(function(err) {
                        console.log('Something went wrong while registering Service Worker', err);
                  });
      }
      // Register for WAMP + Crossbar Events
      console.log("Ok, Autobahn loaded", autobahn.version);
	    var connection = new autobahn.Connection({url: "wss://demo.crossbar.io/ws",
     										  realm: "realm1"
     							});

      connection.onopen = function (session, details) {
      	  function onStockUpdate(args) {
                receivedStockUpdate = args[0];
                console.log("StockUpdate:", receivedStockUpdate);
                receivedStockKey = receivedStockUpdate['stock_unit'];
                if(!(listOfDisplayedStocks.includes(receivedStockKey))){
                  createUserPicks(receivedStockKey, receivedStockUpdate);
                }else{
                  updateUserPicks(receivedStockKey, receivedStockUpdate);
                }
      	  }
      	  session.subscribe("com.quickstocks.publisher.praneesh", onStockUpdate);
    	};

    	connection.onclose = function (reason, details) {
    	   console.log("Connection lost to Crossbar Server");
    	}
    	connection.open();
  }

  $('#searchBtn').on('click', function(event) {
      onStockOptionSearchUpdate();
  });

  $('#search-stocks').on('keypress', function(event) {
        var key = event.which;
        if(key == 13)  // the enter key code
        {
          onStockOptionSearchUpdate();
        }
  });

  function onStockOptionSearchUpdate(){
    var companySelected = $('#search-stocks').val();
    // Call the Quick Stocks endpoint to update the selection in JSON
    if(companySelected == ""){
       alertify.warning('Please choose a company from search box.');
       return;
    }
    var payloadData = new Object();
    payloadData.stock_company = companySelected;
    alertify.success('Updating your stock preferences.');
    $.ajax({
          method: "PUT",
          url: "http://127.0.0.1:5000/qs/stocks/preferences/praneesh",
          dataType:'json',
          contentType:'application/json',
          data: JSON.stringify(payloadData)
        }).done(function( msg ) {
            alertify.success('Stock Preferences Updated');
        }).fail(function() {
            alertify.error('Oops ! Could not update your stock preferences. Please try again !');
        });
   }
  /*
      This creates a User Picks for the user Selected Stocks
  */
  function createUserPicks(stockKey, stockObject){
    // Update the List with the DIsplayed Element
    listOfDisplayedStocks.push(stockKey);

    var elmUserPicksRow = $("#widget-rows-userpicks");
    if(elmUserPicksRow == null){
      console.log("Could not get the User Pick row !");
      return;
    }
    /*
      THIS IS GOING TO BE A LONG LONG LONG FUNCTION.... BREAK IT !!!
    */

    // Hide the welcome-note
    $("#default-welcome-text")[0].style.display = 'none';

    // Step 1: Create a Widget elements
    var elmStockWidget = $(document.createElement('div'));
    elmStockWidget.addClass("widget");

    // Step 1.1 : Widget Header
    var elmStockWidgetHeader = $(document.createElement('div'));
    elmStockWidgetHeader.addClass('widget-header');

    var stockWidgetID = 'widget-header-'+stockKey;
    elmStockWidgetHeader.attr('id', stockWidgetID);
    elmStockWidgetHeader.append("<i class='icon-bookmark'></i>");

    var stockWidgetTitle = "<h3>" + stockObject['stock_title'] + "</h3>" ;
    elmStockWidgetHeader.append(stockWidgetTitle);

    // Step 1.2 : Widget Body
    var elmStockWidgetContent = $(document.createElement('div'));
    elmStockWidgetContent.addClass('widget-content');

    var elmStockWidgetContentRow = $(document.createElement('div'));
    elmStockWidgetContentRow.addClass('row');

    //Step 1.3 : Create Stock Price Display DOM
    var elmStockWidgetPriceColumn = $(document.createElement('div'));
    elmStockWidgetPriceColumn.addClass('col-md-10');

    // Stock Price
    elmStockWidgetPriceColumn.append(getStockWidgetPrice(stockObject));

    // Sub Notes 1 - Equity
    var elmStockWidgetSubNote_1 = $(document.createElement('div'));
    elmStockWidgetSubNote_1.addClass('widget-stock-price-subnote');
    var elmStockWidgetSubNote_1_id = 'widget-stock-price-sn-equity-' + stockKey;
    elmStockWidgetSubNote_1.attr('id', elmStockWidgetSubNote_1_id);
    elmStockWidgetSubNote_1.append(stockObject['stock_equity']);
    elmStockWidgetPriceColumn.append(elmStockWidgetSubNote_1);

    // Sub Notes 2 - Date Time
    var elmStockWidgetSubNote_2 = $(document.createElement('div'));
    elmStockWidgetSubNote_2.addClass('widget-stock-price-subnote');
    var elmStockWidgetSubNote_2_id = 'widget-stock-price-sn-time-' + stockKey;
    elmStockWidgetSubNote_2.attr('id', elmStockWidgetSubNote_2_id);
    elmStockWidgetSubNote_2.append(stockObject['stock_last_update_time']);
    elmStockWidgetPriceColumn.append(elmStockWidgetSubNote_2);
    elmStockWidgetContentRow.append(elmStockWidgetPriceColumn);

    //Step 1.3.2 : Create Stock Logo
    var elmStockWidgetLogoColumn = $(document.createElement('div'));
    elmStockWidgetLogoColumn.addClass('col-md-2');
    elmStockWidgetLogoColumn.append(getStockValueLogo(stockKey));
    elmStockWidgetContentRow.append(elmStockWidgetLogoColumn);
    elmStockWidgetContent.append(elmStockWidgetContentRow);

    // ROW 2 for more Stock Week Range !!
    var elmStockRangeRow = $(document.createElement('div'));
    elmStockRangeRow.addClass('row');

    var elmStockRangeRowColumn = $(document.createElement('div'));
    elmStockRangeRowColumn.addClass('col-md-12');
    elmStockRangeRowColumn.append(getStockRangeTable(stockObject));
    elmStockRangeRow.append(elmStockRangeRowColumn);
    elmStockWidgetContent.append(elmStockRangeRow);

    // Row 3 for Stock Properties...!
    // ROW 3 Colum 1 for more Stock Properties !!
    var elmStockPropRow = $(document.createElement('div'));
    elmStockPropRow.addClass('row');
    var elmStockPropRowColumn = $(document.createElement('div'));
    elmStockPropRowColumn.addClass('col-md-6');
    elmStockPropRowColumn.append(getStockParametersTableColumn_One(stockObject));
    elmStockPropRow.append(elmStockPropRowColumn);

    // ROW 3 Colum 2 for more Stock Properties !!
    var elmStockPropRowColumnTwo = $(document.createElement('div'));
    elmStockPropRowColumnTwo.addClass('col-md-6');
    elmStockPropRowColumnTwo.append(getStockParametersTableColumn_Two(stockObject));
    elmStockPropRow.append(elmStockPropRowColumnTwo);

    elmStockWidgetContent.append(elmStockPropRow);


    // Updating the Widget Content
    elmStockWidget.append(elmStockWidgetHeader);
    elmStockWidget.append(elmStockWidgetContent);

    // Create the Column Element
    var elmStockWidgetColumn = $(document.createElement('div'));
    elmStockWidgetColumn.addClass("col-md-6");  //Bootstrap Class - Explore better ways of doing this
    elmStockWidgetColumn.append(elmStockWidget);

    // Add the above column to the UserPicks row
    elmUserPicksRow.append(elmStockWidgetColumn);
  }

  function updateUserPicks(stockKey, stockObject){
    // Update Stock Price
    var elemStockPriceElement_id = "#widget-stock-price-"+stockKey;
    $(elemStockPriceElement_id)[0] = getStockWidgetPrice(stockObject);

    // Update Stock Price
    var elemStockSubNoteCloseTime_id = "#widget-stock-price-sn-time-"+stockKey;
    $(elemStockSubNoteCloseTime_id)[0].innerHTML = stockObject["stock_last_update_time"];
  }

  function createTopPicksForUser(topPickStockElement){
      var elmUserTopPicksRow = $("#widget-rows-toppicks");
      if(elmUserTopPicksRow == null){
        console.log("Could not get the Top Users Pick row !");
        return;
      }

      elmStockWidget = $(document.createElement('div'));
      elmStockWidget.addClass("widget");

      // Step 1.1 : Widget Header
      elmStockWidgetHeader = $(document.createElement('div'));
      elmStockWidgetHeader.addClass('widget-header');
      elmStockWidgetHeader.attr('id','widget-toppick-header-PRAN');
      elmStockWidgetHeader.append("<i class='icon-bookmark'></i>");
      elmStockWidgetHeader.append("<h3>Lexicon Pharma. Inc. (LXRX)</h3>");

      // Step 1.2 : Widget Body
      elmStockWidgetContent = $(document.createElement('div'));
      elmStockWidgetContent.addClass('widget-content');

      elmStockWidgetContentRow = $(document.createElement('div'));
      elmStockWidgetContentRow.addClass('row');

      //Step 1.3 : Create Stock Price Display DOM
      elmStockWidgetPriceColumn = $(document.createElement('div'));
      elmStockWidgetPriceColumn.addClass('col-md-10');
      // Stock Price
      elmStockWidgetPriceColumn.append(getStockWidgetPrice());
      elmStockWidgetContent.append(elmStockWidgetContentRow);


      // Create the Column Element
      elmStockWidgetColumn = $(document.createElement('div'));
      elmStockWidgetColumn.addClass("col-md-4");  //Bootstrap Class - Explore better ways of doing this
      elmStockWidgetColumn.append(elmStockWidget);

      // Updating the Widget Content
      elmStockWidget.append(elmStockWidgetHeader);
      elmStockWidget.append(elmStockWidgetContent);
      // Add the above column to the UserPicks row
      elmStockWidgetColumn.append(elmStockWidget);
      elmUserTopPicksRow.append(elmStockWidgetColumn);
  }

  function getStockWidgetPrice(stockObject){
    var elmStockWidgetPrice = $(document.createElement('div'));
    elmStockWidgetPrice.addClass('widget-stock-price');
    var elmStockWidgetPrice_id = 'widget-stock-price-' + stockObject['stock_unit'];
    elmStockWidgetPrice.attr('id',elmStockWidgetPrice_id);
    elmStockWidgetPrice.append("<span>" + stockObject['stock_price'] +"</span>");

    var elmStockWidgetStats = $(document.createElement('span'));
    if(stockObject['stock_deviation_status'] == 'Decline'){
      elmStockWidgetStats.addClass('widget-stock-deviation-decline');
    }else{
      elmStockWidgetStats.addClass('widget-stock-deviation-rise');
    }

    var elmStockWidgetStats_id = 'widget-stock-status-' + stockObject['stock_unit'];
    elmStockWidgetStats.attr('id',elmStockWidgetStats_id);
    elmStockWidgetStats.append("<span> "+ stockObject['stock_deviation'] +" </span>");
    elmStockWidgetPrice.append(elmStockWidgetStats);

    return elmStockWidgetPrice;
  }

  function getStockValueLogo(stockKey){
    elmStockWidgetLogo = $(document.createElement('div'));
    elmStockWidgetLogo.addClass('widget-stock-price-logo');
    elmStockWidgetLogo_id = 'widget-stock-price-logo-' + stockKey;
    elmStockWidgetLogo.attr('id',elmStockWidgetLogo_id);
    elmStockWidgetLogo.append(stockKey[0]);
    return elmStockWidgetLogo;
  }

  function getStockRangeTable(stockObject){
    // 52 Wk Row Table
    var elmStockRangeTable = $(document.createElement('table'));
    elmStockRangeTable.addClass('table table-condensed');

    var elmStockRangeTableRow = $(document.createElement('tr'));
    var elmStockRangeTitleTableColumn = $(document.createElement('td'));
    elmStockRangeTitleTableColumn.append('52wk Range');

    var elmStockRangeValueTableColumn = $(document.createElement('td'));
    elmStockRangeValueTableColumn.attr('width','35%');
    var elmStockRangeValueTableColumn_id = 'widget-tbl-52wk-' + stockObject['stock_unit'];
    elmStockRangeValueTableColumn.attr('id',elmStockRangeValueTableColumn_id)
    elmStockRangeValueTableColumn.append(stockObject['stock_52wkrange']);

    elmStockRangeTableRow.append(elmStockRangeTitleTableColumn);
    elmStockRangeTableRow.append(elmStockRangeValueTableColumn);
    elmStockRangeTable.append(elmStockRangeTableRow)

    return elmStockRangeTable;
  }

  function getStockParametersTableColumn_One(stockObject){
    // Rest of the parameters
    var elmStockParametersTable = $(document.createElement('table'));
    elmStockParametersTable.addClass('table table-condensed');

    // Col 1 Row 1    :: StockOpen
    var elmStockPropOpenTableRow = $(document.createElement('tr'));
    var elmStockPropOpenTitleTableColumn = $(document.createElement('td'));
    elmStockPropOpenTitleTableColumn.append('Open');
    elmStockPropOpenTableRow.append(elmStockPropOpenTitleTableColumn);

    var elmStockPropOpenValueTableColumn = $(document.createElement('td'));
    elmStockPropOpenValueTableColumn.attr('width','25%');
    var elmStockPropOpenValueTableColumn_id = 'widget-tbl-open-' + stockObject['stock_unit'];
    elmStockPropOpenValueTableColumn.attr('id',elmStockPropOpenValueTableColumn_id);
    elmStockPropOpenValueTableColumn.append(stockObject['stock_open']);
    elmStockPropOpenTableRow.append(elmStockPropOpenValueTableColumn);
    elmStockParametersTable.append(elmStockPropOpenTableRow)

    // Col 1 Row 2    :: StockPrevClose
    var elmStockPropPrevCloseTableRow = $(document.createElement('tr'));
    var elmStockPropPrevCloseTitleTableColumn = $(document.createElement('td'));
    elmStockPropPrevCloseTitleTableColumn.append('Prev Close');
    elmStockPropPrevCloseTableRow.append(elmStockPropPrevCloseTitleTableColumn);

    var elmStockPropPrevCloseValueTableColumn = $(document.createElement('td'));
    elmStockPropPrevCloseValueTableColumn.attr('width','25%');
    var elmStockPropPrevCloseValueTableColumn_id = 'widget-tbl-prevclose-' + stockObject['stock_unit'];
    elmStockPropPrevCloseValueTableColumn.attr('id',elmStockPropPrevCloseValueTableColumn_id);
    elmStockPropPrevCloseValueTableColumn.append(stockObject['stock_prev_close']);
    elmStockPropPrevCloseTableRow.append(elmStockPropPrevCloseValueTableColumn);
    elmStockParametersTable.append(elmStockPropPrevCloseTableRow)
    //elmStockPropRowColumn.append(elmStockParametersTable);

    return elmStockParametersTable;
  }

  function getStockParametersTableColumn_Two(stockObject){

    // Rest of the parameters
    var elmStockParametersTable = $(document.createElement('table'));
    elmStockParametersTable.addClass('table table-condensed');

    // Col 1 Row 1
    var elmStockPropOpenTableRow = $(document.createElement('tr'));
    var elmStockPropOpenTitleTableColumn = $(document.createElement('td'));
    elmStockPropOpenTitleTableColumn.append('Market Cap');
    elmStockPropOpenTableRow.append(elmStockPropOpenTitleTableColumn);

    var elmStockPropOpenValueTableColumn = $(document.createElement('td'));
    elmStockPropOpenValueTableColumn.attr('width','25%');
    var elmStockPropOpenValueTableColumn_id = 'widget-tbl-mcap-' + stockObject['stock_unit'];
    elmStockPropOpenValueTableColumn.attr('id',elmStockPropOpenValueTableColumn_id);
    elmStockPropOpenValueTableColumn.append(stockObject['stock_market_cap']);
    elmStockPropOpenTableRow.append(elmStockPropOpenValueTableColumn);
    elmStockParametersTable.append(elmStockPropOpenTableRow)

    // Col 1 Row 2
    var elmStockPropPrevCloseTableRow = $(document.createElement('tr'));
    var elmStockPropPrevCloseTitleTableColumn = $(document.createElement('td'));
    elmStockPropPrevCloseTitleTableColumn.append('P/E Ratio (ttm)');
    elmStockPropPrevCloseTableRow.append(elmStockPropPrevCloseTitleTableColumn);

    var elmStockPropPrevCloseValueTableColumn = $(document.createElement('td'));
    elmStockPropPrevCloseValueTableColumn.attr('width','25%');
    var elmStockPropPrevCloseValueTableColumn_id = 'widget-tbl-ttm-' + stockObject['stock_unit'];
    elmStockPropPrevCloseValueTableColumn.attr('id', elmStockPropPrevCloseValueTableColumn_id);
    elmStockPropPrevCloseValueTableColumn.append(stockObject['stock_peratio_tte']);
    elmStockPropPrevCloseTableRow.append(elmStockPropPrevCloseValueTableColumn);
    elmStockParametersTable.append(elmStockPropPrevCloseTableRow)

    return elmStockParametersTable;
  }

});
