from sentence_transformers import SentenceTransformer
import scipy.spatial

embedder = SentenceTransformer('bert-base-nli-mean-tokens')
corpus = ['apple inc.', 'microsoft Corporation', 'honda', 'samsung electronics',  
          'bloomberg llc', 'toyota', 'google', 'facebook', 'amazon']
corpus_embeddings = embedder.encode(corpus)

queries = ['ipad pro', 'iphone 10 plus','iphone', 'kindle e-reader', 'android', 'accord ex', 'windows os', 'windows',
            'windows operating system',
           'camry le', 'galaxy s9', 'galaxy s8', 'civic', 'chromecast'
           ,'pixel phone', 'xbox one', 'fire tv']
query_embeddings = embedder.encode(queries)

closest_n = 1
for query, query_embedding in zip(queries, query_embeddings):
    distances = scipy.spatial.distance.cdist([query_embedding], corpus_embeddings, "cosine")[0]

    results = zip(range(len(distances)), distances)
    results = sorted(results, key=lambda x: x[1])
    
    print("======================")
    print("Query:", query)
    print("Result:")

    for idx, distance in results[0:closest_n]:
        result = corpus[idx].strip() + "(Score: %.4f)" % (1-distance) if 1-distance > 0.6 else 'Match not found.'
        print(result)
        
