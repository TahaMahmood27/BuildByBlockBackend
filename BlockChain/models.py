from django.db import models
from django.contrib.auth.models import User

class BlockChain(models.Model):
    file = models.FileField(upload_to='blockchain/')
    upload_date = models.DateField(auto_now_add=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Only allow admins to update the status field
        if self.pk is not None:
            orig = BlockChain.objects.get(pk=self.pk)
            if orig.status != self.status and not self.user.is_staff:
                raise PermissionError("Only admin users can update the status field.")
        super().save(*args, **kwargs)
