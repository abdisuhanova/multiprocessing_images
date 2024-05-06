import multiprocessing
import requests
from PIL import Image
from io import BytesIO

def download_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    return image

def main():
    # List of image URLs to download
    image_urls = [
        "https://res.cloudinary.com/demo/image/upload/v1312461204/sample.jpg",
        "https://cdn.pixabay.com/photo/2016/03/08/20/03/flag-1244649_1280.jpg",
        "https://html.com/wp-content/uploads/flamingo.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Cute_dog.jpg/640px-Cute_dog.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR70d3KkFBLHhFnx0_tBzhGHPZemkt5XqYumoJxREF2pw&s"
    ]

    print("Downloading images:")
    # Defining a multiprocessing pool
    pool = multiprocessing.Pool()

    # Perform the image downloads in parallel
    results = []
    for url in image_urls:
        # Apply async to execute function asynchronously
        result = pool.apply_async(download_image, args=(url,))
        results.append(result)

    # Close the pool and wait for all processes to finish
    pool.close()
    pool.join()

    print("Download completed.")

    # Get the downloaded images
    images = [result.get() for result in results]

    # Display the downloaded images
    for i, image in enumerate(images):
        image.show(title=f"Image {i+1}")

if __name__ == "__main__":
    main()
