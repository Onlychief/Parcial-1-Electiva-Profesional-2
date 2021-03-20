-- --------------------------------------------------------
-- Host:                         localhost
-- Versión del servidor:         5.7.24 - MySQL Community Server (GPL)
-- SO del servidor:              Win64
-- HeidiSQL Versión:             10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para user
CREATE DATABASE IF NOT EXISTS `user` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `user`;

-- Volcando estructura para tabla user.datosuser
CREATE TABLE IF NOT EXISTS `datosuser` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `apellido` varchar(255) DEFAULT NULL,
  `celular` varchar(255) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL,
  `contrasenia` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla user.datosuser: ~9 rows (aproximadamente)
/*!40000 ALTER TABLE `datosuser` DISABLE KEYS */;
INSERT INTO `datosuser` (`id`, `nombre`, `apellido`, `celular`, `correo`, `contrasenia`) VALUES
	(4, 'yoni', 'Jaramildlox', '55555', 'Jhony@gmaild.com', 'Jhonatan%$%344'),
	(5, 'ramiro', 'lopez', '3203719867', 'jl@gmail.com', '12345Aa#'),
	(6, 'pedrito', 'lopez', '3203719763', 'pedrosisimo@gmail.com', 'Aa@12334567'),
	(7, 'Jhonatand', 'Jaramildlox', '55555', 'Jhony@gmaild.com', 'Jhonatan%$%344'),
	(8, 'Jhonatand', 'Jaramildlox', '55555', 'Jhony@gmaild.com', 'Jhonatan%$%344'),
	(9, 'Jhonatand', 'Jaramildlox', '55555', 'Jhony@gmaild.com', 'Jhonatan%$%344'),
	(10, 'Jhonatand', 'Jaramildlox', '55555', 'Jhony@gmaild.com', 'Jhonatan%$%344'),
	(11, 'Jhonatan', 'Jaramillo', 'Jhonfds', 'jjhonata@mgil', 'fds%%$'),
	(12, 'Jhonatan', 'Jaramillo', 'Jhonfds', 'jjhonata@mgil', 'fffgdf%$');
/*!40000 ALTER TABLE `datosuser` ENABLE KEYS */;

-- Volcando estructura para tabla user.insumos
CREATE TABLE IF NOT EXISTS `insumos` (
  `id` int(11) NOT NULL,
  `insumospruebados` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla user.insumos: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `insumos` DISABLE KEYS */;
/*!40000 ALTER TABLE `insumos` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
