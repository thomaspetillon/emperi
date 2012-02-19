// UDMv4.52 //
///////////////////////////////////////////////////////////////////
var um={'menuClasses':[],'itemClasses':[],'menuCode':[]};
///////////////////////////////////////////////////////////////////
//                                                               //
//  ULTIMATE DROP DOWN MENU Version 4.52 by Brothercake          //
//  http://www.udm4.com/                                         //
//                                                               //
//  This script may not be used or distributed without license   //
//                                                               //
///////////////////////////////////////////////////////////////////




///////////////////////////////////////////////////////////////////
// CORE CONFIGURATION                                            //
///////////////////////////////////////////////////////////////////


//path to images folder
um.baseSRC = "udm-resources/";


//initialization trigger element ["id"];
um.trigger = "";


//navbar orientation
um.orientation = [
	"horizontal",	// alignment ["vertical"|"horizontal"|"popup"|"expanding"]
	"left",		// h align ["left"|"right"]
	"top",		// v align ["top"|"bottom"]
	"relative",	// positioning ["relative"|"absolute"|"fixed"|"allfixed"]
	"0px",	// x position ["em"|"ex"|"px"|"0"]
	"0px",	// y position ["em"|"ex"|"px"|"0"]
	"1000",		// z order ["0" to "10000"] (menu takes 20000 headroom)
	];


//navbar list output
um.list = [
	"flexible",	// horizontal overflow ["rigid"|"flexible"]
	"yes",		// -SPARE-
	"no", 		// -SPARE-
	];


//menu behaviors
um.behaviors = [
	"20",		// open timer ["milliseconds"|"0"]
	"500",		// close timer ["milliseconds"|"never"|"0"]
	"yes",		// reposition menus to stay inside the viewport ["yes"|"no"]
	"default",	// manage windowed controls for win/ie ["default","hide","iframe","none"]
	];


//reset behaviors
um.reset = [
	"yes",		// reset from document mouse click ["yes"|"no"]
	"yes",		// reset from window resize ["yes"|"no"]
	"yes",		// reset from text resize ["yes"|"no"]
	"no",		// reset after following link ["yes"|"no"]
	];


//horizontal continuation strip
um.hstrip = [
	"none",		// background ["color"|"#hex"|"rgb()"|"image.gif"|"none"]
	"yes",		// copy navbar item margin-right to margin-bottom ["yes"|"no"]
	];




///////////////////////////////////////////////////////////////////
// MODULE SETTINGS                                               //
///////////////////////////////////////////////////////////////////


//keyboard navigation [comment out or remove if not using]
um.keys = [
	"38",		// up ["n"] ("38" = up arrow key)
	"39",		// right ["n"] ("39" = right arrow key)
	"40",		// down ["n"] ("40" = down arrow key)
	"37",		// left ["n"] ("37" = left arrow key)
	"123",		// hotkey ["n"] ("38" = F12]
	"none",		// hotkey modifier ["none"|"shiftKey"|"ctrlKey"|"altKey"|"metaKey"]
	"27",		// escape ["n"|"none"] ("27" = escape key)
	"document.getElementsByTagName('a')[0]", // exit focus ["js-expression"]
	];




///////////////////////////////////////////////////////////////////
// NAVBAR DEFAULT STYLES                                         //
///////////////////////////////////////////////////////////////////


//styles which apply to the navbar
um.navbar = [
	"0",		// nav -> menu x-offset (+-)["n" pixels]
	"0",		// nav -> menu y-offset (+-)["n" pixels]
	"7.5em",	// width ["em"|"ex"|"px"] (vertical navbar only - horizontal navbar items have "auto" width) ("%" doesn't work right)
	];


