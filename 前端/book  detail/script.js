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
  