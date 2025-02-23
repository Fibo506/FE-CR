# CONFIGURACION PARA POS - ODOO version 17
	A- SECUENCIAS PARA POS

	Ir a ajustes - técnico - Secuencias
	* Crear una secuencia para cada terminal del punto de venta (caja)
	* Nombre de la secuencia + POS 001 (terminando con el terminal para crear una secuencia unica)
	* código de la secuencia: sequence.FE.pos.001
	* Tamaño de la secuencia: 10
	* Siguiente número: Asignar la numeracion de Facturacion Elctronica.
	* Todos los demás campos se dejan como están


	Ir a Contabilidad - Configuracion - Diarios
	* crear un diario para cada punto de venta
	* Nombre corto: F2001 (F+Sucursal+Terminal)
	* Seleccionar las secuencias creadas en el paso anterior
	
	
	configurar los metodos de pago
	configurar el impuesto de venta predeterminado
	Seleccionar el diario para facturas. (diario creado en el paso 1)
	seleccionar cliente predeterminado

	Modificar el diario de la sesion para que coincida con el nombre del Punto de Venta.

	PARA EMITIR FACTURA ELECTRONICA
	1. El cliente debe estar Inscrito. (Se actualiza con el modulo hacienda_info_query)
	2. El cliente Debe tener configuradas las actividades economicas prederterminadas.
 	

	341 TE 
	103 FE 





	Crear las secuencias para cada terminal (CAJA)
	Ir a AJUSTES - TECNICO - SECUENCIAS
	I. Duplicar las secuencias de facturación
		Nombre: Secuencia de Factura Electrónica POS (Tipo doc: 01)
		Cod Sec: sequence.fe.pos (cambiar el nombre es opcional)
		Prefijo: 506%(day)s%(month)s%(y)s0009099909990010000104 (000112540139 cédula, 001 sucursal, 00001 terminal, 04 tipo de documento)
		NOTA: Si es ced jur 003101222222
		Sufijo: 1%(h12)s%(day)s%(month)s%(y)s
		Tamaño de secuencia 10
		Próximo número: (aquí establecer consecutivo para FE, NC, ND, TE y FEE)
	II. Hacer lo mismo para las siguientes secuencias cambiando número de tipo de documento
		Secuencia de Nota Crédito Electrónica POS (T doc: 03)
		Secuencia de Nota Débito Electrónica POS (T doc: 02)
		Secuencia de Tiquete Electrónico POS (T doc: 04)
		Secuencia de Factura Electrónica de Exportación POS (T doc: 09)

	B- DIARIOS
	NOTA: Crear un diario y secuencia para cada caja
	Ir a FACTURACION - CONFIGURACION - DIARIOS
	I. POS SALE JOURNAL
	En la pestaña de Facturación Electrónica asignar las secuencias correspondientes (consecutivo hacienda)
		Secuencia de Factura Electrónica POS
		Secuencia de Tiquete Electrónico POS
		Secuencia de Factura Electrónica de Exportación POS
		Secuencia de Nota Crédito Electrónica POS
		Secuencia de Nota Débito Electrónica POS
		En Branch asignar el número de sucursal
		En Terminal asignar el número correspondiente
		Ejemplo puede usar para la caja 1 Sucursal 1 y para terminal 2, para la caja 2 sucursal 1 terminal 3 y así sucesivamente
		** Verificar la sucursal y terminal en el prefijo de las secuencias de POS **
	En la pestaña de asientos contables (OPCIONAL para el consecutivo interno)
		Código corto: FPOS
		Asignar el próximo número
		Modificar los valores de FPOS Secuencia, sustituir prefijo por: Caja-1/, tamaño de secuencia 10 y desmarcar utilizar subsecuencias por date_range, guardar los cambios y regresar al diario
		Marcar Secuencia de facturas rectificativas dedicada y asignar el número siguiente, guardar los cambios
		Modificar los valores de FPOS: Rectificación Secuencia, sustituir prefijo por: Rect.Caja-1/, tamaño de secuencia 10 y desmarcar utilizar subsecuencias por date_range, guardar los cambios y regresar al diario
	En la pestaña de configuración avanzada
		Marcar agrupar lineas y permitir cancelar asientos (opcional)
	Guardar los cambios

11. FORMAS DE PAGO PARA EL TPV
	En PUNTO DE VENTA - CONFIGURACION - FORMAS DE PAGO
	I. Crear forma de pago Efectivo POS
	Código corto: EFPOS
	Seleccionar las cuentas Ej: Efectivo
	En confIguración avanzada marcar permitir cancelacion de asientos
	Guardar cambios
	
	II. Crear forma de pago Tarjeta POS
	Código corto: TJPOS
	Seleccionar las cuentas Ej: Banco
	En la pestaña de cuenta bancaria seleccionar la cuenta del catálogo
	En configuración avanzada marcar permitir cancelacion de asientos
	Guardar cambios

12. Configuraciones varias
	Ir a la configuración de la terminal POS, en la sección FACTURAS Y RECIBOS, desmarcar la opción de FACTURACION (esto deshabilita el botón en POS)
	En moneda modificar el factor de redondeo deseado Ej para 2 decimales: 0,010000
	En precisión decimal cambiar la cantidad de decimales por cada item según lo requiera (ej: 2 en todos y mantener 15 para currency rate)

13. Clientes exonerados y no sujetos
    I.  Cliente Exonerado
	    Crear o modificar el cliente
		    a. Marcar la opción HAS EXONERATION (esto habilitará las opciones de la exoneración)
		    b. En la pestaña de VENTAS Y COMPRAS agregar la posición fiscal correspondiente a la exoneración
	   	    c. En la pestaña EXONERATION completar todos los campos según la autorización de exonet
        Al asignar el cliente se seleccionará automaticamente la posición fiscal IVA Exonerado al 100%
    II. Cliente no sujeto
        Crear o modificar el cliente
		    a. En la pestaña de VENTAS Y COMPRAS agregar la posición fiscal Exento no sujeto
        Al asignar el cliente se seleccionará automaticamente la posición fiscal Exento no sujeto

14. Configurar módulo de asistencia empleados
	Ir a aplicaciones e instalar el módulo ASISTENCIAS
	Hacer click en EMPLEADOS-CONFIGURACION y crear o modificar el calendario por defecto (de ser necesario establecer los horarios del cliente)
	Hacer click en ASISTENCIAS-CONFIGURACION y marcar la opción de PIN para marcación por modo quiosco
	Ir a EMPLEADOS y crear los empleados que marcaran la asistencia y asociarlos con los usuarios respectivos