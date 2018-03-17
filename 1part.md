# Doory: a smart mood reader. 

## A typical bad day 
Picture this. It's a rainy day. Wake up at 5 AM. Want to take a shower, but there's no hot water, so _cold shower_. Then you take your car and head to work, but... **traffic**. Another boring day. You feel overwhelmed and, even worse, nobody understands you, neither your workteam neither your family. Once back home, at the end of that bad day, this is Mario:

![alt text](1.gif)

 _Mario arguing with a woman. His ex-wife_.

That is a typical day without Doory. 

## The same day with Doory

With Doory things could have been a little different.

Doory will be able to modify your room atmosphere depending on your current mood. It will control lighthing and music out of the box, but thanks to an open API it will be able to communicate with any other IoT device in your house: smart TVs, essential oil diffusers and even tea-pots.

Playing your favorite playlist, setting the right lighting, Doory will gradually change your mood turning even the worst day into the best one.

![alt text](2.gif)

_Mario and his wife dancing in a perfect room atmosphere, carefully prepared by Doory._

Doory will be able to modify your room atmosphere depending on your current mood. It will control lighthing and music out of the box, but thanks to an open API it will be able to communicate with any other IoT device in your house: smart TVs, essential oil diffusers and even tea-pots. 

## Aesthetic and universal design 

We designed Doory as a small and aesthetic device that should be put on the wall, near a room's entrance. The case has a plain design and will be 3D-printed in two different models: black and white. We kept the size and shape of the case as simple as possible, to better adapt with any room furniture and design.

<img src="https://github.com/2n-1/doory/blob/master/1.jpg" width="200">

## Doory knows how do you feel today

Inside the case, we decided to use a Raspberry PI board with a camera module. The idea is to take a photo whenever a person enters the room to detect his mood. The camera should be directed in the right angle to better capture user's face. We plan to use a motion sensor to detect user's entrance. Mood detection is achieved by using a Python script that connects to Google Cloud Vision API [1] through REST HTTP requests, as shown in the source code below.

```python
...
	camera = picamera.PiCamera()
	camera.capture('photo.jpg')
	credentials = GoogleCredentials.get_application_default()
	service = discovery.build('vision', 'v1', credentials = credentials)
	with open('image.jpg', 'rb') as image:
		image_content = base64.b64encode(image.read())
		service_request = service.images().annotate(body={
			'requests': [{
				'image': {
					'content': image_content.decode('UTF-8')
				},
				'features': [{
					'type': 'FACE_DETECTION',
					'maxResults': 10
				}]
			 }]
		})
...
```

Google Cloud Vision API takes the user's face photo as input and returns a JSON object containing several informations about position and angles of different face parts such as mouth, eyes and nose. Using that data, the API estimates a possible mood the user is feeling in that moment.

```javascript
...
        "boundingPoly": {
          "$ref": "BoundingPoly",
          "description": "The bounding polygon around the face. The coordinates of the bounding box\nare in the original image's scale, as returned in `ImageParams`.\nThe bounding box is computed to \"frame\" the face in accordance with human\nexpectations. It is based on the landmarker results.\nNote that one or more x and/or y coordinates may not be generated in the\n`BoundingPoly` (the polygon will be unbounded) if only a partial face\nappears in the image to be annotated."
        },
        "rollAngle": {
          "description": "Roll angle, which indicates the amount of clockwise/anti-clockwise rotation\nof the face relative to the image vertical about the axis perpendicular to\nthe face. Range [-180,180].",
          "format": "float",
          "type": "number"
        },
...
```

Google Cloud Vision API currently supports four different types of emotions:
- Happiness
- Anger
- Sorrow
- Surprise 

Each supported emotion has a LIKEHOOD value in the API response. This value represents the probability of that emotion to be felt by the user, as shown below:

```javascript
...
        "enumDescriptions": [
            "Unknown likelihood.",
            "It is very unlikely that the image belongs to the specified vertical.",
            "It is unlikely that the image belongs to the specified vertical.",
            "It is possible that the image belongs to the specified vertical.",
            "It is likely that the image belongs to the specified vertical.",
            "It is very likely that the image belongs to the specified vertical."
          ],
          "enum": [
            "UNKNOWN",
            "VERY_UNLIKELY",
            "UNLIKELY",
            "POSSIBLE",
            "LIKELY",
            "VERY_LIKELY"
          ],
...
```
The most likely mood is then selected as follows.

[code]

---

[1] Google Cloud Vision API https://cloud.google.com/vision/docs/reference/rest/

## Lighthing control via XXX board

We used a FRDM-K64F board to emulate the lighthing system. FRDM-K64F board has a single RGB led. We connected Raspberry PI board to FRDM-K64F board using a simple HTTP API. For a better communication between boards we plan to implement Conrad Connect system [2].

<img src="https://github.com/2n-1/doory/blob/master/2.jpg" style="width:20px !important;">

After the Raspberry PI detects user's mood, it sends an HTTP post to the FRDM-K64F board API endpoint containing RGB values. For testing purposes we used the following settings:

| Detected mood | R | G | B | Color shown |
| ------------- | - | - | - | ----------- |
| Anger         | 0 | 0 | 1 | Blue        |
| Happiness     | 0 | 1 | 0 | Green       |
| Sadness       | 1 | 0 | 0 | Red         |
| Surprise      | 1 | 1 | 0 | Yellow      |

---
[2] Conrad Connect https://conradconnect.de/en

## Tell Doory what do you like

Our idea is to make Doory one hundred percent customizable. Everyone has different tastes. Personal tastes in terms of music playlists, lighting preferences and external IoT communication, will be set using a dedicated smartphone application. User will be able to create a personal account with his own tastes. Having a deeper knowledge of the user will help creating a tailor-made atmosphere for every occasion. No matter how stressed you will be, Doory will know how to change your day in a positive way.

## Doory talks with your home 

We plan to provide an open API for Doory. Every IoT device in your home will be able to communicate with Doory, and collaborate to create an eco-system that makes you feel better. Your smart TV could play a comedy when you are sad, your IoT tea-pot would start preparing a tea when you feel tired and your essential oil diffuser would spray some relaxing fragrance when someone made you angry.
 


