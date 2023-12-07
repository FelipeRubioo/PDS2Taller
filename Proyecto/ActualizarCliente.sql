DECLARE @idCliente INT = NULL; 
DECLARE @nombreCliente nvarchar(50) = NULL;
DECLARE @rfc nvarchar(50) = NULL;
DECLARE @email nvarchar(50) = NULL;
DECLARE @telefono nvarchar(10) = NULL;
DECLARE @direccion nvarchar(50) = NULL;

SET @idCliente  = '{}'; 
SET @nombreCliente  = '{}';
SET @rfc  = '{}';
SET @email  = '{}';
SET @telefono  = '{}';
SET @direccion  = '{}';

--UPDATE
UPDATE Cliente
SET nombreCliente = @nombreCliente,
    rfc = @rfc,
    email = @email,
    telefono = @telefono,
    direccion = @direccion

WHERE idCliente = @idCliente
