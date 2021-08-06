-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 06, 2021 at 09:53 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `harga`
--

-- --------------------------------------------------------

--
-- Table structure for table `all_in`
--

CREATE TABLE `all_in` (
  `Jns_ Kendaraan` varchar(500) NOT NULL,
  `type_kendaran` varchar(255) NOT NULL,
  `Thn_pembuatan` varchar(255) NOT NULL,
  `warna` text NOT NULL,
  `Hrg_dlm_kota` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `all_in`
--

INSERT INTO `all_in` (`Jns_ Kendaraan`, `type_kendaran`, `Thn_pembuatan`, `warna`, `Hrg_dlm_kota`) VALUES
('Alphard G', 'Facelift', '2019', 'Hitam', 'Rp.2.900.000'),
('Alphard G', 'Transformer', '2017 Up', 'Hitam, Putih', 'Rp.2.800.000'),
('Mercedez-Benz', 'E 250', '2018', 'Hitam', 'Rp.3.600.000'),
('Mercedes-Benz', 'E 300 AMG', '2018', 'Hitam, Putih', 'Rp.3.700.000'),
('Mercedes-Benz', 'S400', '2018', 'Hitam', 'Rp.14.500.000'),
('Mercedes-Benz', 'S450', '2018', 'Hitam', 'Rp.16.500.000'),
('Pajero Sport', 'Dakar 2x4', '2018', 'Hitam, Putih', 'Rp. 1.800.000'),
('Fortuner', 'VRZ-TRD', '2018 - 2019', 'Hitam, Putih', 'Rp. 1.800.000'),
('Elf Long', '19 Seat', '2017', 'Silver', 'Hubungi Via Whatsapp Kami'),
('Hiace', 'Commuter M/T DSL 19', '2017 - 2019', 'Putih', 'Hubungi Via Whatsapp Kami'),
('Hyundai H1', 'Royale A/T DSL 8 Seat', '2018', 'Hitam, Putih', 'Hubungi Via Whatsapp Kami'),
('CR-V Turbo', 'Prestige', '2019', 'Hitam', 'Rp. 1.800.000'),
('Innova Reborn', 'Matic - Diesel', '2019', 'Hitam, Putih', 'Rp. 1.200.000'),
('Xpander', 'Ultimate', '2019', 'Hitam, Putih, Merah', 'Rp. 900.000'),
('Toyota Voxy', '-', '2019', 'Hitam', 'Rp. 1.800.000'),
('Toyota Camry', '2.5 V A/T', '2019', 'Hitam', 'Rp. 2.600.000');

-- --------------------------------------------------------

--
-- Table structure for table `lepas_kunci`
--

CREATE TABLE `lepas_kunci` (
  `Jns_ Kendaraan` varchar(255) NOT NULL,
  `typ_mbl` varchar(255) NOT NULL,
  `Thn_pembuatan` varchar(255) NOT NULL,
  `warna` text NOT NULL,
  `Hrg_dlm_kota` varchar(255) NOT NULL,
  `Hrg_luar_kota` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `lepas_kunci`
--

INSERT INTO `lepas_kunci` (`Jns_ Kendaraan`, `typ_mbl`, `Thn_pembuatan`, `warna`, `Hrg_dlm_kota`, `Hrg_luar_kota`) VALUES
('Alphard G', 'Facelift', '2019', 'Hitam', 'Rp. 2.100.000', 'Hubungi Via Whatsapp Kami'),
('Alphard G', 'Transformer', '2017 Up', 'Hitam, Putih', 'Rp. 2.000.000', 'Hubungi Via Whatsapp Kami'),
('Mercedez-Benz', 'E 250', '2018', 'Hitam', 'Rp. 2.800.000', 'Hubungi Via Whatsapp Kami'),
('Mercedes-Benz', 'E300 AMG', '2018', 'Hitam, Putih', 'Rp. 3.200.000', 'Hubungi Via Whatsapp Kami'),
('Mercedes-Benz', 'S400', '2018', 'Hitam', 'Rp. 10.500.000', 'Hubungi Via Whatsapp Kami'),
('Mercedes-Benz', 'S450', '2018', 'Hitam', 'Hubungi Via Whatsapp Kami', 'Hubungi Via Whatsapp Kami'),
('Pajero Sport', 'Dakar 2x4', '2018', 'Hitam, Putih', 'Rp. 1.200.000', 'Hubungi Via Whatsapp Kami'),
('Fortuner', 'VRZ-TRD', '2018 - 2019', 'Hitam, Putih', 'Rp. 1.200.000', 'Hubungi Via Whatsapp Kami'),
('Elf Long', '19 Seat', '2017', 'Silver', 'Hubungi Via Whatsapp Kami', 'Hubungi Via Whatsapp Kami'),
('Hiace', 'Commuter M/T DSL 19', '2017 - 2019', 'Putih', 'Hubunngi Via Whatsapp Kami', 'Hubunngi Via Whatsapp Kami'),
('Hyundai H1', 'Royale A/T DSL 8 Seat\r\n', '2018', 'Hitam, Putih', 'Rp. 1.400.000', 'Hubungi Via Whatsapp Kami'),
('CR-V Turbo', 'Prestige', '2019', 'Hitam', 'Rp. 1.300.000', 'Hubungi Via Whatsapp Kami'),
('Innova Reborn', 'Matic - Diesel', '2019', 'Hitam, Putih', 'Rp. 600.000', 'Hubungi Via Whatsapp Kami'),
('Xpander', 'Ultimate', '2019', 'Hitam, Putih, Merah', 'Rp. 450.000', 'Hubungi Via Whatsapp Kami'),
('Toyota Voxy', 'MPV', '2017 - 2019', 'Hitam', 'Rp. 1.100.000', 'Hubungi Via Whatsapp Kami'),
('Toyota Camry', '2.5 V A/T', '2019', 'Hitam', 'Rp. 1.400.000', 'Hubungi Via Whatsapp Kami');

-- --------------------------------------------------------

--
-- Table structure for table `mbl_spr`
--

CREATE TABLE `mbl_spr` (
  `jns_kendaraan` varchar(255) NOT NULL,
  `typ_mbl` varchar(255) NOT NULL,
  `Thn_pembuatan` varchar(255) NOT NULL,
  `warna` text NOT NULL,
  `Hrg_dlm_kota` varchar(255) NOT NULL,
  `Hrg_luar_kota` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `mbl_spr`
--

INSERT INTO `mbl_spr` (`jns_kendaraan`, `typ_mbl`, `Thn_pembuatan`, `warna`, `Hrg_dlm_kota`, `Hrg_luar_kota`) VALUES
('Alphard G', 'Facelift', '2019', 'Hitam', 'Rp.2.500.000', 'Hubungi Via Whatsapp Kami'),
('Alphard G', 'Transformer', '2017 Up', 'Hitam, Putih', 'Rp. 2.400.000', 'Hubungi Via Whatsapp Kami'),
('Mercedez-Benz', 'E 250', '2018', 'Hitam', 'Rp. 2.800.000', 'Hubungi Via Whatsapp Kami'),
('Mercedes-Benz', 'E300 AMG', '2018', 'Hitam, Putih', 'Rp. 3.000.000', 'Hubungi Via Whatsapp Kami'),
('Mercedes-Benz', 'S400', '2018', 'Hitam', 'Rp. 14.500.000', 'Hubungi Via Whatsapp Kami'),
('Mercedes-Benz', 'S450', '2018', 'Hitam', 'Rp. 12.500.000', 'Hubungi Via Whatsapp Kami'),
('Pajero Sport', 'Pajero Sport', '2018', 'Hitam, Putih', 'Rp. 1.400.000', 'Hubungi Via Whatsapp Kami'),
('Fortuner', 'VRZ-TRD', '2018-2019', 'Hitam, Putih', 'Rp. 1.400.000', 'Hubungi Via Whatsapp Kami'),
('Elf Long', '19 Seat', '2017', 'Silver', 'Hubungi Via Whatsapp Kami', 'Hubungi Via Whatsapp Kami'),
('Hiace', 'Commuter M/T DSL 19', '2017-2019', 'Putih', 'HUbungi Via Whatsapp Kami', 'HUbungi Via Whatsapp Kami'),
('Hyundai H1', 'Royale A/T DSL 8 Seat', '2018', 'Hitam, Putih', 'Hubungi Via Whatsapp Kami', 'Hubungi Via Whatsapp Kami'),
('CR-V Turbo', 'Prestige', '2019', 'Hitam', 'Rp. 1.400.000', 'Hubungi Via Whatsapp Kami'),
('Innova Reborn', 'Matic - Diesel', '2019', 'Hitam, Putih', 'Rp. 800.000', 'Hubungi Via Whatsapp Kami'),
('Xpander', 'Ultimate', '2019', 'Hitam, Putih, Merah', 'Rp. 650.000', 'Hubungi Via Whatsapp Kami'),
('Toyota Voxy', 'MPV', '2017 - 2019', 'Hitam', 'Rp. 1.500.000', 'Hubungi Via Whatsapp Kami'),
('Toyota Camry', '2.5 V A/T', '2019', 'Hitam', 'Rp. 1.800.000', 'Hubungi Via Whatsapp Kami');

-- --------------------------------------------------------

--
-- Table structure for table `sop_allin`
--

CREATE TABLE `sop_allin` (
  `1` varchar(255) NOT NULL,
  `2` varchar(255) NOT NULL,
  `3` varchar(255) NOT NULL,
  `4` varchar(255) NOT NULL,
  `5` varchar(255) NOT NULL,
  `6` varchar(255) NOT NULL,
  `7` varchar(255) NOT NULL,
  `8` varchar(255) NOT NULL,
  `9` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sop_allin`
--

INSERT INTO `sop_allin` (`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`) VALUES
('Rincian harga All in diatas tidak mengikat dan dapat berubah sewaktu-waktu.', 'Dalam kota (Jabodetabek- dengan batasan ciawi , karawang, dan cikupa).', 'Kendaraan sewa yang digunakan lewat dari durasi sewa dikenakan biaya overtime 10% dari harga sewa kendaraan.', 'Sewa Lepas kunci perhari (unit only) : Perhari/ Pertanggal , Pukul 00.00 / 23:59 WIB , Perbulan 30 hari.', 'Sewa 12 jam / full day durasi cut off jam 23:59 , Harga sudah termasuk BBM, Toll, Parkir dan Penginapan sopir (jika luar kota) permalam Rp. 100.000- s/d Rp. 200.000(Jika ada), Harga sewa tidak termasuk tiket tempat wisata (Jika Ada).', 'Harga tarif luar kota sesuai daerah tujuan.', 'Booking Call by admin : 081294686040, 082114380022, 08118062075. OFFICE (021) 22830782.', 'Pemesan valid dan sah setelah pembayaran DP sebesar 50%, jika customer tanpa konfirmasi pemesanan selama 3 jam maka akan dibatalkan pemesananya.', 'Jika unit sewa yang anda butuhkan tidak terdaftar hubungi admin.');

-- --------------------------------------------------------

--
-- Table structure for table `sop_lk`
--

CREATE TABLE `sop_lk` (
  `1` varchar(255) NOT NULL,
  `2` varchar(255) NOT NULL,
  `3` varchar(255) NOT NULL,
  `4` varchar(255) NOT NULL,
  `5` varchar(255) NOT NULL,
  `6` varchar(255) NOT NULL,
  `7` varchar(255) NOT NULL,
  `8` varchar(255) NOT NULL,
  `9` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sop_lk`
--

INSERT INTO `sop_lk` (`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`) VALUES
('Rincian harga sewa mobil lepas kunci diatas tidak mengikat dan dapat berubah sewaktu-waktu.', 'Dalam kota (Jabodetabek- dengan batasan ciawi , karawang, dan cikupa).', 'Kendaraan sewa yang digunakan lewat dari durasi sewa dikenakan biaya overtime 10% dari harga sewa kendaraan.', 'Sewa Lepas kunci perhari ( unit only ) : Perhari/ Pertanggal , Pukul 00.00 / 23:59 WIB , Perbulan 30 hari.', 'Biaya survei ( non- Refundable ) dan ongkos antar jemput kendaraan tergantung lokasi.', 'Booking Call by admin : 081294686040, 082114380022, 08118062075. OFFICE (021) 22830782.', 'Pemesan valid dan sah setelah pembayaran DP sebesar 50%, jika customer tanpa konfirmasi pemesanan selama 3 jam maka akan dibatalkan pemesananya.', 'Syarat dan ketentuan yang berlaku.', 'Jika unit sewa yang anda butuhkan tidak terdaftar hubungi admin.');

-- --------------------------------------------------------

--
-- Table structure for table `sop_ms`
--

CREATE TABLE `sop_ms` (
  `1` varchar(255) NOT NULL,
  `2` varchar(255) NOT NULL,
  `3` varchar(255) NOT NULL,
  `4` varchar(255) NOT NULL,
  `5` varchar(255) NOT NULL,
  `6` varchar(255) NOT NULL,
  `7` varchar(255) NOT NULL,
  `8` varchar(255) NOT NULL,
  `9` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sop_ms`
--

INSERT INTO `sop_ms` (`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`) VALUES
('Rincian harga sewa mobil dengan driver diatas tidak mengikat dan dapat berubah sewaktu-waktu.', 'Dalam kota (Jabodetabek- dengan batasan ciawi , karawang, dan cikupa).', 'Kendaraan sewa yang digunakan lewat dari durasi sewa dikenakan biaya overtime 10% dari harga sewa kendaraan.', 'Sewa Lepas kunci perhari ( unit only ) : Perhari/ Pertanggal , Pukul 00.00 / 23:59 WIB , Perbulan 30 hari.', 'Sewa 12 jam / full day durasi cut off jam 23:59 , Harga tidak termasuk BBM, Toll, Parkir dan Penginapan sopir (jika luar kota) permalam Rp. 100.000- s/d Rp. 200.000(Jika ada), Harga sewa tidak termasuk tiket tempat wisata (Jika Ada).', 'Harga tarif luar kota sesuai daerah tujuan.', 'Booking Call by admin : 081294686040, 082114380022, 08118062075. OFFICE (021) 22830782.', 'Pemesan valid dan sah setelah pembayaran DP sebesar 50%, jika customer tanpa konfirmasi pemesanan selama 3 jam maka akan dibatalkan pemesananya.', 'Jika unit sewa yang anda butuhkan tidak terdaftar hubungi admin.');

-- --------------------------------------------------------

--
-- Table structure for table `sop_wedding`
--

CREATE TABLE `sop_wedding` (
  `1` varchar(255) NOT NULL,
  `2` varchar(255) NOT NULL,
  `3` varchar(255) NOT NULL,
  `4` varchar(255) NOT NULL,
  `5` varchar(255) NOT NULL,
  `6` varchar(255) NOT NULL,
  `7` varchar(255) NOT NULL,
  `8` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sop_wedding`
--

INSERT INTO `sop_wedding` (`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`) VALUES
('Rincian harga sewa mobil pengantin di atas tidak mengikat dan dapat berubah sewaktu-waktu.', 'Dalam kota (Jabodetabek- dengan batasan ciawi , karawang, dan cikupa).', 'Kendaraan sewa yang digunakan lewat dari durasi sewa dikenakan biaya overtime 10% dari harga sewa kendaraan.', 'Harga termasuk jasa driver, BBM, Tol, Parkir dan tidak termasuk tiket wisata.', 'Sewa 12 jam / full day, Harga tidak termasuk BBM, Toll, Parkir dan Penginapan sopir (jika luar kota) permalam Rp. 100.000- s/d Rp. 200.000(Jika ada) Harga sewa diluar tiket tempat wisata (Jika ada).', 'Jika unit sewa yang anda butuhkan tidak terdaftar hubungi admin.', 'Booking Call by admin : 081294686040, 082114380022, 08118062075. OFFICE (021) 22830782.', 'Pemesan valid dan sah setelah pembayaran DP sebesar 50%, jika customer tanpa konfirmasi pemesanan selama 3 jam maka akan dibatalkan pemesananya.');

-- --------------------------------------------------------

--
-- Table structure for table `wedding_full`
--

CREATE TABLE `wedding_full` (
  `Jenis` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `pembuatan` varchar(255) NOT NULL,
  `warna` text NOT NULL,
  `harga1` varchar(255) NOT NULL,
  `harga2` varchar(255) NOT NULL,
  `harga3` varchar(255) NOT NULL,
  `harga4` varchar(255) NOT NULL,
  `harga5` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `wedding_full`
--

INSERT INTO `wedding_full` (`Jenis`, `type`, `pembuatan`, `warna`, `harga1`, `harga2`, `harga3`, `harga4`, `harga5`) VALUES
('Alphard G', 'Facelift', '2019', 'Hitam', 'Rp. 2.900.000', 'Rp. 2.600.000', 'Tidak Tersedia', 'Tidak Tersedia', 'Tidak Tersedia'),
('Alphard G', 'Transformer', '2017 Up', 'Hitam - Putih', 'Rp. 2.800.000', 'Rp. 2.500.000', 'Tidak Tersedia', 'Tidak Tersedia', 'Tidak Tersedia'),
('Mercedez-Benz', 'E 250', '2018', 'Hitam', 'Rp. 4.500.000', 'Rp. 4.000.000', 'Tidak Tersedia', 'Tidak Tersedia', 'Tidak Tersedia'),
('Mercedes-Benz', 'E300 AMG', '2018', 'Hitam - Putih', 'Rp. 4.500.000', 'Rp. 4.000.000', 'Tidak Tersedia', 'Tidak Tersedia', 'Tidak Tersedia'),
('Mercedes-Benz', 'S400', '2018', 'Hitam', 'Tidak Tersedia', 'Rp. 10.500.000', 'Rp. 14.000.000', 'Tidak Tersedia', 'Tidak Tersedia'),
('Mercedes-Benz', 'S450', '2018', 'Hitam', 'Tidak Tersedia', 'Rp. 12.500.000', 'Rp. 16.500.000', 'Tidak Tersedia', 'Tidak Tersedia'),
('CR-V Turbo', 'Prestige', '2019', 'Hitam', 'Tidak Tersedia', 'Tidak Tersedia', 'Tidak Tersedia', 'Rp. 2.500.000', 'Rp. 2.300.000'),
('Toyota Camry', '2.5 V A/T', '2019', 'Hitam', 'Tidak Tersedia', 'Tidak Tersedia', 'Tidak Tersedia', 'Rp. 2.100.000', 'Rp. 1.800.000');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
