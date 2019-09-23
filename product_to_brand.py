from sentence_transformers import SentenceTransformer
import scipy.spatial

embedder = SentenceTransformer('bert-base-nli-mean-tokens')
brand = ['apple inc.', 'microsoft Corporation', 'honda', 'samsung electronics',  
          'bloomberg llc', 'toyota', 'google', 'facebook', 'amazon']
brand_embeddings = embedder.encode(brand)

product = ['ipad pro', 'iphone 10 plus','iphone', 'kindle e-reader', 'android', 'accord ex', 'windows os', 'windows',
            'windows operating system',
           'camry le', 'galaxy s9', 'galaxy s8', 'civic', 'chromecast'
           ,'pixel phone', 'xbox one', 'fire tv']
product_embeddings = embedder.encode(product)

closest_n = 1
for product, product_embedding in zip(product, product_embeddings):
    distances = scipy.spatial.distance.cdist([product_embedding], brand_embeddings, "cosine")[0]

    results = zip(range(len(distances)), distances)
    results = sorted(results, key=lambda x: x[1])
    
    print("======================")
    print("Query:", product)
    print("Result:")

    for idx, distance in results[0:closest_n]:
        result = brand[idx].strip() + "(Score: %.4f)" % (1-distance) if 1-distance > 0.6 else 'Match not found.'
        print(result)
        
