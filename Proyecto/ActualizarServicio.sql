DECLARE @idServicio INT = NULL; 
DECLARE @nombreServicio nvarchar(50) = NULL;
DECLARE @precio float = NULL;
DECLARE @producto bit = NULL;

SET @idServicio  = '{}'; 
SET @nombreServicio  = '{}';
SET @precio  = '{}';
SET @producto  = '{}';


--UPDATE
UPDATE Servicio
SET nombreServicio = @nombreServicio,
    precio = @precio,
    producto = @producto

WHERE idServicio = @idServicio