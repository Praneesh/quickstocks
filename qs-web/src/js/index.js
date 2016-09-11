$(document).ready(function(){

  initialize();

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

    // Step 5.1
    createUserPicks("HONEYWELL");

    // Step 5.3
    //createTopPicksForUser("HONEYWELL");
  }

  function createUserPicks(stockElement){
    var elmUserPicksRow = $("#widget-rows-userpicks");
    if(elmUserPicksRow == null){
      console.log("Could not get the User Pick row !");
      return;
    }
    /*
      THIS IS GOING TO BE A LONG LONG LONG FUNCTION.... BREAK IT !!!
    */

    // Step 1: Create a Widget elements
    elmStockWidget = $(document.createElement('div'));
    elmStockWidget.addClass("widget");

    // Step 1.1 : Widget Header
    elmStockWidgetHeader = $(document.createElement('div'));
    elmStockWidgetHeader.addClass('widget-header');
    elmStockWidgetHeader.attr('id','widget-header-PRAN');
    elmStockWidgetHeader.append("<i class='icon-bookmark'></i>");
    elmStockWidgetHeader.append("<h3>Honeywell International Inc. (HON)</h3>");

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

    // Sub Notes 1 - Equity
    elmStockWidgetSubNote_1 = $(document.createElement('div'));
    elmStockWidgetSubNote_1.addClass('widget-stock-price-subnote');
    elmStockWidgetSubNote_1.attr('id','widget-stock-price-sn-equity-PRAN');
    elmStockWidgetSubNote_1.append('NYSE - NYSE Real Time Price.');
    elmStockWidgetPriceColumn.append(elmStockWidgetSubNote_1);

    // Sub Notes 2 - Date Time
    elmStockWidgetSubNote_2 = $(document.createElement('div'));
    elmStockWidgetSubNote_2.addClass('widget-stock-price-subnote');
    elmStockWidgetSubNote_2.attr('id','widget-stock-price-sn-time-PRAN');
    elmStockWidgetSubNote_2.append('At close: 4:01 PM EDT');
    elmStockWidgetPriceColumn.append(elmStockWidgetSubNote_2);

    elmStockWidgetContentRow.append(elmStockWidgetPriceColumn);

    //Step 1.3.2 : Create Stock Logo
    elmStockWidgetLogoColumn = $(document.createElement('div'));
    elmStockWidgetLogoColumn.addClass('col-md-2');
    elmStockWidgetLogoColumn.append(getStockValueLogo());
    elmStockWidgetContentRow.append(elmStockWidgetLogoColumn);
    elmStockWidgetContent.append(elmStockWidgetContentRow);

    // ROW 2 for more Stock Week Range !!
    elmStockRangeRow = $(document.createElement('div'));
    elmStockRangeRow.addClass('row');
    elmStockRangeRowColumn = $(document.createElement('div'));
    elmStockRangeRowColumn.addClass('col-md-12');
    elmStockRangeRowColumn.append(getStockRangeTable());
    elmStockRangeRow.append(elmStockRangeRowColumn);
    elmStockWidgetContent.append(elmStockRangeRow);

    // Row 3 for Stock Properties...!
    // ROW 3 Colum 1 for more Stock Properties !!
    elmStockPropRow = $(document.createElement('div'));
    elmStockPropRow.addClass('row');
    elmStockPropRowColumn = $(document.createElement('div'));
    elmStockPropRowColumn.addClass('col-md-6');
    elmStockPropRowColumn.append(getStockParametersTableColumn_One());
    elmStockPropRow.append(elmStockPropRowColumn);

    // ROW 3 Colum 2 for more Stock Properties !!
    elmStockPropRowColumnTwo = $(document.createElement('div'));
    elmStockPropRowColumnTwo.addClass('col-md-6');
    elmStockPropRowColumnTwo.append(getStockParametersTableColumn_Two());
    elmStockPropRow.append(elmStockPropRowColumnTwo);

    elmStockWidgetContent.append(elmStockPropRow);


    // Updating the Widget Content
    elmStockWidget.append(elmStockWidgetHeader);
    elmStockWidget.append(elmStockWidgetContent);

    // Create the Column Element
    elmStockWidgetColumn = $(document.createElement('div'));
    elmStockWidgetColumn.addClass("col-md-6");  //Bootstrap Class - Explore better ways of doing this
    elmStockWidgetColumn.append(elmStockWidget);

    // Add the above column to the UserPicks row
    elmUserPicksRow.append(elmStockWidgetColumn);
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

  function getStockWidgetPrice(){
    elmStockWidgetPrice = $(document.createElement('div'));
    elmStockWidgetPrice.addClass('widget-stock-price');
    elmStockWidgetPrice.attr('id','widget-stock-price-PRAN');
    elmStockWidgetPrice.append("<span>112.0 USD </span>");

    elmStockWidgetStats = $(document.createElement('span'));
    elmStockWidgetStats.addClass('widget-stock-deviation-decline');
    elmStockWidgetStats.attr('id','widget-stock-status-PRAN');
    elmStockWidgetStats.append('-1.83 (-1.59%)');
    elmStockWidgetPrice.append(elmStockWidgetStats);

    return elmStockWidgetPrice;
  }

  function getStockValueLogo(){
    elmStockWidgetLogo = $(document.createElement('div'));
    elmStockWidgetLogo.addClass('widget-stock-price-logo');
    elmStockWidgetLogo.attr('id','widget-stock-price-logo-PRAN');
    elmStockWidgetLogo.append('P');
    return elmStockWidgetLogo;
  }

  function getStockRangeTable(){
    // 52 Wk Row Table
    elmStockRangeTable = $(document.createElement('table'));
    elmStockRangeTable.addClass('table table-condensed');

    elmStockRangeTableRow = $(document.createElement('tr'));
    elmStockRangeTitleTableColumn = $(document.createElement('td'));
    elmStockRangeTitleTableColumn.append('52wk Range');

    elmStockRangeValueTableColumn = $(document.createElement('td'));
    elmStockRangeValueTableColumn.attr('width','35%');
    elmStockRangeValueTableColumn.attr('id','widget-tbl-52wk-PRAN')
    elmStockRangeValueTableColumn.append('55.01 - 78.86 USD');

    elmStockRangeTableRow.append(elmStockRangeTitleTableColumn);
    elmStockRangeTableRow.append(elmStockRangeValueTableColumn);
    elmStockRangeTable.append(elmStockRangeTableRow)

    return elmStockRangeTable;
  }

  function getStockParametersTableColumn_One(){
    // Rest of the parameters
    elmStockParametersTable = $(document.createElement('table'));
    elmStockParametersTable.addClass('table table-condensed');

    // Col 1 Row 1
    elmStockPropOpenTableRow = $(document.createElement('tr'));
    elmStockPropOpenTitleTableColumn = $(document.createElement('td'));
    elmStockPropOpenTitleTableColumn.append('Open');
    elmStockPropOpenTableRow.append(elmStockPropOpenTitleTableColumn);

    elmStockPropOpenValueTableColumn = $(document.createElement('td'));
    elmStockPropOpenValueTableColumn.attr('width','25%');
    elmStockPropOpenValueTableColumn.attr('id','widget-tbl-open-PRAN');
    elmStockPropOpenValueTableColumn.append('112.86');
    elmStockPropOpenTableRow.append(elmStockPropOpenValueTableColumn);
    elmStockParametersTable.append(elmStockPropOpenTableRow)

    // Col 1 Row 2
    elmStockPropPrevCloseTableRow = $(document.createElement('tr'));
    elmStockPropPrevCloseTitleTableColumn = $(document.createElement('td'));
    elmStockPropPrevCloseTitleTableColumn.append('Prev Close');
    elmStockPropPrevCloseTableRow.append(elmStockPropPrevCloseTitleTableColumn);

    elmStockPropPrevCloseValueTableColumn = $(document.createElement('td'));
    elmStockPropPrevCloseValueTableColumn.attr('width','25%');
    elmStockPropPrevCloseValueTableColumn.attr('id','widget-tbl-prevclose-PRAN');
    elmStockPropPrevCloseValueTableColumn.append('113.82');
    elmStockPropPrevCloseTableRow.append(elmStockPropPrevCloseValueTableColumn);
    elmStockParametersTable.append(elmStockPropPrevCloseTableRow)
    elmStockPropRowColumn.append(elmStockParametersTable);

    return elmStockParametersTable;
  }

  function getStockParametersTableColumn_Two(){

    // Rest of the parameters
    elmStockParametersTable = $(document.createElement('table'));
    elmStockParametersTable.addClass('table table-condensed');

    // Col 1 Row 1
    elmStockPropOpenTableRow = $(document.createElement('tr'));
    elmStockPropOpenTitleTableColumn = $(document.createElement('td'));
    elmStockPropOpenTitleTableColumn.append('Market Cap');
    elmStockPropOpenTableRow.append(elmStockPropOpenTitleTableColumn);

    elmStockPropOpenValueTableColumn = $(document.createElement('td'));
    elmStockPropOpenValueTableColumn.attr('width','25%');
    elmStockPropOpenValueTableColumn.attr('id','widget-tbl-mcap-PRAN');
    elmStockPropOpenValueTableColumn.append('112.86');
    elmStockPropOpenTableRow.append(elmStockPropOpenValueTableColumn);
    elmStockParametersTable.append(elmStockPropOpenTableRow)

    // Col 1 Row 2
    elmStockPropPrevCloseTableRow = $(document.createElement('tr'));
    elmStockPropPrevCloseTitleTableColumn = $(document.createElement('td'));
    elmStockPropPrevCloseTitleTableColumn.append('P/E Ratio (ttm)');
    elmStockPropPrevCloseTableRow.append(elmStockPropPrevCloseTitleTableColumn);

    elmStockPropPrevCloseValueTableColumn = $(document.createElement('td'));
    elmStockPropPrevCloseValueTableColumn.attr('width','25%');
    elmStockPropPrevCloseValueTableColumn.attr('id','widget-tbl-ttm-PRAN');
    elmStockPropPrevCloseValueTableColumn.append('23.17');
    elmStockPropPrevCloseTableRow.append(elmStockPropPrevCloseValueTableColumn);
    elmStockParametersTable.append(elmStockPropPrevCloseTableRow)

    return elmStockParametersTable;
  }
});
