-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 03, 2023 at 11:05 AM
-- Server version: 5.6.12-log
-- PHP Version: 5.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `accessoriesrecommendation`
--
CREATE DATABASE IF NOT EXISTS `accessoriesrecommendation` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `accessoriesrecommendation`;

-- --------------------------------------------------------

--
-- Table structure for table `accessories`
--

CREATE TABLE IF NOT EXISTS `accessories` (
  `Accessory_Id` int(11) NOT NULL,
  `AccessoryName` varchar(50) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `DressType` varchar(100) NOT NULL,
  `DressImage` varchar(100) NOT NULL,
  PRIMARY KEY (`Accessory_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `accessories`
--

INSERT INTO `accessories` (`Accessory_Id`, `AccessoryName`, `Gender`, `DressType`, `DressImage`) VALUES
(1, 'Bangle', 'Male', 'Traditional', 'bangle1.jpeg'),
(2, 'Stud', 'Female', 'Traditional', 'stud1.jpg'),
(3, 'Watch', 'Male', 'Modern', 'male-watch2.jpg'),
(4, 'Watch', 'Female', 'Modern', 'female-watch2.jpg'),
(5, 'Watch', 'Female', 'Traditional', 'female-watch1.jpg'),
(6, 'Anklet', 'Female', 'Traditional', 'kolusu1.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `dressdetails`
--

CREATE TABLE IF NOT EXISTS `dressdetails` (
  `DressName` varchar(100) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `DressCategory` varchar(50) NOT NULL,
  `DressImage` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dressdetails`
--

INSERT INTO `dressdetails` (`DressName`, `Gender`, `DressCategory`, `DressImage`) VALUES
('Jeans', 'Male', 'Modern', 'jeans1_men.jpg'),
('Jeans', 'Male', 'Modern', 'jeans2_men.jpg'),
('Jeans', 'Female', 'Modern', 'jeans_women.jpg'),
('Jeans', 'Female', 'Modern', 'jeans2_women.jpeg'),
('Saree', 'Female', 'Traditional', 'saree1.jpg'),
('Saree', 'Female', 'Traditional', 'saree2.jpeg'),
('Saree', 'Female', 'Traditional', 'saree3.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `newuser`
--

CREATE TABLE IF NOT EXISTS `newuser` (
  `Name` varchar(50) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `DOB` date NOT NULL,
  `Age` int(11) NOT NULL,
  `city` varchar(50) NOT NULL,
  `MailId` varchar(50) NOT NULL,
  `MobileNo` varchar(15) NOT NULL,
  `Userid` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL,
  PRIMARY KEY (`Userid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `newuser`
--

INSERT INTO `newuser` (`Name`, `Gender`, `DOB`, `Age`, `city`, `MailId`, `MobileNo`, `Userid`, `Password`) VALUES
('SasiKumar.A.M', 'Male', '1978-06-22', 45, 'Madurai', 'amsasi@gmail.com', '9842168547', 'amsasi', 'amsasi'),
('PremKumar.M', 'Male', '1977-03-23', 46, 'Chennai', 'prem@gmail.com', '9994914485', 'prem', 'prem'),
('PriyaaSasi', 'Female', '2009-05-04', 14, 'Madurai', 'priyaa@gmail.com', '9842168547', 'priyaa', 'priyaa');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
