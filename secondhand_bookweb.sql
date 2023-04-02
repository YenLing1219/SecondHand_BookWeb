-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- 銝餅��嚗� 127.0.0.1
-- ��Ｙ��������嚗� 2023 撟� 04 ��� 02 ��� 09:51
-- 隡箸����函����穿�� 10.4.27-MariaDB
-- PHP �����穿�� 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 鞈����摨恬�� `secondhand_bookweb`
--

-- --------------------------------------------------------

--
-- 鞈����銵函��瑽� `account_manage`
--

CREATE TABLE `account_manage` (
  `A_ID` int(10) NOT NULL,
  `A_Account` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `A_Password` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `A_StuID` varchar(9) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `A_RealNameVerify` tinyint(1) DEFAULT NULL,
  `A_BirthDate` date NOT NULL,
  `A_Major` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- 鞈����銵函��瑽� `book_information`
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
  `B_ExtraInfor` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- 鞈����銵函��瑽� `order_information`
--

CREATE TABLE `order_information` (
  `O_OrderID` int(10) NOT NULL,
  `O_OrderTime` datetime DEFAULT NULL,
  `O_LockerID` varchar(2) DEFAULT NULL,
  `B_BookID` int(10) NOT NULL,
  `A_BuyerID` int(10) NOT NULL,
  `A_SalerID` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 撌脣�曉�啗�����銵函��蝝Ｗ��
--

--
-- 鞈����銵函揣撘� `account_manage`
--
ALTER TABLE `account_manage`
  ADD PRIMARY KEY (`A_ID`),
  ADD KEY `A_ID` (`A_ID`);

--
-- 鞈����銵函揣撘� `book_information`
--
ALTER TABLE `book_information`
  ADD KEY `B_BookID` (`B_BookID`);

--
-- 鞈����銵函揣撘� `order_information`
--
ALTER TABLE `order_information`
  ADD PRIMARY KEY (`O_OrderID`),
  ADD KEY `A_BuyerID` (`A_BuyerID`),
  ADD KEY `A_SalerID` (`A_SalerID`),
  ADD KEY `B_BookID` (`B_BookID`);

--
-- 撌脣�曉�啗�����銵函�������嗅��
--

--
-- 鞈����銵函�������嗅�� `order_information`
--
ALTER TABLE `order_information`
  ADD CONSTRAINT `order_information_ibfk_1` FOREIGN KEY (`A_BuyerID`) REFERENCES `account_manage` (`A_ID`),
  ADD CONSTRAINT `order_information_ibfk_2` FOREIGN KEY (`A_SalerID`) REFERENCES `account_manage` (`A_ID`),
  ADD CONSTRAINT `order_information_ibfk_3` FOREIGN KEY (`B_BookID`) REFERENCES `book_information` (`B_BookID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
