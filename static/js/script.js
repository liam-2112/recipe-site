document.addEventListener('DOMContentLoaded', function () {
 // Star rating functionality
     const starRating = document.querySelector('.star-rating');
     if (starRating){
     const stars = starRating.querySelectorAll('input[type="radio"]');
     
     stars.forEach(star => {
         star.addEventListener('change', function() {
             const checkedValue = this.value;
             stars.forEach(s => {
                 const label = s.nextElementSibling;
                 if (s.value <= checkedValue) {
                     label.style.color = '#ffdd00';
                 } else {
                     label.style.color = '#ddd';
                 }
             });
         });
     });
 
         // Hover effect
     const labels = starRating.querySelectorAll('label');
     labels.forEach(label => {
         label.addEventListener('mouseover', function() {
             const siblingInput = this.previousElementSibling;
             const hoverValue = siblingInput.value;
             labels.forEach(l => {
                 if (l.previousElementSibling.value <= hoverValue) {
                     l.style.color = '#ffdd00';
                 } else {
                     l.style.color = '#ddd';
                 }
             });
         });
 
         label.addEventListener('mouseout', function() {
             const checkedStar = starRating.querySelector('input:checked');
             if (checkedStar) {
                 const checkedValue = checkedStar.value;
                 labels.forEach(l => {
                     if (l.previousElementSibling.value <= checkedValue) {
                         l.style.color = '#ffdd00';
                     } else {
                         l.style.color = '#ddd';
                     }
                 });
             } else {
                 labels.forEach(l => l.style.color = '#ddd');
             }
         });
 });
 }

//  Delete review button
   
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let reviewId = e.target.getAttribute("review_id");
            deleteConfirm.href = `reviews/delete_review/${reviewId}`;
            deleteModal.show();
        });
    }
});
    