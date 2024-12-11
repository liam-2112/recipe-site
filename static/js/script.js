document.addEventListener('DOMContentLoaded', function() {

//  Delete suggestion button
 
  const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
  const deleteButtons = document.getElementsByClassName("btn-delete");
  const deleteConfirm = document.getElementById("deleteConfirm");

  for (let button of deleteButtons) {
      button.addEventListener("click", (e) => {
          let suggestionId = e.target.getAttribute("suggestion_id");
          deleteConfirm.href = `suggestions/delete_suggestion/${suggestionId}`;
          deleteModal.show();
      });
  }
});
  