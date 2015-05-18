# -*- coding: utf-8 -*-
import webbrowser
import os
import re

# Open tags, head and styles for the page
# head syntax adapted from https://html5boilerplate.com v5.2.0
main_page_head = '''<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>Dave's Trailer Park</title>
    <meta name="description" content="A site showing off movie trailers and information, built as part of a Udacity course.">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap 3.1.0 CSS -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">

    <!-- Fonts -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
    <!-- font-family: 'Fontawesome', sans-serif; -->
    <link href='http://fonts.googleapis.com/css?family=Open+Sans:400,700' rel='stylesheet' type='text/css'>
    <!-- font-family: 'Open Sans', sans-serif; -->
    
    <!-- Page Styles -->
    <style type="text/css" media="screen">
        body {
            padding-top: 6em;
            font-family: 'Open Sans', sans-serif;
        }
        h1, .h1, h2, .h2, h3, .h3, h4, .h4, h5, .h5, h6, .h6 {
            font-family: 'Open Sans', serif;
            font-weight: 700;
        }
        .navbar-brand {
          font-size:2em;
          font-weight: 700;
        }
        .filters {
          padding-bottom: 1em;
        }
        .filters-label {
          display: inline-block;
          width: 4em;
        }
        .movie-container {
          padding-bottom:5em;
          padding-left:0;
          padding-right:0;
        }
        .movie-tile {
            margin-bottom: 1.5em;
            padding-top: 1.5em;
        }
        .movie-tile:hover {
            background-color: #EEE;
        }

        /* Handle floats at different sizes. Clear every 2 up to 991px, every 3 up to 1200, then every 4
           Commented out in favor of using Isotope
        @media (max-width: 991px) {
             .movie-tile:nth-of-type(2n+1) {  
              content: '';
              clear: both;
            }
        }
        @media (min-width: 992px) and (max-width: 1199px) {
             .movie-tile:nth-of-type(3n+1) {  
              content: '';
              clear: both;
            }
        }
        @media (min-width: 1200px) {
             .movie-tile:nth-of-type(4n+1) {  
              content: '';
              clear: both;
            }
        }*/

        .movie-tile img {
          display:block;
          margin: 0 auto;
        }

        /* Handle size and position of art in modal background */
        .movieinfo .modal-background {
          background-size: contain;
          background-position: left;
          background-repeat: no-repeat;
          display: block;
          z-index: -1;
          opacity: .5;
          background-color: #000;
        }

        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
            margin-bottom:2em;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .footer {
          position: fixed;
          bottom: 0;
          width: 100%;
          padding: 2em 0 1em;
          background-color: #f5f5f5;
        }
    </style>
</head>
<body>'''

# The title bar and main page layout
main_page_content = '''
<!--[if lt IE 8]>
<div class="bg-danger alert text-danger browserupgrade"><div class="container">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</div></div>
<![endif]-->
<!-- Navigation -->
    <div class="container nav-container">
      <div class="navbar navbar-default navbar-fixed-top" role="navigation">
        <div class="container">
          <h1>Dave&rsquo;s Trailer Park</h1>
        </div>
      </div>
    </div>

<!-- Sorting Buttons -->
<div id="filters" class="filters container">
  <div class="filters-label">Filter by: </div>
  <div class="btn-group">
    <button data-filter="" class="btn btn-default">Show All</button>
    <button data-filter="comedy" class="btn btn-primary">Comedy</button>
    <button data-filter="action" class="btn btn-primary">Action</button>
    <button data-filter="drama" class="btn btn-primary">Drama</button>
    <button data-filter="sci-fi" class="btn btn-primary">Sci-Fi</button>
    <button data-filter="western" class="btn btn-primary">Western</button> 
  </div> 

</div>
<div id="sorts" class="filters container">
  <div class="filters-label">Sort by:</div> 
  <div class="btn-group">
    <button data-sort-by="title" class="btn btn-default">Title</button>
    <button data-sort-by="year" class="btn btn-primary">Year</button>
    <button data-sort-by="rating" class="btn btn-primary">IMDb Rating</button>
  </div>
</div>

<!-- Main Page Content -->
    <div class="container movie-container">
      {movie_tiles}
    </div>
'''

