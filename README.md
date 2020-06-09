# `load-test-template`

This project gives you minimal resources necessary to begin conducting load tests
with no dependencies on your systems besides docker.

# Getting Setup

1. setup your urls

  You can either update the example urls.csv in the root of the repo or the URLS
  list in the provided locustfile.

2. set your host

  In the locustfile, you'll notice a HOST variable- set that to the host of the paths
  you're testing. (e.g. https://example.org) No trailing slash please.

3. update the request action methods as appropriate

  See the [locust docs](https://docs.locust.io/en/stable/writing-a-locustfile.html) for
  all the available options. The provided example sends 90% of requests to a random url
  from one url list and 10% to another.


# Running

To run, you can use the following:

`docker run -p 8000:8089 -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/locustfile.py`

With this, the locust service runs on port 8089 inside the container and 8000 on the host.

To start a load test, visit the UI at http://localhost:8000 and click start!


# Guarantees of Liability

Absolutely none. You're on your own. Be responsible. And do not use against a system
not your own.
