window.onload = function() {
  var submitBtn = document.getElementById('submitBtn');
  var replyToId = null;

  submitBtn.addEventListener('click', function() {
    submitText();
  });

  function submitText() {
    var textArea = document.getElementById('textArea');
    var text = textArea.value.trim();

    if (text !== '') {
      var num = document.getElementsByClassName('border').length;
      var borderId = 'border-' + num;

      var border = document.createElement('div');
      border.classList.add('border');
      border.id = borderId;

      var left = document.createElement('div');
      left.classList.add('left');
      border.appendChild(left);

      var leftBorder = document.createElement('div');
      leftBorder.classList.add('left-border');
      left.appendChild(leftBorder);

      var leftContent = document.createElement('div');
      leftContent.classList.add('left-content');
      leftBorder.appendChild(leftContent);

      var image = document.createElement('img');
      image.setAttribute('src', 'your-image-url.jpg');
      image.setAttribute('id', 'image');
      leftContent.appendChild(image);

      var textElement = document.createElement('p');
      textElement.textContent = text;
      leftContent.appendChild(textElement);

      var right = document.createElement('div');
      right.classList.add('right');
      border.appendChild(right);

      var rightText = document.createElement('p');
      rightText.textContent = text;
      right.appendChild(rightText);

      var replyBtn = document.createElement('button');
      replyBtn.textContent = '回覆';
      replyBtn.classList.add('reply-btn');
      right.appendChild(replyBtn);

      var numElement = document.createElement('span');
      numElement.textContent = '#' + num;
      numElement.classList.add('num');
      right.appendChild(numElement);

      var replySeparator = document.createElement('hr');
      replySeparator.classList.add('reply-separator');
      right.appendChild(replySeparator);

      replyBtn.addEventListener('click', function() {
        var originalText = this.parentNode.parentNode.querySelector('.left-content p').textContent;
        textArea.value = '回覆 ' + originalText + ': ';
        textArea.focus();
        window.location.href = '#textArea';

        replyToId = borderId;
      });

      var textContainer = document.getElementById('textContainer');
      textContainer.appendChild(border);

      if (replyToId && text.startsWith('回覆')) {
        var findOriginalBtn = document.createElement('button');
        findOriginalBtn.textContent = '找原文';
        findOriginalBtn.classList.add('find-original-btn');
        findOriginalBtn.addEventListener('click', function() {
          window.location.href = '#' + replyToId;
        });
        right.appendChild(findOriginalBtn);
      }

      textArea.value = '';
    }
  }
};
