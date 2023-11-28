from openai import OpenAI
from django.shortcuts import render
from django.http import JsonResponse
import urllib.request
from PIL import Image as PILImage

client = OpenAI()
OpenAI.api_key = "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"  # Replace with your OpenAI API key


def generate_image(image_description):
    img_response = client.images.generate(
        prompt=image_description,
        model="dall-e-3"
        n=1,
        size="1024x1024"
    )

    img_url = img_response.data[0].url
    urllib.request.urlretrieve(img_url, 'imageapp/static/img.png')
    img = PILImage.open("imageapp/static/img.png")
    return img

def generate_image_view(request):
    if request.method == 'POST':
        img_description = request.POST.get('img_description')
        if img_description:
            generated_img = generate_image(img_description)
            return JsonResponse({'img_url': 'static/img.png'})
        else:
            return JsonResponse({'error': 'Please provide an image description.'}, status=400)
    return render(request, 'index.html')
