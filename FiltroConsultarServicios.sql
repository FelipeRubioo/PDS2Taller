DECLARE @idServicio INT = NULL; 
DECLARE @nombreServicio nvarchar(50) = NULL;
DECLARE @precio float = NULL;
DECLARE @producto bit = NULL;

SET @idServicio  = {}; 
SET @nombreServicio  = {};
SET @precio  = {};
SET @producto  = {};


-- Your SELECT statement with optional parameters
SELECT idServicio, nombreServicio, precio, producto
FROM Servicio
WHERE
    (@idServicio IS NULL OR idServicio = @idServicio)
    AND
    (@nombreServicio IS NULL OR nombreServicio = @nombreServicio)
    AND
    (@precio IS NULL OR precio = @precio)
	AND
	(@producto IS NULL OR producto = @producto);
	