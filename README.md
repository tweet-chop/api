# Tweet Chop API

A simple webapp to chop your paragraphs into tweetable bites and get ready for that awesome tweetstorm you're about to bring onto the world!

This is where all the magic happens!

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

To run the code on your machine, you will need first to install:
- Python (> 3.2)

If you are on macOS X, you can install them using Homebrew:
```
brew install python3
```

You will also need to have `pipenv` on your machine:
```
pip install pipenv
```

> The latest the version, the better!

### Installing

Now that you have installed the needed software, let's look into getting this instance to run!

Run the following from the root of the project:
```
pipenv install
```

This will install all the dependencies for the server.

Finally, to kick things up, run the following:
```
pipenv shell
FLASK_APP=app.py FLASK_DEBUG=1 flask run
```

If there are no errors, then you are pretty much set!


## Running the tests

-- TODO --

## Deployment

-- TODO --

## Contributing

-- TODO --

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Tiphaine Viard** - *Initial work* - [TiphaineV](https://github.com/TiphaineV)
* **Antonio Villagra De La Cruz** - *Initial work* - [AntonioVdlC](https://github.com/AntonioVdlC)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

MIT

## Acknowledgments

* [Billie Thompson](https://github.com/PurpleBooth) for this [README.md template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) ... it's awesome!
