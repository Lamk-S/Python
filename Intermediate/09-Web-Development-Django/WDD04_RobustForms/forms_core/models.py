from django.db import models

class TransaccionPago(models.Model):
    ESTADOS_PAGO = [
        ('PENDIENTE', 'Pendiente'),
        ('APROBADO', 'Aprobado'),
        ('RECHAZADO', 'Rechazado'),
    ]

    titular = models.CharField(max_length=100, verbose_name="Titular de la tarjeta")
    monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto a pagar")
    ultimos_digitos = models.CharField(max_length=4, verbose_name="Últimos 4 dígitos")
    estado = models.CharField(max_length=20, choices=ESTADOS_PAGO, default='PENDIENTE')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de transacción")

    def __str__(self):
        return f"{self.titular} - ${self.monto} ({self.estado})"