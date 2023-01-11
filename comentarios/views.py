
from contextlib import _RedirectStream
from .forms import CommentForm
from django.shortcuts import render

 
def post_detailview(request, id):
   
  if request.method == 'POST':
    cf = CommentForm(request.POST or None)
    if cf.is_valid():
      content = request.POST.get('content')
      #comment = CommentForm.objects.create(post = post_mortem, user = request.user, content = content)
      #comment.save()
      #return _RedirectStream(post.get_absolute_url())
    else:
      cf = CommentForm()
       
    context ={
      'comment_form':cf,
      }
    return render(request, 'socio / post_detail.html', context)
# Create your views here.
