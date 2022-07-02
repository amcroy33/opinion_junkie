let favButtons = document.querySelectorAll('.fav-btn');
let csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0]

// console.log(csrfToken)

const axiosConfig = {
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken.value
    },
    xsrfHeaderName: 'X-CSRFToken'
  }

function handleFavEvent(event){

    // console.log(event)
    
    let movieId = event.target.id

    movieId = movieId.split('-')[2]

    url = 'http://127.0.0.1:8000/favorite/' + movieId

    axios.post(url, {}, axiosConfig)
    .then(response=>{
      const Favorited = response.data.Favorited

      const FavBtn = event.target.querySelector(`.fav-btn-icon`)

      if(Favorited){
        FavBtn.classList.remove('bi-bookmark-heart')
        FavBtn.classList.add('bi-bookmark-heart-fill')
      } else {
        FavBtn.classList.remove('bi-bookmark-heart-fill')
        FavBtn.classList.add('bi-bookmark-heart')
      }
    })
    .catch(error=>console.log(error))
}