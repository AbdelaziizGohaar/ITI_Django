from django.db import models
from django.db.models import Q
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
# ======== Author Model ===============
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    # Dahh Bonus bs msh sha8al :( Mafrood  Add image field
    image = models.ImageField(upload_to='authors/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

# ======== Post Model ===============
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # Dah by Regular image URL field
    image_url = models.URLField(blank=True, null=True)
    # Bonus: Add image file field Msh sha8al brdo :(
    image_file = models.ImageField(upload_to='posts/', blank=True, null=True)

    def __str__(self):
        return self.title
    

# ======== comments Model ===============
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    posted_by = models.CharField(max_length=100)  

    def __str__(self):
        return f"Comment by {self.posted_by} on {self.post.title}"