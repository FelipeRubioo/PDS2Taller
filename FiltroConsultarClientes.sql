DECLARE @idCliente INT = NULL; 
DECLARE @nombreCliente nvarchar(50) = NULL;
DECLARE @rfc nvarchar(50) = NULL;
DECLARE @email nvarchar(50) = NULL;
DECLARE @telefono nvarchar(10) = NULL;
DECLARE @direccion nvarchar(50) = NULL;

SET @idCliente  = {}; 
SET @nombreCliente  = {};
SET @rfc  = {};
SET @email  = {};
SET @telefono  = {};
SET @direccion  = {};

-- Your SELECT statement with optional parameters
SELECT *
FROM Cliente
WHERE
    (@idCliente IS NULL OR idCliente = @idCliente)
    AND
    (@nombreCliente IS NULL OR nombreCliente = @nombreCliente)
    AND
    (@rfc IS NULL OR rfc = @rfc)
	AND
	(@email IS NULL OR email = @email)
	AND
	(@telefono IS NULL OR telefono = @telefono)
	AND
	(@direccion IS NULL OR direccion = @direccion);
	