# The bottom of the page: footer, scripts and close tags
# jQuery: http://jquery.com/
# Bootstrap: http://getbootstrap.com/
# Isotope: http://isotope.metafizzy.co/ 
end_page = '''
    <footer class="footer">
      <div class="container">
        <p class="text-muted pull-right">Trailers from YouTube. Movie data and images from IMDb provided with the help of <a href="http://www.omdbapi.com/" target="_blank">OMDb API</a></p>
      </div>
    </footer>

    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="http://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery.isotope/2.2.0/isotope.pkgd.min.js"></script>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(".movieinfo").on("hidden.bs.modal", function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $(this).find(".trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.play', function (event) {
            event.preventDefault();
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id');
            var targetID = $(this).attr('data-target')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $(targetID).find(".trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        /* Turn off one-by-one animation in favor of the sorting function
          // Animate in the movies when the page loads
          $(document).ready(function () {
            $('.movie-tile').hide().first().show("fast", function showNext() {
              $(this).next("div").show("fast", showNext);
            });
          });
        */
        
        // Isotope scripts
        $(document).ready(function () {
          $('.movie-container').isotope({
            itemSelector: '.movie-tile',
            layoutMode: 'fitRows',
            getSortData: {
              title: function(element) {
                var title = $(element).find(".title").text(); 
                var newtitle = title.replace('The ',''); 
                return newtitle
              },
              year: '.year',
              rating: '.rating',
            },
            sortBy: 'title',
            sortAscending: {
              title: true,
              year: false,
              rating: false
            }
          });
          $('.filters button').on( 'click', function() {
            $(this).removeClass('btn-primary').addClass('btn-default');
            $(this).siblings().removeClass('btn-default').addClass('btn-primary');
          });
          $('#sorts button').on( 'click', function() {
            var sortByValue = $(this).attr('data-sort-by');
            $('.movie-container').isotope({ sortBy: sortByValue });
          });
          $('#filters button').on( 'click', function() {
            var filterValue = $(this).attr('data-filter');
            $('.movie-container').isotope({ 
              filter: function(){
                var genre = $(this).find('.genre').text();
                return genre.toLowerCase().indexOf(filterValue) >= 0;
              }
            });
          });
        });
    </script>
  </body>
</html>'''

# A single movie entry html template
movie_tile_content = '''
      <div class="col-sm-6 col-md-4 col-lg-3 movie-tile">
          <a class="play" href="#" data-toggle="modal" data-target="#{movie_id}" data-trailer-youtube-id="{trailer_youtube_id}" title="Play trailer of {movie_title}"><img src="{poster_image_url}" height="300" alt="Play trailer of {movie_title}"></a>
          <h3 class="title">{movie_title}</h3>
          <p class="text-left">{movie_storyline}</p>
          <p><a class="play" href="#" data-toggle="modal" data-target="#{movie_id}" data-trailer-youtube-id="{trailer_youtube_id}"><i class="fa fa-play-circle"></i> Play Trailer <span class="sr-only">of {movie_title}</span></a>

          <div class="modal fade movieinfo" id="{movie_id}" tabindex="-1" role="dialog" aria-labelledby="{movie_id}Label" aria-hidden="true">
            <div class="modal modal-background" data-dismiss="modal" style="background-image:url({poster_image_url})"></div>
            <div class="modal-dialog modal-lg">
              <div class="modal-content">
                <div class="modal-header">
                  <button type="button" class="close" data-dismiss="modal" aria-label="Close"><i class="fa fa-times fa-2x"><span class="sr-only">Close</span></i></button>
                  <h3 class="modal-title" id="{movie_id}Label">{movie_title}, <span class="year">{movie_year}</span></h3>
                </div>
                <div class="modal-body">
                  <p><strong><span class="genre">{movie_genre}</span></strong></p>
                  <p>{movie_storyline}</p>
                  <div class="scale-media trailer-video-container"></div>
                  <p>Released {movie_released} / {movie_runtime} / {movie_language} / {movie_country}</p>
                  <p>Awards: {movie_awards}
                  <p>MPAA rating: {movie_rated} / Metascore: <span class="metascore">{movie_metascore}</span> / IMDb Rating: <span class="rating">{movie_imdbRating}</span> ({movie_imdbVotes} votes)</p>
                </div>
              </div>
            </div>
          </div>
 
      </div>

'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.movie_trailer)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.movie_trailer)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.movie_title,
            poster_image_url=movie.movie_poster,
            movie_storyline=movie.movie_plot,
            trailer_youtube_id=trailer_youtube_id,
            movie_id=movie.movie_id,
            movie_year=movie.movie_year,
            movie_genre=movie.movie_genre,
            movie_rated=movie.movie_rated,
            movie_metascore=movie.movie_metascore,
            movie_released=movie.movie_released,
            movie_runtime=movie.movie_runtime,
            movie_language=movie.movie_language,
            movie_country=movie.movie_country,
            movie_awards=movie.movie_awards,
# Getting an ascii codec error when outputting Actors, Directors, and Writers -- need to resolve
#            movie_actors=movie.movie_actors,
#            movie_director=movie.movie_director,
#            movie_writer=movie.movie_writer,
            movie_imdbRating=movie.movie_imdbRating,
            movie_imdbVotes=movie.movie_imdbVotes
        )
    return content


def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('daves_trailer_park.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content + end_page)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
