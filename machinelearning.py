import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
# import tensorflow as tf
# from tensorflow.keras.models import load_model
import librosa
import librosa.util as librosa_util
# import numpy as np

# loaded_model = load_model('zcr_model.keras')

def extract_zcr(audio_path, window_size=0.02, hop_length=0.01, max_len=100):
    """
    Extracts zero-crossing rate features for an audio file.
    
    Args:
      audio_path: Path to the audio file.
      window_size: Size of the time window (seconds).
      hop_length: Hop length for sliding window (seconds).
    
    Returns:
      zcr_features: A 1D NumPy array of zero-crossing rates.
    """

    # Load audio
    y, _ = librosa.load(audio_path)
    
    # Calculate ZCR features for overlapping windows
    zcr_features = []
    for start in range(0, len(y), int(hop_length * len(y))):
        end = min(start + len(y), start + int(window_size * len(y)))
        window = y[start:end]
        zcr_count = np.sum(np.diff(np.sign(window)) != 0)
        zcr_features.append(zcr_count / (window_size * len(y)))  # Normalize
        

    return np.array(zcr_features[:max_len])

# Load the model
with open('rf_model.pkl', 'rb') as f:
  loaded_rf = pickle.load(f)


if __name__ == '__main__':
    audio_path = 'sample-000000.mp3'
    zcr_features = extract_zcr(audio_path)
    # print(np.array([zcr_features]))
    print(loaded_rf.predict(np.array([zcr_features])))
