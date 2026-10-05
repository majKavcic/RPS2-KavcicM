-- --------------------------------------------------------
-- Strežnik:                     127.0.0.1
-- Verzija strežnika:            10.4.24-MariaDB - mariadb.org binary distribution
-- Operacijski sistem strežnika: Win64
-- HeidiSQL Različica:           12.18.0.7304
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for itm
DROP DATABASE IF EXISTS `itm`;
CREATE DATABASE IF NOT EXISTS `itm` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `itm`;

-- Dumping structure for tabela itm.dnevnik
DROP TABLE IF EXISTS `dnevnik`;
CREATE TABLE IF NOT EXISTS `dnevnik` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `DatumCas` date DEFAULT NULL,
  `visina` float DEFAULT NULL,
  `teza` float DEFAULT NULL,
  `itm` float DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table itm.dnevnik: ~0 rows (približno)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
