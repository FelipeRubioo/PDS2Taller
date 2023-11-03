DECLARE @idVehiculo INT = NULL; 
DECLARE @marca nvarchar(20) = NULL;
DECLARE @modelo nvarchar(20) = NULL;
DECLARE @color nvarchar(20) = NULL;
DECLARE @kilometraje nvarchar(7) = NULL;
DECLARE @numeroSerie nchar(10) = NULL;
DECLARE @placa nvarchar(8) = NULL;
DECLARE @idCliente INT = NULL;

SET @idVehiculo  = {}; 
SET @marca  = {};
SET @modelo  = {};
SET @color  = {};
SET @kilometraje  = {};
SET @numeroSerie  = {};
SET @placa = {};
SET @idCliente  = {};

-- Your SELECT statement with optional parameters
SELECT idVehiculo, marca, modelo, color, kilometraje, numeroSerie, placa, idCliente
FROM Vehiculo
WHERE
    (@idVehiculo IS NULL OR idVehiculo = @idVehiculo)
    AND
    (@marca IS NULL OR marca = @marca)
    AND
    (@modelo IS NULL OR modelo = @modelo)
	AND
	(@color IS NULL OR color = @color)
	AND
	(@kilometraje IS NULL OR kilometraje = @kilometraje)
	AND
	(@numeroSerie IS NULL OR numeroSerie = @numeroSerie)
	AND
	(@placa IS NULL OR placa = @placa)
	AND
	(@idCliente IS NULL OR idCliente = @idCliente);