//styles which apply to each navbar item
um.items = [
	"0",		// margin between items ["n" pixels]
	"0",		// border size ["n" pixels] (single value only)
	"collapse",	// border collapse ["collapse"|"separate"] (only applies when margin = "0")
	"transparent transparent transparent transparent",// border colors ["color"|"#hex"|"rgb()"] (single, double or four values)
	"none",	// border styles ["solid"|"double"|"dotted"|"dashed"|"groove"|"ridge"|"inset"|"outset"] (single, double or four values; be careful with using "none")
	"transparent transparent transparent transparent",// hover/focus border colors ["color"|"#hex"|"rgb()"] (single, double or four values)
	"none",	// hover/focus border styles ["solid"|"double"|"dotted"|"dashed"|"groove"|"ridge"|"inset"|"outset"] (single, double or four values; be careful with using "none")
	"transparent transparent transparent transparent",// visited border colors ["color"|"#hex"|"rgb()"] (single, double or four values)
	"none none none",// visited border styles ["solid"|"double"|"dotted"|"dashed"|"groove"|"ridge"|"inset"|"outset"] (single, double or four values; be careful with using "none")
	"0",		// left/right padding ["n" pixels] (single value only)
	"2",		// top/bottom padding ["n" pixels] (single value only)
	"transparent",		// background ["color"|"#hex"|"rgb()"|"image.gif"]
	"transparent",		// hover/focus background ["color"|"#hex"|"rgb()"|"image.gif"]
	"transparent",		// visited background ["color"|"#hex"|"rgb()"|"image.gif"]
	"90%",		// font size ["em"|"ex"|"%"|"px"|"pt"|"absolute-size"|"relative-size"]
	"'LinuxLibertineORegular', serif",// font family ["font1,font2,font3"] (always end with a generic family name)
	"bold",		// font weight ["normal"|"bold"|"bolder"|"lighter|"100" to "900"]
	"none",		// text decoration ["none"|"underline"|"overline"|"line-through"]
	"center",		// text-align ["left"|"right"|"center"]
	"#000",	// color ["color"|"#hex"|"rgb()"]
	"#FFFFFF",	// hover/focus color ["color"|"#hex"|"rgb()"]
	"#transparent",	// visited color ["color"|"#hex"|"rgb()"]
	"normal",	// font-style ["normal"|"italic"|"oblique"]
	"normal",	// hover/focus font-style ["normal"|"italic"|"oblique"]
	"normal",	// visited font-style ["normal"|"italic"|"oblique"]
	"letter-spacing:0px !important;",// additional link CSS (careful!)
	"",		// additional hover/focus CSS (careful!)
	"",		// additional visited CSS (careful!)
	"none",// menu indicator character/image ["text"|"image.gif"|"none"]
	"none",// menu indicator rollover character/image ["text"|"image.gif"|"none"] (must be same type)
	"7",		// clipping width of indicator image ["n" pixels] (only when using image arrows)
	"..",		// alt text of indicator image ["text"] (only when using image arrows)
	];




///////////////////////////////////////////////////////////////////
// MENU DEFAULT STYLES                                           //
///////////////////////////////////////////////////////////////////


//styles which apply to each menu
um.menus = [
	"-7",		// menu -> menu x-offset (+-)["n" pixels]
	"-12",		// menu -> menu y-offset (+-)["n" pixels]
	"0",		// border size ["n" pixels] (single value only)
	"#000000 #000000 #000000 #000000",// border colors ["color"|"#hex"|"rgb()"] (single, double or four values)
	"none",	// border styles ["solid"|"double"|"dotted"|"dashed"|"groove"|"ridge"|"inset"|"outset"] (single, double or four values; be careful with using "none")
	"106px",	// width ["em"|"ex"|"px"]
	"0",		// padding ["n" pixels] (single value only)
	"#BDD600",	// background ["color"|"#hex"|"rgb()"|"image.gif"]
	"",		// additional menu CSS (careful!) (you can use a transition here but *not* a static filter)
	"none",// shadow background ["color"|"#hex"|"rgb()"|"image.gif"|"none"]
	"2px",		// shadow offset (+-) ["em"|"px"|"pt"|"%"|"0"]
	"filter:alpha(opacity=50);",// additional shadow layer CSS (if you use a Microsoft.Shadow filter here then Win/IE5.5+ will do that *instead* of default shadow)
	];


//styles which apply to each menu item
um.menuItems = [
	"0",		// margin around items ["n" pixels] (single value only; margins are like table cellspacing)
	"0",		// border size ["n" pixels] (single value only)
	"separate",	// border collapse ["collapse"|"separate"] (only applies when margin = "0")
	"#ffffff",	// border colors ["color"|"#hex"|"rgb()"] (single, double or four values)
	"solid",	// border styles ["solid"|"double"|"dotted"|"dashed"|"groove"|"ridge"|"inset"|"outset"] (single, double or four values; be careful with using "none")
	"#000000",		// hover/focus border colors ["color"|"#hex"|"rgb()"] (single, double or four values)
	"solid",	// hover/focus border styles ["solid"|"double"|"dotted"|"dashed"|"groove"|"ridge"|"inset"|"outset"] (single, double or four values; be careful with using "none")
	"#ffffff",	// visited border colors ["color"|"#hex"|"rgb()"] (single, double or four values)
	"solid",	// visited border styles ["solid"|"double"|"dotted"|"dashed"|"groove"|"ridge"|"inset"|"outset"] (single, double or four values; be careful with using "none")
	"5",		// left/right padding ["n" pixels] (single value only)
	"5",		// top/bottom padding ["n" pixels] (single value only)
	"transparent",	// background ["color"|"#hex"|"rgb()"|"image.gif"]
	"white",	// hover/focus background ["color"|"#hex"|"rgb()"|"image.gif"]
	"transparent",	// visited background ["color"|"#hex"|"rgb()"|"image.gif"]
	"75%",		// font size ["em"|"ex"|"%"|"px"|"pt"|"absolute-size"|"relative-size"]
	"Verdana,sans-serif",// font family ["font1,font2,font3"] (always end with a generic family name)
	"normal",	// font weight ["normal"|"bold"|"bolder"|"lighter|"100" to "900"]
	"none",		// text decoration ["none"|"underline"|"overline"|"line-through"]
	"center",		// text-align ["left"|"right"|"center"]
	"#000000",		// color ["color"|"#hex"|"rgb()"]
	"#000",		// hover/focus color ["color"|"#hex"|"rgb()"]
	"#000000",		// visited color ["color"|"#hex"|"rgb()"]
	"normal",	// font-style ["normal"|"italic"|"oblique"]
	"normal",	// hover/focus font-style ["normal"|"italic"|"oblique"]
	"normal",	// visited font-style ["normal"|"italic"|"oblique"]
	"",		// additional link CSS (careful!)
	"",		// additional hover/focus CSS (careful!)
	"",		// additional visited CSS (careful!)
	"none",// submenu indicator character/image ["text"|"image.gif"|"none"]
	"none",// submenu indicator rollover character/image ["text"|"image.gif"|"none"] (must be the same type)
	"3",		// clipping width of indicator image ["n" pixels] (only when using image arrows)
	"..",		// alt text of indicator image ["text"] (only when using image arrows)
	];




