from django.shortcuts import render, redirect
from . models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()

    context = {
        'movies':movies
    }
    return render(request, 'movies/index.html', context)

def new(request):

    return render(request, 'movies/new.html')

def create(request):
    #POST된 데이터를 가져오기!
    # print(request.POST)
    # question = Question()
    # movie2 는 클래스의 생성자. 비어있는거지만, Movie의 형식은 가지고있는!!!!!
    # question = Question.objects.get(pk=question_pk)#이렇게 부르는 건'기존'것을 찾도록 인스턴스!저장. / Question매니저님, pk가 def update(request, question_pk)여기서 유알엘이랑 넘어온 숫자인 question_pk인 인스턴스 하나 찾아주세요!
    # 위처럼 가지고 오는 것은 pk정보가 포함된 특정데이터!
    # movie2 = Movie() 빈 클래스를 만들어준 것 데이터만 비어있는 클래스(db에서는 테이블)
    # 빈 국영수 칸만 만들어놓는 식! / 데이터가 들어가기 위한 자리를 만들어둠!
    movie2 = Movie()
    movie2.title = request.POST.get('ttl_for_server')
    movie2.overview =request.POST.get('ovv_for_server')
    movie2.poster_path =request.POST.get('pp_for_server')
    movie2.save()

    #A
    # return redirect('movies:index') #전체영화니까 특정pk가 아님.movie2.pk 필요없음
    #B
    return redirect('movies:detail', movie2.pk) #방금만든 movie2테이블 추가분에서 pk를 들고옴(def내)
    

def detail(request, movie_pk):
    movie1 = Movie.objects.get(pk=movie_pk)
    context = {
        'movie1':movie1
    }
    return render(request, 'movies/detail.html', context)

def edit(request, movie_pk):
    #특정 movie를 edit해야하므로
    movie3 = Movie.objects.get(pk=movie_pk)

    #html에 띄워줄 것.
    context = {
        'movie333' : movie3
    }
    return render(request, 'movies/edit.html', context)

def update(request, movie_pk):
    #edit.html에서 POST방식으로 요청을 보냈으니. 받아줘야.
    # request.POST  #이게 받은 것.
    print(request.POST)

    # 특정 pk에 해당하는 데이터를 테이블에 update하므로.
    # 일단 데이터가 들어가기 위한 자리를 만들어둠!
    movie4 = Movie.objects.get(pk=movie_pk)
    # 생성자에 미리 데이터를 셋팅해놓는 경우도 있으므로(기본세팅) 다 비었다고할 수는 없음
    # pk는 지금 값이 다 차있는상태인데, 데이터를 '수정'하여 저장해주는 것.
    # 위에서는 빈것. 이건 아예 빈 것. movie2 = Movie()
    movie4.title = request.POST.get('ttl_for_server')
    movie4.overview = request.POST.get('ovv_for_server')
    movie4.poster_path = request.POST.get('pp_for_server')
    movie4.save()
    return redirect('movies:detail', movie4.pk)

def delete(request, movie_pk):
    movie5 = Movie.objects.get(pk=movie_pk)#이렇게 부르는 건'기존'것을 찾도록 인스턴스!저장. / Question매니저님, pk가 def update(request, question_pk)여기서 유알엘이랑 넘어온 숫자인 question_pk인 인스턴스 하나 찾아주세요!
    if request.method == "POST":
        movie5.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie5.pk)