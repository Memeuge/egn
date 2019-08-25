# GS Hack Challenge

##Equipo: Develoopers - 2938

##Elastic Green Notificatios

![alt text](https://github.com/Memeuge/egn/blob/master/readme/Diagrama.png)


# SERVICIO API NOTIFICATIONS
  - código: egn_api [a relative link](egn_api/README.md)

  Este subproyecto contiene el API Rest principal por donde llegan las peticiones de mensajes del banco y está expuesta, es capaz de ser configurada para que solo reciba peticiones de una IP especifica.
  Este subproyecto está desarrollado en Python3 y se monta sobre App Engine Flexible.

  Su funcionalidad es recibir el mensaje del banco y agregarlo a la cola de mensaje adecuada para ser enviado por whatsapp, sms o correo electrónico

# SERVICIOS DE INTEGRACIÓN
 - código: egn_notifications [a relative link](egn_notifications/README.md)

 Este proyecto contiene los servicios que obtienen los datos de las colas de Pub/Sub y hacen la integración hacia los servicios de whatsapp, sms o correo electrónico
