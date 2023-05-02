function confirmPurchase() {
  if (confirm("請確認是否購買該物品\n點擊'確認'完成訂單，點擊'取消'回到上一頁")) {
    // 彈出新的alert並顯示指定的信息
    alert("訂單已成立，詳細資訊請至查詢訂單狀況或email查看");
    
    // 開始對超連結地址跳轉
    window.location.href = "YOUR_URL"; // 將YOUR_URL替換為實際的超連結地址
  } else {
    // 返回上一頁
    window.history.back();
  }
}
