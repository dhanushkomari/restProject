/*
			KEY COMPONENTS:
			"activeItem" = null until an edit button is clicked. Will contain object of item we are editing
			"list_snapshot" = Will contain previous state of list. Used for removing extra rows on list update

			PROCESS:
			1 - Fetch Data and build rows "buildList()"
			2 - Create Item on form submit
			3 - Edit Item click - Prefill form and change submit URL
			4 - Delete Item - Send item id to delete URL
			5 - Cross out completed task - Event handle updated item
			NOTES:
			-- Add event handlers to "edit", "delete", "title"
			-- Render with strike through items completed
			-- Remove extra data on re-render
			-- CSRF Token
*/
buildList()

function buildList(){
  var wrapper = getElementById("list-wrapper")

	var url = "http://127.0.0.1:8000/api/task-list"

	fetch(url)
	.then((resp) => resp.json())
	.then(function(){
		console.log('Data:', data);
	})
}
