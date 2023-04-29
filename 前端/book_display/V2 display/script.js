$(document).ready(function () {
    // 配置
    var itemsPerPage = 16;
    var currentPage = 1;
    var totalPages = 1;
    var data = generateData(50); // 修改這個數字以更改測試數據的數量

    // 生成測試數據
    function generateData(numItems) {
        var items = [];
        for (var i = 0; i < numItems; i++) {
            items.push({
                url: "https://www.example.com",
                imgSrc:
                    "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/072/34/0010723443.jpg&v=5791f5bck&w=280&h=280",
                title: "商業管理",
                price: "500 NT$",
            });
        }
        return items;
    }

    // 更新分頁信息
    function updatePagination() {
        totalPages = Math.ceil(data.length / itemsPerPage);
        $("#previousPage").prop("disabled", currentPage === 1);
        $("#nextPage").prop("disabled", currentPage === totalPages);
        $("#lastPage").prop("disabled", currentPage === totalPages);
        $("#currentPage").text(currentPage + " / " + totalPages);
    }

    // 渲染表格項目
    function renderGridItems() {
        $(".grid-container").empty();
        var startIndex = (currentPage - 1) * itemsPerPage;
        var endIndex = Math.min(startIndex + itemsPerPage, data.length);
        for (var i = startIndex; i < endIndex; i++) {
            var item = data[i];
            var gridItem = $("<div>")
                .addClass("grid-item")
                .data("url", item.url)
                .on("click", function () {
                    window.location.href = $(this).data("url");
                });

            var imageContainer = $("<div>")
                .addClass("image-container")
                .appendTo(gridItem);
            $("<img>").attr("src", item.imgSrc).appendTo(imageContainer);

            var textContainer = $("<div>").addClass("text-container").appendTo(gridItem);
            $("<p>").text(item.title).appendTo(textContainer);
            $("<p>").text(item.price).appendTo(textContainer);

            $(".grid-container").append(gridItem);
        }
    }

    // 上一頁按鈕事件
    $("#previousPage").on("click", function () {
        currentPage--;
        renderGridItems();
        updatePagination();
    });

    // 下一頁按鈕事件
    $("#nextPage").on("click", function () {
        currentPage++;
        renderGridItems();
        updatePagination();
    });

    // 尾頁按鈕事件
    $("#lastPage").on("click", function () {
        currentPage = totalPages;
        renderGridItems();
        updatePagination();
    });

    // 初始化渲染
    renderGridItems();
    updatePagination();
});
