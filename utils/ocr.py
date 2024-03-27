import easyocr


def readImageFile(filePath):
    """
    Reads the text content from an image file using optical character recognition (OCR).

    Args:
        filePath (str): The path to the image file.

    Returns:
        list: A list of strings representing the text content extracted from the image.

    Raises:
        None

    Example:
        >>> readImageFile('/path/to/image.jpg')
        ['Hello', 'World']
    """
    reader = easyocr.Reader(['ch_sim', 'en'])
    result = reader.readtext('../static/images/' + filePath)
    content = []
    for (bbox, text, prob) in result:
        content.append(text)
        
    print(content)
    return content

    
readImageFile('test.jpg')