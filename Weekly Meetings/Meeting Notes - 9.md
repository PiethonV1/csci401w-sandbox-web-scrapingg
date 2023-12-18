-------------------------------------
Class Notes - Workshop

Finish Foundation
Feature Focus
Presentations

Challenges -
	Breaking up work
	Studio > Github
	(Us) Tech stack getting started
		Sharing code
	Node.js Database
	(Also Us) Pulling Data from API (Facebook / Yahoo Finance)

-------------------------------------

Assignment 4 - 
	Backlog in Trello with Acceptance Criteria
	5 - 10 Min Video	
		Upload to Teams Channel
		Tag Prof for Grading
	Talk about Challenges with Project

-------------------------------------

Workshop - Bringing everything together
	Learn by example
	Used MySQL/SQLite

	What:

	Main:
		Primitive code
		Branch: More Functionality
	Using jQuery
	Express.js
	SQLite

	Src:
		Folders seperated by what part it is.
		API, Data, Docs, Scripts, UI

	How:

	Diagram:			Node JS(Express JS)

		|File system|		|Server|			|File System|
		|Browser    |	--->	|API   |     -------------->	|DB	    |
		|UI	    |		
					   |
					   V

				      |USDA Foods|

	Main:
		Pull down and try to follow - Update for issues
			
	Troubleshooting:
		Developer tools:
			Click on source of error to be brought to error location.
			Failed fetch - Connectivity issue
			Breakpoint - Allows Inspection.

	API: See Textbook for Indepth 	
		Share/Expose Functionality to let Vendor access Data
		Website without UI (Typically)
		Tens to Hundreds of different API

Organization is key

		Node JS(Express JS)
		server.js starts program
		Check for package instead of drivers - etc
			Check for shared code.
		Package.json - What version of each package is brought in.
				Manages dependancies.
		Swagger - Documents Endpoints for UI-less API
			Where source code is. Mini-Documentation
			node server.js	(Allows for testing)
			Without, you'll need to know where endpoints are, and put them into the browser.
		Dont want full connection
		Can't connect Browser to DB Directly
			Java app is exception, unless other people want access.		
		listen -> import and direct to index (Router-like)		
		Run in debug mode
			Stepthrough - is useful for wrong spelling, etc.

Programmer Pet Peeve - No Due Diligence on Problem.

		Include packages/drivers/etc from Node
		Index:
			Res.json - return data into function in website
			fetch
			then
Track which foods:
	Branch: Fav Foods.
		More endpoints.
		Get a Specific User by User ID
			Bogus ID gets error (Defensive Coding/Coding for errors)
		Param into actual request
		res.status(404).json for invaild ID (Doesn't exist)
			Code should be static, one of the standard HTTP Protocol ones.

	DB:
		ChatGPT for Dummy Data
		Library
		JavaScript Framework
			JQEasyUI - great for Database (jeasyui.com)
				offers HTML - etc
				Not perfectly.
				Mock Data 		
		URL > API
		Column name matchs up with call.
		React on click (onclickrow (index row))
				Call API, Return Data
		datagrid
			JQEasyUI kit
		Create DB > API > Dummy Data > Swagger
		UI Problems IN UI Problems

Test Driven Development
	Run test after a/a few change(s).

Merge Branch

-------------------------------------

Other - 
	Demo took 6-8 hours - Thanks to ChatGPT
		2 hours a day

	Introducing server / setup
		Might take mulitple hours
		plus documentation
		With Firebase not so much

		USDA foods API food data central
			If you can eat it - it's here
			Calories
			API Key:
				DEMO_API
		Example call
		HTTP Request
		save as json
		Store data in Config(?)

		
		
-------------------------------------

Meeting Notes -

DB: SQLite

Problem: Streamlit supposed to be on it's own - not on top of Django
	Alts for Streamlit?
		New version: Run on own machine, Output on UI. 
		Make sure your plugged in. Uses Computers Specs.

Pull tables > DB > Visual > Django > Another Window

Next Step: Get Database running.

Database larger than thought.

Look at other predection models / Docker?

Difficulty on running project:
	Goal: Run on any computer. Progess made.
	
	Clear Cache? (ChatGPT?) (pip cmd?)

	Have to put in manually

Seperate class

Learning curve: Make work with "alien" software.

Only Pulls - Graphs


