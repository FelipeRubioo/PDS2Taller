DECLARE @idVehiculo INT = NULL; 
DECLARE @marca nvarchar(20) = NULL;
DECLARE @modelo nvarchar(20) = NULL;
DECLARE @color nvarchar(20) = NULL;
DECLARE @kilometraje nvarchar(7) = NULL;
DECLARE @numeroSerie nchar(10) = NULL;
DECLARE @placa nvarchar(8) = NULL;
DECLARE @idCliente INT = NULL;

SET @idVehiculo  = '{}'; 
SET @marca  = '{}';
SET @modelo  = '{}';
SET @color  = '{}';
SET @kilometraje  = '{}';
SET @numeroSerie  = '{}';
SET @placa = '{}';
SET @idCliente  = '{}';

-- UPDATE
UPDATE Vehiculo
   SET marca = @marca,
       modelo = @modelo,
       color = @color,
       kilometraje = @kilometraje,
       numeroSerie = @numeroSerie,
       placa = @placa,
       idCliente = @idCliente

 WHERE idVehiculo = @idVehiculo
