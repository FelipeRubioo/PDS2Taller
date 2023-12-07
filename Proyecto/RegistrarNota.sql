DECLARE @fechaGeneracion DATE = GETDATE();
DECLARE @plazoCredito DATE = NULL;
DECLARE @facturado bit = NULL;
DECLARE @idCliente int = NULL;
DECLARE @idVehiculo int = NULL;
DECLARE @idServicio int = NULL;
DECLARE @cantidadProducto int = NULL;
DECLARE @precioNeto float = NULL;
DECLARE @precioImpuestos float = NULL;
DECLARE @precioTotal float = NULL;

SET @plazoCredito = '{}'; 
SET @facturado = {}; 
SET @idCliente = {}; 
SET @idVehiculo = {}; 
SET @idServicio = {}; 
SET @cantidadProducto = {};
SET @precioNeto = {};
SET @precioImpuestos = {};
SET @precioTotal = {};

INSERT INTO NotaServicio (fechaGeneracion, plazoCredito, facturado, idCliente,
                            idVehiculo, idServicio, cantidadProducto,
                            precioNeto, precioImpuestos, precioTotal)
VALUES (@fechaGeneracion, @plazoCredito, @facturado, @idCliente,
        @idVehiculo, @idServicio, @cantidadProducto,
        @precioNeto, @precioImpuestos, @precioTotal);