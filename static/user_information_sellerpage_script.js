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

    // Check URL parameters and switch content accordingly
    // 網址是/...?tab=finished時預設導到'finished'分頁
    const urlParams = new URLSearchParams(window.location.search);
    const tabParam = urlParams.get('tab');
    if (tabParam === 'finished') {
      document.getElementById('processing').classList.add('hide');
      document.getElementById('finished').classList.remove('hide');
    }

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

      // 將星星依SQL中O_SalerRating值填滿對應個數
      const ratingValue = parseInt($("#ratingValueInput").val()); // 取得O_SalerRating的值
      $(".comment").children("li").each(function(index) { // 找到對應的<li>元素，將索引小於等於ratingValue的<li>元素設定為填滿的星星
        if (index < ratingValue) {
          $(this).text(wjx_all).addClass("clicked");
        }
      });

    } else {
      enableEdit = true; // Set enableEdit to true if the button text is not "評價"
      editBtn.text("評價");

      // Remove event listeners
      commentSection.off("mouseenter", "li", starHoverEnter);
      commentSection.off("mouseleave", starHoverLeave);
      commentSection.off("click", "li", starClick);

      // (鎖定狀態下)將星星依SQL中O_SalerRating值填滿對應個數
      $(".comment").children("li").each(function(index) {
        if (index < ratingValue) {
          $(this).text(wjx_all);
        } else {
          $(this).text(wjx_none);
        }
      });

    }
  }

  // Call toggleEditMode() on page load to ensure initial state is non-edit mode
  toggleEditMode();

  // Call toggleEditMode() when the button is clicked to toggle the edit mode
  $("#editBtn").click(function() {
    toggleEditMode();
  });
});