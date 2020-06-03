from django.test import TestCase
from .models import Image,Profile,Likes,Comments
# Test for Profile

class ProfileTestClass(TestCase):
    #Set up Method
    def setUp(self):
        '''
        test case for profiles
        '''
        self.user = User.objects.create_user('testuser','password')
        self.profile = Profile(bio='I am a testcase',photo='', user='')
        self.profile.save_profile()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profles) > 0)

    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profiel) == 0)

    def test_search_by_profile(self):
        profiles = Profile.search_profile('')
        self.assertTrue(len(profiles)>0

# Test for Image class

class ImageTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(bio='I am a testcase',photo='',user='')
        self.proile.save_profile()


        self.image = Image(name='image test', picture='my test',caption='a caption test', profile='', profile_det=self.profile)
        self.image.save_image()

        self.likes = Likes(image = self.image, user = '')
        self.likes.save_like()

        self.comments = Comments(comment='',image=self.image, user = '')
        self.comment.save_comment()


    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def tearDown(self):
        self.image.delete_image()
        self.profile.delete_profile()


    def test_save_method(self):
        self.image.save_image()
        images  = Image.objects.all()
        self.assertTrue(len(images)>0)


    def test_get_all_images(self):
        images = Image.get_all_images()
        self.assertTrue(len(images)>0)

    def test_get_image_by_id(self):
        images= Image.get_image_by_id(self.image.id)
        self.assertTrue(len(images) == 1)

    def test_get_profile_pic(self):
        images = Image.get_profile_pic(profile.id)
        self.assertTrue(len(images)>0)

    def test_count_likes(self):
        images = Image.count_likes()
        self.assertTrue(images.likes.count()>0)

    def test_count_comments(self):
        images = Image.count_comments()
        self.assertTrue(len(images.comments.count())>0)



class LikesTest(TestCase):
    def setUp(self):
        self.profile = Profile(bio='I am a testcase',photo='',user='')
        self.profile.save_profile()

        self.image = Image(name='image test', picture='my test',caption='a caption test', profile='', profile_det=self.profile)
        self.image.save_image()

        self.likes = Likes(image = self.image, user = '')
        self.likes.save_like()

        self.comments = Comments(comment='',image=self.image, user = '')
        self.comment.save_comment()


    def test_instance(self):
        self.assertTrue(isinstance(self.likes,Like))

    def test_save_method(self):
        self.profile.save_like()
        like = Like.objects.all()
        self.assertTrue(len(like) > 0)

    def test_unlike_method(self):
        self.like.save_like()
        self.like.unlike_like()
        like = Like.objects.all()
        self.assertTrue(len(like) == 0)

class CommentsTest(TestCase):
    def setUp(self):
        self.profile = Profile(bio='I am a testcase',photo='',user='')
        self.proile.save_profile()

        self.image = Image(name='image test', picture='my test',caption='a caption test', profile='', profile_det=self.profile)
        self.image.save_image()

        self.likes = Likes(image = self.image, user = '')
        self.likes.save_like()

        self.comments = Comments(comment='',image=self.image, user = '')
        self.comment.save_comment()


    def test_instance(self):
        self.assertTrue(isinstance(self.comments,Comments))

    def test_save_method(self):
        self.comments.save_comment()
        comment = Comments.objects.all()
        self.assertTrue(len(comments) > 0)

    def test_delete_method(self):
        self.comments.save_comment
        self.comments.delete_comment()
        comments = Comments.objects.all()
        self.assertTrue(len(comments) == 0)