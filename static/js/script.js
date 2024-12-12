const editButtons = document.getElementsByClassName("btn-edit");
const suggestionText = document.getElementById("id_body");
const suggestionForm = document.getElementById("suggestionForm");
const submitButton = document.getElementById("submitButton");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated suggestions ID upon click.
* - Fetches the content of the corresponding suggestion.
* - Populates the `suggestionText` input/textarea with the suggestions content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_suggestion/{suggestionId}` endpoint.
*/

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let suggestionId = e.target.getAttribute("suggestion_id");
    let suggestionContent = document.getElementById(`suggestion${suggestionId}`).innerText;
    suggestionText.value = suggestionContent;
    submitButton.innerText = "Update";
    suggestionForm.setAttribute("action", `edit_suggestion/${suggestionId}`);
  });
}

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated suggestions ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific suggestion.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/

for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let suggestionId = e.target.getAttribute("suggestion_id");
    deleteConfirm.href = `delete_suggestion/${suggestionId}`;
    deleteModal.show();
  });
}
  