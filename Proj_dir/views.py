from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    page_title = 'Home'
    return render(request, 'index/index.html', {'page_title': page_title })

def contact(request):
    page_title = 'Contact Us'
    return render(request, 'index/contact.html', {'page_title': page_title })

def about(request):
    page_title = 'About'
    about_txt = {
    
        "Sub title" : "Lose weight and achieve gains with Gorilla Fitness", 
        "About us: " : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.  Gravida arcu ac tortor dignissim convallis. Eu consequat ac felis donec et. Interdum consectetur libero id faucibus nisl tincidunt eget nullam non. Tristique et egestas quis ipsum suspendisse ultrices gravida. Non quam lacus suspendisse faucibus interdum. Ultricies integer quis auctor elit sed vulputate mi sit. Sit amet luctus venenatis lectus magna fringilla. Diam phasellus vestibulum lorem sed. \
         In pellentesque massa placerat duis.. Lorem ipsum dolor sit amet consectetur adipiscing.  Eget dolor morbi non arcu. Non enim praesent elementum facilisis leo. Nulla pharetra diam sit amet. Tincidunt id aliquet risus feugiat in ante metus dictum at. In metus vulputate eu scelerisque felis imperdiet. Porttitor rhoncus dolor purus non enim. Convallis convallis tellus id interdum velit laoreet id donec ultrices. Elit ullamcorper dignissim cras tincidunt lobortis. Urna condimentum mattis pellentesque id nibh tortor. Accumsan in nisl nisi scelerisque eu ultrices vitae auctor. Venenatis urna cursus eget nunc scelerisque viverra.",   
    }

    benefits = {
                    "Benefit One" : "Lose weight in a controlled manner.",
                    "Benefit Two" : "A personalized diet profile - customized to your unique weight loss goals.",
                    "Benefit Three" : "Track what you eat with just a few clicks from anywhere with an internet connection - at home or at work.",
                    "Benefit Four" : " No matter what diet you\'re on, we can help."
    }
    

    return render(request, 'index/about.html', {'page_title': page_title, 'about_txt' : about_txt, 'benefits': benefits })

