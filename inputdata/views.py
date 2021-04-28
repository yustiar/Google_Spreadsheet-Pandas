from django.shortcuts import render


# from .models import Post
# Create your views here.
def index(request):

	# base_data = Post.objects.all()
	# print(base_data)
	# basemaster = list(Post.objects.values('namakk','alamat','jumlahart','nomorhp','latitude','longitude'))	


	# if request.method == 'POST':
	# 	print('!!!!!!!!!!!!!!!!!!!!!!!!!!')
	# 	print(request.POST['hotjsonvalue'])

	
	context = {
		'Title' : 'Leaflet Tinatar | Input Data',
		'Heading' : 'Input Data',

	}

	return render(request, 'inputdata/index.html', context)