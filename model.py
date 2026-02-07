# Dummy model implementation

def predict_image(image):
    """
    Simulates image prediction.
    Args:
        image: PIL Image object

    Returns:
        tuple: (result, confidence)
    """
    # For demonstration, return a dummy result and confidence
    result = "cat"
    confidence = 0.95
    return result, confidence