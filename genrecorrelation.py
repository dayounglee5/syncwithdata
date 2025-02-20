import numpy as np

def merge_genre_probabilities(prob_dict):
    merged = {}
    for genre, prob in prob_dict.items():
        if genre == "Pop/Pop":
            merged["Pop"] = merged.get("Pop", 0) + prob
        elif genre == "Rock/Rock":
            merged["Rock"] = merged.get("Rock", 0) + prob
        else:
            merged[genre] = merged.get(genre, 0) + prob
    return merged

tv_genre_song_probabilities = {
    "Action/Adventure": {"Rock": 0.9775, "Pop": 0.0225},
    "Comedy/Sitcom": {"Pop": 0.2046 + 0.2158, "Rock": 0.5796},  
    "Crime/Thriller": {"Pop": 0.3903 + 0.4773, "Rock": 0.0313},  
    "Drama": {"Pop": 0.459, "Rock": 0.1202 + 0.2901},  
    "Fantasy": {"Indie Rock": 0.6544},
    "Horror": {"Pop": 0.5982, "Rock": 0.3674, "Electronica": 0.1010},
    "Reality-TV": {"Pop": 1.0},
    "Romance": {"R&B/Hip-Hop": 0.2527, "Rock": 0.3484},
    "Sci-Fi": {"Pop": 0.0856, "Rock": 0.4330 + 0.4814}  
}

def normalize_probabilities(prob_dict):
    total = sum(prob_dict.values())
    if total == 0:
        return {key: 1.0 / len(prob_dict) for key in prob_dict}  
    return {key: value / total for key, value in prob_dict.items()}  

def predict_song_genre(tv_show_genre):
    if tv_show_genre not in tv_genre_song_probabilities:
        return "Unknown Genre"
    
    normalized_probs = normalize_probabilities(tv_genre_song_probabilities[tv_show_genre])
    
    genres = list(normalized_probs.keys())
    probabilities = list(normalized_probs.values())
    
    return np.random.choice(genres, p=probabilities)

if __name__ == "__main__":
    tv_show = input("Enter a TV show genre: ")
    predicted_genre = predict_song_genre(tv_show)
    print(f"For a '{tv_show}' show, the recommended song genre is: {predicted_genre}")