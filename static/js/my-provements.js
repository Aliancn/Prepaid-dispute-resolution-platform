document.addEventListener('DOMContentLoaded', function() {
    var pageSize = 10;
    var currentPage = 1;
    var paginationElement = document.getElementById('pagination');
    var table = document.getElementById("provementTable");
    var tableRows = table.querySelectorAll('tbody tr');
    var pageCount = Math.ceil(tableRows.length / pageSize);
    var queryDate = "";
    var queryTitle = "";
    

    function showPage(page, tableRows) {
        var startIndex = (page - 1) * pageSize;
        var endIndex = startIndex + pageSize;
        
        tableRows.forEach(function(row, index) {
            console.log(row);
            if (index >= startIndex && index < endIndex) {
                row.style.display = 'table-row';
            } else {
                row.style.display = 'none';
            }
        });
    }

    function updatePagination(tableRows) {
        while (paginationElement.firstChild) {
            paginationElement.removeChild(paginationElement.firstChild);
        }
        
        var previousButton = createPaginationButton('Previous', '«', 'previous-page', currentPage === 1);
        paginationElement.appendChild(previousButton);

        for (var i = 1; i <= pageCount; i++) {
            var pageButton = createPaginationButton(i, i, 'page-' + i, i === currentPage);
            paginationElement.appendChild(pageButton);
        }

        var nextButton = createPaginationButton('Next', '»', 'next-page', currentPage === pageCount);
        paginationElement.appendChild(nextButton);

        addPaginationEventListeners(tableRows);
    }

    function createPaginationButton(ariaLabel, innerHTML, id, isDisabled) {
        var button = document.createElement('li');
        button.className = 'page-item';
        if (isDisabled) {
            button.classList.add('disabled');
        }
        var link = document.createElement('a');
        link.className = 'page-link';
        link.href = 'javascript:;';
        link.setAttribute('aria-label', ariaLabel);
        link.innerHTML = innerHTML;
        button.appendChild(link);
        button.id = id;
        return button;
    }

    function addPaginationEventListeners(tableRows) {
        var pageLinks = document.querySelectorAll('.pagination li.page-item:not(.disabled) a.page-link');
        pageLinks.forEach(function(link) {
            link.addEventListener('click', function() {
                var clickedPage = parseInt(this.innerHTML);
                if (!isNaN(clickedPage)) {
                    currentPage = clickedPage;
                    showPage(currentPage, tableRows);
                    updatePagination(tableRows);
                } else if (this.parentNode.id === 'previous-page') {
                    currentPage--;
                    showPage(currentPage, tableRows);
                    updatePagination(tableRows);
                } else if (this.parentNode.id === 'next-page') {
                    currentPage++;
                    showPage(currentPage, tableRows);
                    updatePagination(tableRows);
                }
            });
        });
    }

    // 初始化页面
    
    updatePagination(tableRows);
    showPage(currentPage, tableRows);

    document.getElementById("queryButton").addEventListener("click", function(event) {
        event.preventDefault();
        queryDate = document.getElementById("datePick").value;
        queryTitle = document.getElementById("titleInput").value;
    
        // 根据查询条件重新过滤表格行
        tableRows = table.querySelectorAll('tbody tr');
        tableRows.forEach(function(row) {
            var provmentDate = row.querySelector('td:nth-child(3)').innerHTML;
            var provmentTitle = row.querySelector('td:nth-child(1)').innerHTML;
            if (
                (queryDate === "" || provmentDate === queryDate) &&
                (queryTitle === "" || provmentTitle === queryTitle)
            ) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
        var newtableRows = table.querySelectorAll('tbody tr:not([style="display: none;"])');
        // 重新计算总页数和当前页面，并更新分页器
        pageCount = Math.ceil(newtableRows.length / pageSize);
        currentPage = 1; // 查询后回到第一页
        
        showPage(currentPage, newtableRows);
        updatePagination(newtableRows);
        
    });
});

if (document.querySelector(".datepicker")) {
    flatpickr(".datepicker", {});
}
