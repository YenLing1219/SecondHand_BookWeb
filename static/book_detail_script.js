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
  async function purchaseBook(book_id, buyer_id) {
    const response = await fetch(`/purchaseBook/${book_id}/${buyer_id}`);
    const result = await response.text();
  
    if (result === 'Emails sent successfully!') {
      alert('郵件已成功發送！');
    } else {
      alert('郵件發送失敗，請稍後重試。');
    }
  }
  