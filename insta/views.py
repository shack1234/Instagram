from django.http  import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Image, Profile, Comments,Likes
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProfileForm, ImageForm, SignupForm, CommentForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from friendship.models import Friend, Follow, Block


# Create your views here.
def signup(request):
    title='Signup Page'
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form,'title':title})

@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.get_all_images()
    likes = Likes.objects.all()
    profiles = Profile.objects.all()
    comments = Comments.objects.all()
    profileimage=  User.objects.all()
    following = Follow.objects.following(request.user)
    form = CommentForm()

    id = request.user.id
    liked_images = Likes.objects.filter(user_id=id)
    mylist = [i.image_id for i in liked_images]

    title = 'Home Page'
    return render(request, 'index.html', {'title':title, 'images':images, 'profileimage':profileimage, 'following':following, 'form':form, 'comments':comments, 'profiles':profiles,'likes':likes,'list':mylist})

@login_required(login_url='/accounts/login/')
def comment(request,image_id):
    if request.method == 'POST':
        image = get_object_or_404(Image, pk = image_id)
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.image = image
            comment.save()
            return redirect('index')
    else:
        form = CommentForm()

    title = 'Home'
    return render(request, 'index.html', {'title':title})

@login_required(login_url='/accounts/login/')
def home(request):

    title = 'Home'
    return render(request, 'registration/home.html', {'title':title})

@login_required(login_url='/accounts/login/')
def profile(request, username):
    title = "Profile"
    profile = User.objects.get(username=username)
    comments = Comments.objects.all()
    users = User.objects.get(username=username)
    follow = len(Follow.objects.followers(users))
    following = len(Follow.objects.following(users))
    people_following = Follow.objects.following(request.user)
    id = request.user.id
    liked_images = Likes.objects.filter(user_id=id)
    mylist = [i.image_id for i in liked_images]
    form = CommentForm()

    try :
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)


    images = Image.get_profile_pic(profile.id)
    return render(request, 'profile/profile.html', {'title':title, 'comments':comments,'profile':profile, 'profile_details':profile_details, 'images':images, 'follow':follow, 'following':following, 'list':mylist,'people_following':people_following,'form':form})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    title="Edit"
    profile = User.objects.get(username=request.user)
    try :
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('profile', username=request.user)
    else:
        form = ProfileForm()

    return render(request, 'profile/edit_profile.html', {'form':form, 'profile_details':profile_details})


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users = User.objects.filter(username__icontains = search_term)
        message = f"{search_term}"
        profileimage=  User.objects.all( )
        return render(request, 'search.html',{"message":message,"users": searched_users,'profileimage':profileimage})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def upload_image(request):
        profile = Profile.objects.all()
        form = ImageForm()
        for profile in profile:
            if profile.user.id == request.user.id:
                if request.method == 'POST':
                    form = ImageForm(request.POST, request.FILES)
                    if form.is_valid():
                        upload =form.save(commit=False)
                        upload.profile = request.user
                        upload.profile_det = profile
                        upload.save()
                        return redirect('profile', username=request.user)
                else:
                    form = ImageForm()

        return render(request, 'upload.html',{'form':form})

def follow(request,user_id):
    other_user = User.objects.get(id = user_id)

    follow = Follow.objects.add_follower(request.user, other_user)

    return redirect('index')

def unfollow(request,user_id):
    other_user = User.objects.get(id = user_id)

    follow = Follow.objects.remove_follower(request.user, other_user)

    return redirect('index')


def like(request,image_id):
    images = Image.objects.get(id = image_id)
    liked = Likes.objects.filter(image=image_id, user=request.user).first()
    
    if liked:
        liked.delete()
        return redirect('index')
    else:
        new_like = Likes(image = images, user = request.user)
        likes = new_like.save_like()
        return redirect('index')

def is_liked(request):
    id = request.user.id
    liked_images = Likes.objects.filter(user_id=id)
    mylist = [i.image_id for i in liked_images]
    print(mylist)
    return HttpResponse(liked_images)