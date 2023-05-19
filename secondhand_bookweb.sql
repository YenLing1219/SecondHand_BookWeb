-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2023 年 05 月 19 日 23:27
-- 伺服器版本： 10.4.28-MariaDB
-- PHP 版本： 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `secondhand_bookweb`
--

-- --------------------------------------------------------

--
-- 資料表結構 `account_manage`
--

CREATE TABLE `account_manage` (
  `A_Email` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `A_Password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `A_StuID` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `A_RealNameVerify` tinyint(1) DEFAULT NULL,
  `A_BirthDate` date DEFAULT NULL,
  `A_Major` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `A_Nickname` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `A_CreditPoint` int(2) NOT NULL DEFAULT 50,
  `A_TradeCount` int(10) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `account_manage`
--

INSERT INTO `account_manage` (`A_Email`, `A_Password`, `A_StuID`, `A_RealNameVerify`, `A_BirthDate`, `A_Major`, `A_Nickname`, `A_CreditPoint`, `A_TradeCount`) VALUES
('shioubi0216@gmail.com', '$2b$12$4Lf28Xl7d6t1EkIecScc8u1ZQWU36ndFvm7GJ8FNm8CAssSKKC2OK', '410402407', 0, '2023-01-19', '經濟學系、所', '', 0, 0),
('wsx2244667@gmail.com', '$2b$12$QmsxuEa5a/YxaPQ6vbAixu8lQfiwRCQz6S8YYg80Pd9e3Bhfrd1sK', '410402408', 0, '2023-05-09', '音樂學系', '', 0, 0);

-- --------------------------------------------------------

--
-- 資料表結構 `book_information`
--

CREATE TABLE `book_information` (
  `B_BookID` int(10) NOT NULL,
  `B_BookName` varchar(75) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `B_ISBN` varchar(11) NOT NULL,
  `B_Author` varchar(15) NOT NULL,
  `B_BookVersion` varchar(3) NOT NULL,
  `B_BookMajor` varchar(3) NOT NULL,
  `B_LessonName` varchar(20) NOT NULL,
  `B_BookPic` varchar(255) NOT NULL,
  `B_BookStatus` int(4) NOT NULL,
  `B_UsedStatus` varchar(255) NOT NULL,
  `B_UsedByTeacher` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `B_Extra_Info` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `B_Price` int(5) NOT NULL,
  `B_SalerID` varchar(9) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `book_information`
--

INSERT INTO `book_information` (`B_BookID`, `B_BookName`, `B_ISBN`, `B_Author`, `B_BookVersion`, `B_BookMajor`, `B_LessonName`, `B_BookPic`, `B_BookStatus`, `B_UsedStatus`, `B_UsedByTeacher`, `B_Extra_Info`, `B_Price`, `B_SalerID`) VALUES
(1, '1', '111', '111', '110', '資管', 'wfee', 'qefrqfefeff', 1, '寫出來了 超級感動\r\n                        ', '11114', '~說明文字~\r\n                        ', 1500, '410402407'),
(2, '221', '222', 'author', '22', 'adv', 'wfee', 'qefrqfefeff', 1, '~說明文字~\r\n    advadva                    ', 'efqf', '~說明文字~\r\n          advadv              ', 1000, ''),
(3, '333', '3333333', 'hu', '33', '企管', 'akkkk', 'wWWWWWwww', 1, '~說明文字~', '', '~說明文字~', 650, '410402407'),
(4, '444', '5151', '+8448599', '4', '666', '8448', '555', 3, '~說明文字~', '2', '~說明文字~', 600, ''),
(5, 'ug', 'xgx', 'xfgj', 'gjc', '企管', 'xtrjs', 'wwwwwwwww', 1, '~說明文字~\r\n                        ', '55', 'kkk~說明文字~\r\n                        ', 777, ''),
(7, 'ftj', 'sst', 'sthsj', 'fhx', '資管', 'xtrjs', 'ww', 1, '~說明文字~\r\n                        ', 'k', '~說明文字~\r\n                        ', 660, ''),
(8, '33', '45555555555', 'author', '1.1', '財金', '555', 'IMG_0589.PNG', 2, '453\r\n3\r\n\r\n                        ', '', '~說明文字~\r\n                        ', 680, ''),
(9, '999', '355322', 'author3', '1.1', '財金', '666', 'IMG_20180720_093925.jpg', 3, 'hahahahaha\r\n                        ', 'x', 'test test\r\n123\r\n                        ', 720, '');

-- --------------------------------------------------------

--
-- 資料表結構 `order_information`
--

CREATE TABLE `order_information` (
  `O_OrderID` int(10) NOT NULL,
  `O_OrderTime` datetime DEFAULT NULL,
  `O_LockerID` varchar(2) DEFAULT NULL,
  `B_BookID` int(10) NOT NULL,
  `A_BuyerID` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `B_SalerID` varchar(9) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `O_OrderStatus` varchar(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `account_manage`
--
ALTER TABLE `account_manage`
  ADD PRIMARY KEY (`A_StuID`);

--
-- 資料表索引 `book_information`
--
ALTER TABLE `book_information`
  ADD PRIMARY KEY (`B_BookID`),
  ADD KEY `B_BookID` (`B_BookID`),
  ADD KEY `B_SalerID` (`B_SalerID`);

--
-- 資料表索引 `order_information`
--
ALTER TABLE `order_information`
  ADD PRIMARY KEY (`O_OrderID`),
  ADD KEY `B_BookID` (`B_BookID`),
  ADD KEY `A_BuyerID` (`A_BuyerID`),
  ADD KEY `B_SalerID` (`B_SalerID`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `book_information`
--
ALTER TABLE `book_information`
  MODIFY `B_BookID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- 已傾印資料表的限制式
--

--
-- 資料表的限制式 `order_information`
--
ALTER TABLE `order_information`
  ADD CONSTRAINT `order_information_ibfk_1` FOREIGN KEY (`B_BookID`) REFERENCES `book_information` (`B_BookID`),
  ADD CONSTRAINT `order_information_ibfk_2` FOREIGN KEY (`A_BuyerID`) REFERENCES `account_manage` (`A_StuID`),
  ADD CONSTRAINT `order_information_ibfk_3` FOREIGN KEY (`B_SalerID`) REFERENCES `book_information` (`B_SalerID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
