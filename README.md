# song-recommendation-system

### Table of Contents
- [Demo](#demo)
- [Overview](#overview)
- [Motivation](#motivation)
- [Technical Aspect](#technical-aspect)
- [Installation](#installation)
- [Run](#run)
- [Deployment on Render](#deployment-on-render)
- [Directory Tree](#directory-tree)
- [To Do](#to-do)
- [Bug / Feature Request](#bug--feature-request)
- [Technologies Used](#technologies-used)
- [Team](#team)
- [License](#license)
- [Credits](#credits)

---

## Demo
This project provides movie recommendations based on content similarity using machine learning techniques.<br>
**Link to Demo:** [Movie-Recommender-System](#) 

## song recommendation system

![Movie Recommender](https://i.imgur.com/Mb5qOcx.png)

---

## Overview
The **Movie-Recommender-System** project leverages natural language processing (NLP) and machine learning techniques to suggest movies based on user preferences.

Key features:
- Content-based filtering for movie recommendations.
- Data preprocessing using Bag-of-Words (BoW).
- Web-based interface for user interaction.

## Model Performance

### Evaluation Metrics
- **Cosine Similarity Score**: Measures the closeness of movies based on textual descriptions.

### Model Training Details
- **Vectorization**: BoW (Term Frequency-Inverse Document Frequency)
- **Similarity Calculation**: Cosine Similarity
- **Dataset**: TMDB 5000 Movies Dataset

---

## Motivation
Recommender systems help users discover movies based on their interests, improving their movie-watching experience.

This project showcases the application of NLP and machine learning for movie recommendation based on textual metadata.

---

## Technical Aspect
### Training Movie Recommendation Model:
1. **Data Collection**:
   - Movies dataset collected from TMDB (The Movie Database).

2. **Preprocessing**:
   - Cleaning movie descriptions by removing special characters and stopwords.
   - Converting text to numerical representations using Bag-of-Words (BoW).

3. **Model Training**:
   - Computing similarity between movies using Cosine Similarity.

4. **Web Application**:
   - A Flask-based web app allows users to enter movie names and receive recommendations.
   - The app is deployed on Render for public access.
  
---

## Installation
The Code is written in Python 3.10. Install the required packages and libraries by running:

```bash
pip install -r requirements.txt
```

## Run
To run the Flask web app locally:

```bash
python app.py
```

## Deployment on Render

To deploy the Flask web app on Render:
- Push your code to GitHub.
- Log in to Render and create a new web service.
- Connect the GitHub repository.
- Configure environment variables (if any).
- Deploy and access your app live.

## Directory Tree 
```
Movie-Recommender-System/
│
├── data/                # Movie dataset
├── model/               # Trained models
├── static/              # Static files (CSS, JS, Images)
│   ├── css/
│   ├── js/
│   └── images/
├── templates/           # HTML templates
│   └── index.html
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── app.py               # Main Flask application
```

## To Do

- Expand dataset for better recommendations.
- Experiment with collaborative filtering.
- Integrate user-based recommendations.

## Bug / Feature Request
If you encounter any bugs or want to request a new feature, please open an issue on GitHub. Contributions are welcome!

## Technologies Used
- Python 3.10
- scikit-learn
- Flask (for web app development)
- Render (for hosting and deployment)
- pandas (for data manipulation)
- numpy (for numerical computations)





![](https://forthebadge.com/images/badges/made-with-python.svg)


[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/260px-Scikit_learn_logo_small.svg.png" width=170>](https://pandas.pydata.org/docs/)
[<img target="_blank" src="https://miro.medium.com/v2/resize:fit:720/format:webp/0*RWkQ0Fziw792xa0S" width=170>](https://pandas.pydata.org/docs/)
 [<img target="_blank" src="https://icon2.cleanpng.com/20180829/okc/kisspng-flask-python-web-framework-representational-state-flask-stickker-1713946755581.webp" width=170>](https://flask.palletsprojects.com/en/stable/) 
[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/512px-NumPy_logo_2020.svg.png" width=200>](https://numpy.org/doc/) 







## Team
This project was developed by:
[![Bablu kumar pandey](https://github.com/Creator-Turbo/images-/blob/main/resized_image.png?raw=true)](ressume_link) |
-|


**Bablu Kumar Pandey**


- [GitHub](https://github.com/Creator-Turbo)  
- [LinkedIn](https://www.linkedin.com/in/bablu-kumar-pandey-313764286/)
* **Personal Website**: [My Portfolio](https://creator-turbo.github.io/Creator-Turbo-Portfolio-website/)

## License

This project is licensed under the [MIT License](LICENSE).

You are free to use, modify, and distribute this software under the terms of the MIT License. For more details, see the [LICENSE](LICENSE) file included in this repository.


## Credits

Special thanks to the contributors of the scikit-learn library for their fantastic machine learning tools.