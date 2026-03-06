https://transloadit.com/devtips/creating-a-free-image-cdn-with-cloudflare-r2/

- Includes rate-limiting
- Includes basic authentication
- They don't talk about cloudflare images resizing. However, i think they are using it. ~~this part i didn't quite get - it seems they are just creating a response with the body of the image and then a special `cf` argument.~~ **Yes, they are** These headers/arguments they use are using [transform via Workers](https://developers.cloudflare.com/images/transform-images/transform-via-workers/) functionality.
   ```javascript
    cf: {
      image: {
        fit: 'scale-down',
        width: width ? parseInt(width) : undefined,
        height: height ? parseInt(height) : undefined,
        quality: parseInt(quality),
        format,
      },
    },
    ```
- ~~what i don't fully get is that the access seems to to through the worker but they they also claim this is benefitting from r2 pricing structure of free unlimited bandwidth etc. but if it goes through the worker does it benefit from that??~~ Ans: (after a bit of reading) [`r2.Object.body`](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/#r2objectbody-definition) is a readable stream so when you return that in the response you are returning a readable stream to the underlying object in R2 🎉 so it *is* streaming from R2 🙌

```javascript
  ...
  const url = new URL(request.url)
  const path = url.pathname.slice(1)

  // Parse image transformation parameters
  const width = url.searchParams.get('w')
  const height = url.searchParams.get('h')
  const quality = url.searchParams.get('q') || '85'
  const format = url.searchParams.get('f') || 'auto'

  const object = await env.MY_BUCKET.get(path)

  if (!object) {
    return new Response('Image not found', { status: 404 })
  }

  const headers = new Headers()
  headers.set('Cache-Control', 'public, max-age=31536000')
  headers.set('Content-Type', object.httpMetadata.contentType || 'image/jpeg')

  return new Response(object.body, {
    headers,
    cf: {
      image: {
        fit: 'scale-down',
        width: width ? parseInt(width) : undefined,
        height: height ? parseInt(height) : undefined,
        quality: parseInt(quality),
        format,
      },
    },
  })
```