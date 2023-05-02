-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- 主機： localhost
-- 產生時間： 
-- 伺服器版本： 8.0.17
-- PHP 版本： 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
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
  `A_Email` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `A_Password` varchar(65) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `A_StuID` varchar(9) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `A_RealNameVerify` tinyint(1) DEFAULT NULL,
  `A_BirthDate` date DEFAULT NULL,
  `A_Major` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `account_manage`
--

INSERT INTO `account_manage` (`A_Email`, `A_Password`, `A_StuID`, `A_RealNameVerify`, `A_BirthDate`, `A_Major`) VALUES
('cherry911219@gmail.com', '$2b$12$/sKSfh7TR.S4F6fI7xSwDu/syU8aJbtob7MHmq4RcerLg5wNz0tYm', '410402226', 0, '2022-06-02', '資訊管理學系'),
('shioubi0216@gmail.com', '$2b$12$499rklXJAjYP/H/OkLbNVeSQbl6VM.il90.haYNzAc8gZiESagATS', '410402407', 0, '2023-05-10', '醫學系'),
('wsx2244667@gmail.com', '$2b$12$5oQ7JJqoEjI1mf07r9vuau.LG6IPK51vDtRzl49On/m.5Nc01DEJO', '410402408', 0, '2023-05-12', '音樂學系'),
('test1@gmail.com', '$2b$12$Hkv0sBLsT5wtp930sJ6kj.O1/VpIuF2/0Dh274.RVEvAmE1dEVVme', 'test1', 1, '2023-05-02', '圖書資訊學系'),
('test111@gmail.com', '$2b$12$deX46FQLyTQXUiKSBgTY0eynwSsFZUX5XapT9QmXu/9qymJNktX/u', 'test111', 0, '2023-02-09', '職能治療學系');

-- --------------------------------------------------------

--
-- 資料表結構 `book_information`
--

CREATE TABLE `book_information` (
  `B_BookID` int(10) NOT NULL,
  `B_BookName` varchar(75) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `B_ISBN` varchar(11) COLLATE utf8mb4_general_ci NOT NULL,
  `B_Author` varchar(15) COLLATE utf8mb4_general_ci NOT NULL,
  `B_BookVersion` varchar(3) COLLATE utf8mb4_general_ci NOT NULL,
  `B_BookMajor` varchar(3) COLLATE utf8mb4_general_ci NOT NULL,
  `B_LessonName` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `B_BookPic` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `B_BookStatus` int(4) NOT NULL,
  `B_UsedStatus` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `B_UsedByTeacher` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `B_Extra_Info` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `B_Price` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `book_information`
--

INSERT INTO `book_information` (`B_BookID`, `B_BookName`, `B_ISBN`, `B_Author`, `B_BookVersion`, `B_BookMajor`, `B_LessonName`, `B_BookPic`, `B_BookStatus`, `B_UsedStatus`, `B_UsedByTeacher`, `B_Extra_Info`, `B_Price`) VALUES
(1, 'ドコデモ日本語', '11111111111', 'LiveABC', '1', '全人', '基礎日文', 'test1.jpg', 1, '測試1\r\n                        ', '教師1', '測試2\r\n                        ', 200),
(2, '輔仁大學國文課本大學國文選', '45557555555', '輔仁大學國文系教師', '202', '全人', '國文', 'test3.jpg', 3, '~說明文字~\r\n                        ', 'authot', '~說明文字~\r\n                        ', 289),
(3, '資訊管理', '8888888888', 'author3', '14', '資訊管', '資訊管理', '資訊管理.jpg', 1, '有鉛筆筆記\r\n                        ', '教師3', '~說明文字~\r\n                        ', 530),
(4, 'english', '99999999999', 'author1', '2.3', '資管', '英文', 'GearUp.jpg', 1, '鉛筆筆跡\r\n                        ', '2', '補充\r\n                        ', 240);

-- --------------------------------------------------------

--
-- 資料表結構 `order_information`
--

CREATE TABLE `order_information` (
  `O_OrderID` int(10) NOT NULL,
  `O_OrderTime` datetime DEFAULT NULL,
  `O_LockerID` varchar(2) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `B_BookID` int(10) NOT NULL,
  `A_BuyerID` varchar(9) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `A_SalerID` varchar(9) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
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
  ADD KEY `B_BookID` (`B_BookID`);

--
-- 資料表索引 `order_information`
--
ALTER TABLE `order_information`
  ADD PRIMARY KEY (`O_OrderID`),
  ADD KEY `B_BookID` (`B_BookID`),
  ADD KEY `A_BuyerID` (`A_BuyerID`),
  ADD KEY `A_SalerID` (`A_SalerID`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `book_information`
--
ALTER TABLE `book_information`
  MODIFY `B_BookID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- 已傾印資料表的限制式
--

--
-- 資料表的限制式 `order_information`
--
ALTER TABLE `order_information`
  ADD CONSTRAINT `order_information_ibfk_1` FOREIGN KEY (`B_BookID`) REFERENCES `book_information` (`B_BookID`),
  ADD CONSTRAINT `order_information_ibfk_2` FOREIGN KEY (`A_BuyerID`) REFERENCES `account_manage` (`A_StuID`),
  ADD CONSTRAINT `order_information_ibfk_3` FOREIGN KEY (`A_SalerID`) REFERENCES `account_manage` (`A_StuID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
