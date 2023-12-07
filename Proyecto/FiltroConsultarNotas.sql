DECLARE @idNota INT = NULL; 
DECLARE @fechaGeneracion DATE = NULL;
DECLARE @plazoCredito DATE = NULL;
DECLARE @facturado bit = NULL;
DECLARE @idCliente int = NULL;
DECLARE @idVehiculo int = NULL;
DECLARE @idServicio int = NULL;
DECLARE @cantidadProducto int = NULL;
DECLARE @precioNeto float = NULL;
DECLARE @precioImpuestos float = NULL;
DECLARE @precioTotal float = NULL;

SET @idNota  = {}; 
SET @fechaGeneracion  = {};
SET @plazoCredito  = {};
SET @facturado  = {};
SET @idCliente  = {};
SET @idVehiculo  = {};
SET @idServicio = {};
SET @cantidadProducto  = {};
SET @precioNeto  = {};
SET @precioImpuestos  = {};
SET @precioTotal  = {};

-- Your SELECT statement with optional parameters
SELECT *
FROM NotaServicio
WHERE
    (@idNota IS NULL OR idNota = @idNota)
    AND
    (@fechaGeneracion IS NULL OR fechaGeneracion = @fechaGeneracion)
    AND
    (@plazoCredito IS NULL OR plazoCredito = @plazoCredito)
	AND
	(@facturado IS NULL OR facturado = @facturado)
	AND
	(@idCliente IS NULL OR idCliente = @idCliente)
	AND
	(@idVehiculo IS NULL OR idVehiculo = @idVehiculo)
	AND
	(@idServicio IS NULL OR idServicio = @idServicio)
	AND
	(@cantidadProducto IS NULL OR cantidadProducto = @cantidadProducto)
    AND
	(@precioNeto IS NULL OR precioNeto = @precioNeto)
    AND
	(@precioImpuestos IS NULL OR precioImpuestos = @precioImpuestos)
    AND
	(@precioTotal IS NULL OR precioTotal = @precioTotal)

ORDER BY fechaGeneracion DESC;