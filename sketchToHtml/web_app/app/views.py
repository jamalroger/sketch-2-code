# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.views.generic import TemplateView
import os
from django.conf import settings 
# Create your views here.
class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'index.html')
class sketchcode(TemplateView):
	def post(self, request, **kwargs):
		myfile = request.FILES['file']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		img_url = fs.url(filename)
		convert_img= os.path.join(settings.BASE_DIR,'app/convert_single_image.py')
		path_img = os.path.join(settings.BASE_DIR,'app'+img_url)
		output_folder=os.path.join(settings.BASE_DIR,'app/media/')
		json_file =os.path.join(settings.BASE_DIR,'bin/model_json.json')
		model_w_f= os.path.join(settings.BASE_DIR,'bin/weights.h5')
		os.system("python3 /sketchToHtml/sketch_code/src/convert_single_image.py --png_path /sketchToHtml/web_app"+img_url+" --output_folder /sketchToHtml/web_app/media --model_json_file /sketchToHtml/sketch_code/bin/model_json.json --model_weights_file /sketchToHtml/sketch_code/bin/weights.h5")
        #os.system("python3 "+convert_img + " --png_path "+path_img+ " --output_folder "+ output_folder +" --model_json_file "+json_file+" --model_weights_file "+model_w_f)
		#subprocess32.call(["python3",convert_img,"--png_path",path_img,"--output_folder",output_folder,"--model_json_file",json_file,"--model_weights_file",model_w_f])
		url_file,extension = img_url.rsplit(".")
		return render(request,'sketchcode.html',{'html_url':url_file+".html" })
	def get(self, request, **kwargs):
		return render(request, 'sketchcode.html')
class doc2pdf(TemplateView):
	def post(self, request, **kwargs):
		myfile = request.FILES['file']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		file_url = fs.url(filename)
		os.system("doc2pdf /sketchToHtml/web_app"+file_url)
		url_pdf,extension = file_url.rsplit(".")
		return render(request,'doc2pdf.html',{'pdf_url':url_pdf+".pdf" })
	def get(self, request, **kwargs):
		return render(request, 'doc2pdf.html')
class contact(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'contact.html')
class support(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'support.html')
class google(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'google8bce582a947019d2.html')
class ads(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'ads.txt')

