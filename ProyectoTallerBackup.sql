USE [master]
GO
/****** Object:  Database [ProyectoTaller]    Script Date: 26/10/2023 11:28:17 a. m. ******/
CREATE DATABASE [ProyectoTaller]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'ProyectoTaller', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\ProyectoTaller.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'ProyectoTaller_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\ProyectoTaller_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [ProyectoTaller] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [ProyectoTaller].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [ProyectoTaller] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [ProyectoTaller] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [ProyectoTaller] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [ProyectoTaller] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [ProyectoTaller] SET ARITHABORT OFF 
GO
ALTER DATABASE [ProyectoTaller] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [ProyectoTaller] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [ProyectoTaller] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [ProyectoTaller] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [ProyectoTaller] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [ProyectoTaller] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [ProyectoTaller] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [ProyectoTaller] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [ProyectoTaller] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [ProyectoTaller] SET  DISABLE_BROKER 
GO
ALTER DATABASE [ProyectoTaller] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [ProyectoTaller] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [ProyectoTaller] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [ProyectoTaller] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [ProyectoTaller] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [ProyectoTaller] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [ProyectoTaller] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [ProyectoTaller] SET RECOVERY FULL 
GO
ALTER DATABASE [ProyectoTaller] SET  MULTI_USER 
GO
ALTER DATABASE [ProyectoTaller] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [ProyectoTaller] SET DB_CHAINING OFF 
GO
ALTER DATABASE [ProyectoTaller] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [ProyectoTaller] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [ProyectoTaller] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [ProyectoTaller] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'ProyectoTaller', N'ON'
GO
ALTER DATABASE [ProyectoTaller] SET QUERY_STORE = OFF
GO
USE [ProyectoTaller]
GO
/****** Object:  Table [dbo].[Admin]    Script Date: 26/10/2023 11:28:18 a. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Admin](
	[idAdmin] [int] IDENTITY(1,1) NOT NULL,
	[correo] [nvarchar](20) NOT NULL,
	[contraseña] [nvarchar](20) NOT NULL,
	[nombre] [nvarchar](50) NOT NULL,
	[rfc] [nvarchar](50) NOT NULL,
	[telefono] [nvarchar](50) NOT NULL,
	[direccion] [nvarchar](50) NOT NULL,
 CONSTRAINT [PK_Clientes] PRIMARY KEY CLUSTERED 
(
	[idAdmin] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Cliente]    Script Date: 26/10/2023 11:28:18 a. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Cliente](
	[idCliente] [int] IDENTITY(1,1) NOT NULL,
	[nombreCliente] [nvarchar](50) NOT NULL,
	[rfc] [nvarchar](50) NULL,
	[email] [nvarchar](50) NULL,
	[telefono] [nvarchar](10) NULL,
	[direccion] [nvarchar](50) NULL,
 CONSTRAINT [PK_Cliente] PRIMARY KEY CLUSTERED 
(
	[idCliente] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[NotaServicio]    Script Date: 26/10/2023 11:28:18 a. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[NotaServicio](
	[idNota] [int] IDENTITY(1,1) NOT NULL,
	[fechaGeneracion] [date] NOT NULL,
	[plazoCredito] [date] NOT NULL,
	[facturado] [bit] NOT NULL,
	[idCliente] [int] NOT NULL,
	[idServicio] [int] NOT NULL,
	[idProducto] [int] NOT NULL,
	[cantidadProducto] [int] NOT NULL,
	[precioNeto] [float] NOT NULL,
	[precioImpuestos] [float] NOT NULL,
	[precioTotal] [float] NOT NULL,
 CONSTRAINT [PK_NotaServicio] PRIMARY KEY CLUSTERED 
(
	[idNota] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Producto]    Script Date: 26/10/2023 11:28:18 a. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Producto](
	[idProducto] [int] IDENTITY(1,1) NOT NULL,
	[nombreProducto] [nvarchar](20) NOT NULL,
	[precio] [float] NOT NULL,
 CONSTRAINT [PK_Producto] PRIMARY KEY CLUSTERED 
(
	[idProducto] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Servicio]    Script Date: 26/10/2023 11:28:18 a. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Servicio](
	[idServicio] [int] IDENTITY(1,1) NOT NULL,
	[nombreServicio] [nvarchar](50) NOT NULL,
	[precio] [float] NOT NULL,
	[producto] [bit] NULL,
 CONSTRAINT [PK_Servicio] PRIMARY KEY CLUSTERED 
(
	[idServicio] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Vehiculo]    Script Date: 26/10/2023 11:28:18 a. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Vehiculo](
	[idVehiculo] [int] IDENTITY(1,1) NOT NULL,
	[marca] [nvarchar](20) NOT NULL,
	[modelo] [nvarchar](20) NOT NULL,
	[color] [nvarchar](20) NOT NULL,
	[kilometraje] [nvarchar](7) NULL,
	[numeroSerie] [nchar](10) NOT NULL,
	[placa] [nvarchar](8) NOT NULL,
	[idCliente] [int] NOT NULL,
 CONSTRAINT [PK_Vehiculo] PRIMARY KEY CLUSTERED 
(
	[idVehiculo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
USE [master]
GO
ALTER DATABASE [ProyectoTaller] SET  READ_WRITE 
GO
