document.addEventListener('DOMContentLoaded', function() {
    const tabButtons = document.querySelectorAll('.tab-button');
    
    tabButtons.forEach(function(button) {
      button.addEventListener('click', function() {
        const targetId = button.getAttribute('data-target');
        const targetContent = document.getElementById(targetId);
        
        // Hide all content divs
        document.querySelectorAll('.content').forEach(function(content) {
          content.classList.add('hide');
        });
        
        // Show the content related to the clicked tab
        targetContent.classList.remove('hide');
      });
    });
  });

  $(document).ready(function() {
    // Extract event handlers into separate functions for reuse
    function starHoverEnter() {
      $(this).text(wjx_all).prevAll("li").text(wjx_all).end().nextAll("li").text(wjx_none);
    }

    function starHoverLeave() {
      $(".comment").children("li").text(wjx_none);
      $(".clicked").text(wjx_all).prevAll("li").text(wjx_all).end().nextAll("li").text(wjx_none);
    }

    function starClick() {
      $(this).addClass("clicked").siblings("li").removeClass("clicked");
    }

    var wjx_all = "★"; // Solid star
    var wjx_none = "☆"; // Empty star

    function toggleEditMode() {
      const commentSection = $(".comment");
      const editBtn = $("#editBtn");
      let enableEdit = true; // Set enableEdit to true initially

      if (editBtn.text() === "評價") {
        enableEdit = false; // Set enableEdit to false if the button text is "評價"
        editBtn.text("鎖定");

        // Add event listeners
        commentSection.on("mouseenter", "li", starHoverEnter);
        commentSection.on("mouseleave", starHoverLeave);
        commentSection.on("click", "li", starClick);
      } else {
        enableEdit = true; // Set enableEdit to true if the button text is not "評價"
        editBtn.text("評價");

        // Remove event listeners
        commentSection.off("mouseenter", "li", starHoverEnter);
        commentSection.off("mouseleave", starHoverLeave);
        commentSection.off("click", "li", starClick);
      }
    }

    // Call toggleEditMode() on page load to ensure initial state is non-edit mode
    toggleEditMode();

    // Call toggleEditMode() when the button is clicked to toggle the edit mode
    $("#editBtn").click(function() {
      toggleEditMode();
    });
  });