# Python Package Example

This is a example for pythton projects.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project.

### Prerequisites

- git
- make
- python 3.7
- pip
- virtualenv
- vscode

### Installing

First of all you need to clone this repository:

``` bash
git clone https://github.com/claick-oliveira/python-package-example.git
```

After clone access the folder and create your virtual env:

``` bash
cd python-package-example
make venv
```

Now let's activate your virtual env:

``` bash
make activate
```

To start to code you need to install the requirements and de dev requirements:

``` bash
make requirements
make requirementsdev
```

## Running the tests

To run the tests you need to execute:

``` bash
make test
```

### Break down into end to end tests

This is a simple test which checks the return from function main:

#### Package

``` python
def main():
    msg = 'Python package example!'
    print(msg)
    return(msg)


if __name__ == '__main__':
    main()
```

#### Test

``` python
import python_package.package as package


def test_main():
    msg = package.main()
    right_msg = 'Python package example!'
    assert msg == right_msg, 'This is a dummy test!'
```

### And coding style tests

In this project we'll use [PEP 8](https://www.python.org/dev/peps/pep-0008/) as style guide.

## Clean

To clean the files generated as coverage, builds, env you can use:

``` bash
make clean
```

If you prefer to clear all, use:

```bash
make cleanfull
```

## Contributing

Please read [CONTRIBUTING.md](https://github.com/claick-oliveira/python-package-example/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- **Claick Oliveira** - *Initial work* - [claick-oliveira](https://github.com/claick-oliveira)

See also the list of [contributors](https://github.com/claick-oliveira/python-package-example/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
