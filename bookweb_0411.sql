-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2023 年 04 月 12 日 10:50
-- 伺服器版本： 10.4.27-MariaDB
-- PHP 版本： 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `bookweb_0411`
--

-- --------------------------------------------------------

--
-- 資料表結構 `account_manage`
--

CREATE TABLE `account_manage` (
  `A_Account` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `A_Password` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `A_StuID` varchar(9) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `A_RealNameVerify` tinyint(1) DEFAULT NULL,
  `A_BirthDate` date DEFAULT NULL,
  `A_Major` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  `B_Extra_Info` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `order_information`
--

CREATE TABLE `order_information` (
  `O_OrderID` int(10) NOT NULL,
  `O_OrderTime` datetime DEFAULT NULL,
  `O_LockerID` varchar(2) DEFAULT NULL,
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
