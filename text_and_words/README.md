# Basic of nlkt

## Installation

Install with line below

```
$pip install -U nltk
```

start python prompt with `python` and import nltk

```python
>>> import nltk
```

## Sample Data

Download book data

```python
>>> nltk.download()
```

this will open GUI on macOS, select `book` and download
import book data

```python
>>> from nltk.book import *
```


## Search text

#### Concordance: search text with words around it

```python
>>> text1.concordance("monstrous")
```

#### Similar: search for all similar words

```python
>>> text1.similar("monstrous")
```

#### Common Contexts: search words with same usage contexts

```python
>>> text2.common_contexts(["monstrous", "very"])
```

### Dispersion Plot: word usage in plot graph

numpy and matplotlib required

```python
>>> text4.dispersion_plot(["citizens", "freedom", "war", "terrorist", "love", "America"])
```
