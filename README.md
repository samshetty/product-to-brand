# Indentify Entity relationships between products and companies

Used 
Google's [BERT](https://github.com/google-research/bert) embeddings. And [sentence-transformers](https://github.com/UKPLab/sentence-transformers) in the interest of time.

This python program uses BERT embeddings to indentify entity relationships between products and companies. It only shows matches where the score (based on cosine distance) is more than 0.6. As evidenced by the result, the more detailed the product and company name, the better the results.

Below are the input and output for a sample test:

'''
   
      Input:

      companies = ['apple inc.', 'microsoft Corporation', 'honda', 'samsung electronics', 'bloomberg llc', 
      'toyota', 'google', 'facebook', 'amazon']

      products = ['ipad pro', 'iphone 10 plus','iphone', 'kindle e-reader', 'android', 'accord ex', 
      'windows os', 'windows', 'windows operating system', 'camry le', 'galaxy s9', 'galaxy s8', 
      'civic', 'chromecast','pixel phone', 'xbox one', 'fire tv']

      Output: 
      ======================
      Query: ipad pro
      Result:
      apple inc.(Score: 0.7191)
      ======================
      Query: iphone 10 plus
      
      Result:
      apple inc.(Score: 0.7391)
      ======================
      Query: iphone
      Result:
      samsung electronics(Score: 0.7408)
      ======================
      Query: kindle e-reader
      Result:
      amazon(Score: 0.6436)
      ======================
      Query: android
      Result:
      google(Score: 0.7069)
      ======================
      Query: accord ex
      Result:
      honda(Score: 0.6285)
      ======================
      Query: windows os
      Result:
      microsoft Corporation(Score: 0.7815)
      ======================
      Query: windows
      Result:
      Match not found.
      ======================
      Query: windows operating system
      Result:
      microsoft Corporation(Score: 0.8030)
      ======================
      Query: camry le
      Result:
      toyota(Score: 0.7250)
      ======================
      Query: galaxy s9
      Result:
      samsung electronics(Score: 0.6126)
      ======================
      Query: galaxy s8
      Result:
      samsung electronics(Score: 0.6205)
      ======================
      Query: civic
      Result:
      honda(Score: 0.6588)
      ======================
      Query: chromecast
      Result:
      google(Score: 0.6650)
      ======================
      Query: pixel phone
      Result:
      google(Score: 0.7043)
      ======================
      Query: xbox one
      Result:
      microsoft Corporation(Score: 0.6485)
      ======================
      Query: fire tv
      Result:
      Match not found.
'''

## Getting Started

### Steps to execute

1. Download repo to a local folder

2. Install Prerequisites

   ```
   pip install -r requirements.txt
   ```
   
3. Run [product_to_brand.py](https://github.com/samshetty/product-to-brand/blob/master/product_to_brand.py)

   ```
   python product_to_brand.py
   ```
  
## Author

* **Sam Shetty** 
