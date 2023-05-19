
# 二手書交易平台
***
## 開發工具與環境
  ### python+MySQL 後端資料庫建置
  ### Html 前端網頁建置
  ### Github 協作
***
## MySQL管理設定
### phpmyadmin 預設帳號是 root 密碼為空
### [建議大家統一改成同樣的帳號密碼](https://loki1999.pixnet.net/blog/post/287069464)
***
## 更新MySQL教學
### 這邊教各位如何以最快的速度更新本地的MySQL資料庫
### ~~(起碼是我自己用起來最順的)~~
### 1.下載好sql檔之後(不論是pull下來同步還是什麼)，先打開xampp進入phpmyadmin，點左上角的回到首頁<font color=#FF0000>(紅色圓圈起來的地方)</font>
![](https://hackmd.io/_uploads/rJnSawrBh.png)

### 2.回到首頁之後，在上方的功能欄位的最左邊有一個資料庫，點擊他。
![](https://hackmd.io/_uploads/rkHUADBSn.png)
### 3.然後你會看到現在你電腦上的所有資料庫，<font color=#FF0000>先</font>把二手書欄位的格子打勾起來，<font color=#FF0000>接著勇敢地按下刪除!!!</font>
![](https://hackmd.io/_uploads/SJB8RDSHh.png)
### 4.然後系統會問你真的確定要刪掉嗎? 答案當然是YES，點下去。
![](https://hackmd.io/_uploads/HkrUAvBrn.png)
### 5.下一步我們來更新(復原)資料庫，請在剛剛我們刪除完資料庫的頁面中的上方新建資料庫，輸入"secondhand_bookweb"即可，編碼的話是選單下拉到最下面，倒數幾位的"utf8mb4_unicode_ci"，請記得新建資料庫的名稱，<font color=#FF0000>一定要跟之前下載下來要匯入的sql檔案名稱一致! 很重要!!!</font>
![](https://hackmd.io/_uploads/HJrLCPSr3.png)
### 6.新建完資料庫之後會看見下面的畫面，左邊有出現"secondhand_bookweb"的資料庫就是成功了，接下來點擊上面功能欄位的"<font color=#FF0000>匯入</font>"。
![](https://hackmd.io/_uploads/rJgBIRvHH3.png)
### 7.快結束了! 進到匯入頁面，點擊選擇檔案把剛剛下載下來或是pull下來的sql檔案選起來。
![](https://hackmd.io/_uploads/rJgrU0vHS3.png)
### 8.然後下拉到最底下的"<font color=#FF0000>執行</font>"，點擊下去!!
![](https://hackmd.io/_uploads/r1gH8ADBSn.png)
### 9.大功告成~!! 你的本地資料庫已經更新到最新版本啦~
![](https://hackmd.io/_uploads/rJ-HURwBH2.png)