///////////////////////////////////////////////////////////////////
// MENU CLASSES [comment out or remove if not using]             //
///////////////////////////////////////////////////////////////////


//classes which apply to menus [optional]
um.menuClasses["orangeMenu"] = [
	"#ffffff #ffffff #ffffff #fffff",// border colors ["color"|"#hex"|"rgb()"]
	"solid",	// border styles ["solid"|"double"|"dotted"|"dashed"|"groove"|"ridge"|"inset"|"outset"] (single, double or four values; be careful with using "none")
	"8em",		// width ["em"|"ex"|"px"]
	"#fec",		// background ["color"|"#hex"|"rgb()"|"image.gif"]
	"",		// additional menu CSS (careful!) (you can use a transition here but *not* a static filter)
	"none",// shadow background ["color"|"#hex"|"rgb()"|"image.gif"|"none"]
	"2px",		// shadow offset (+-) ["em"|"px"|"pt"|"%"|"0"]
	"filter:alpha(opacity=50);", // additional shadow layer CSS (if you use a Microsoft.Shadow filter here then Win/IE5.5+ will do that *instead* of default shadow)
	];


//classes which apply to menu items [optional]
um.itemClasses["orangeMenuItem"] = [
	"#fff",		// border colors ["color"|"#hex"|"rgb()"] (single, double or four values)
	"solid",	// border styles ["solid"|"double"|"dotted"|"dashed"|"groove"|"ridge"|"inset"|"outset"] (single, double or four values; be careful with using "none")
	"#ffffff",	// hover/focus border colors ["color"|"#hex"|"rgb()"] (single, double or four values)
	"solid",	// hover/focus border styles ["solid"|"double"|"dotted"|"dashed"|"groove"|"ridge"|"inset"|"outset"] (single, double or four values; be careful with using "none")
	"#fff",		// visited border colors ["color"|"#hex"|"rgb()"] (single, double or four values)
	"solid",	// visited border styles ["solid"|"double"|"dotted"|"dashed"|"groove"|"ridge"|"inset"|"outset"] (single, double or four values; be careful with using "none")
	"#fff",		// background ["color"|"#hex"|"rgb()"|"image.gif"]
	"#fffff",	// hover/focus background ["color"|"#hex"|"rgb()"|"image.gif"]
	"#fff",		// visited background ["color"|"#hex"|"rgb()"|"image.gif"]
	"70%",		// font size ["em"|"ex"|"%"|"px"|"pt"|"absolute-size"|"relative-size"]
	"tahoma,sans-serif",// font family ["font1,font2,font3"] (always end with a generic family name)
	"normal",	// font weight ["normal"|"bold"|"bolder"|"lighter|"100" to "900"]
	"none",		// text decoration ["none"|"underline"|"overline"|"line-through"]
	"center",		// text-align ["left"|"right"|"center"]
	"#BDD600",	// color ["color"|"#hex"|"rgb()"]
	"#BDD600",	// hover/focus color ["color"|"#hex"|"rgb()"]
	"#BDD600",	// visited color ["color"|"#hex"|"rgb()"]
	"normal",	// font-style ["normal"|"italic"|"oblique"]
	"normal",	// hover/focus font-style ["normal"|"italic"|"oblique"]
	"normal",	// visited font-style ["normal"|"italic"|"oblique"]
	"",		// additional link CSS (careful!)
	"",		// additional hover/focus CSS (careful!)
	"",		// additional visited CSS (careful!)
	"none",// submenu indicator character/image ["text"|"image.gif"|"none"] (must be the same type as default submenu indicator)
	"none",// submenu indicator rollover character/image ["text"|"image.gif"|"none"] (must be the same type)
	"..",		// alt text of indicator image  ["text"] (only when using image arrow)
	];




///////////////////////////////////////////////////////////////////
// DYNAMIC MENUS                                                 //
///////////////////////////////////////////////////////////////////




