Feature:  Website layout test
		  As a user I want visual consistency on the http://www.asu.edu/ website


	Scenario:  Header layout
				Given I visit "http://www.asu.edu/"
				Then "header" should have "background-color" of "rgba(255,255,255,1)"

	Scenario:	Logo Offset
				Given I visit "http://www.asu.edu/"
				Then "asuLogo" should have offset "top" of "12"

	Scenario:	Logo Height
				Given I visit "http://www.asu.edu/"
				Then "asuLogo" should have "height" of "32px"

	Scenario:	Logo Width
				Given I visit "http://www.asu.edu/"
				Then "asuLogo" should have "width" of "203px"

	Scenario:   Department Name
				Given I visit "http://www.asu.edu/"
				Then "departmentName" should have "color" of "rgba(0,0,0,1)"

	Scenario:	Department Name Font Size
				Given I visit "http://www.asu.edu/"
				Then "departmentName" should have "font-size" of "24px"

	Scenario:   Universal Footer color
				Given I visit "http://www.asu.edu/"
				Then "footer" should have "background-color" of "rgb(229,229,229)"
