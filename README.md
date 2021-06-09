# A pure numpy implementation of citipy


<div align="center">
    <h2 style="font-color: pink">Find cities with <b>math</b>, not packages!</h2>
</div>

The code necessary for completing the singular task the original package accomplishes
is quite succinct, so I removed the unnecessary dependancy `kdtree`.

We wish to find the nearest city to a given a latitude-longitude pair,
which for the sake of utter nonsense we will call c, such that

<img 
src="https://latex.codecogs.com/gif.latex?c := (x_{\text{lat}}, x_{\text{lon}}) \in S \subset \mathbf{R}^2" 
/> 

Where S is the subset of real number pairs defined by

<img 
src="https://latex.codecogs.com/gif.latex?\forall c \in S: (x_{\text{lat}} \in [-180,180]) \wedge (x_{\text{lon}} \in [-90, 90])"
/> 

Now, contained in this package is a CSV of world cities and their coordinates.

We seek to find the city in our list of cities that minimizes the euclidean distance
between $_{\text{nearest}} and our defined coordinate pair, which we call c_i

I've grown tired of writing LaTeX. But you get the idea.

You can load csv data with numpy using the `np.genfromtxt` function.
The python code is as follows:

```python

lats = # numpy array of latitudes
lons = # numpy array of longitudes
names = # List of city names

def nearest_city(lat, lon, field="city"):
    
    # Shout out to big daddy pythagoras
    distances = np.sqrt((lats - lat) ** 2 + (lons - lon) ** 2)

    # Find the index of the minimum value
    index = distances.argmin()

    # Return the name at that index
    return names[index]
```

Now, while I promised a **pure numpy** implementation, my code uses pandas.

That can easily be fixed with the `np.genfromtxt` function, but that exercise is left to the reader.


##### Original README

---

Looking up for city names with geo-coordinates has always been a big problem when it comes to dealing with social data.

I hate going through web endpoints to look for the city names; we are often rate-limited and it's also such a waste.

We have only this many cities in the world, why isn't there any data set that provides the geo coordinates for all the

available cities, and we can use certain data structure/algorithm like kdtree to look up the nearest city given a set of geo coordinates?

Luckily, both Maxmind(www.maxmind.com/en/free-world-cities-database) and GeoNames(download.geonames.org/export/dump)

provide comprehensive data sets like this.

I then chose Maxmind because I think it's better. GeoNames lacks of many US cities.

# Example

## Installation

```
pip install citipy
```

## Looking up with coordinates

```
>>> from citipy import citipy
>>> city = citipy.nearest_city(22.99, 120.21)
>>> city
<citipy.City instance at 0x1069b6518>
>>>
>>> city.city_name     # Tainan, my home town
'tainan'
>>>
>>> city.country_code
'tw'                  # And the country is surely Taiwan
```

# World Cities Data Set

I use Maxmind's Free World Cities Database. You can get it here: https://www.maxmind.com/en/free-world-cities-database .

Please note that I only count in the cities whose population is over 500, otherwise the results are too noisy for me.

# Contribution

Just send me a PR. It's nice and easy :)

# License

MIT
