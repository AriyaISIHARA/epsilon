# epsilon

Computes neighbor representable float in python.

## Note

Works only in python implementations where `float` is IEEE754 64-bit float.

## Functions

### next_float64

`next_float64(f)` computes the next representable float.

Given a 64-bit float `f`, returns the minimal representable float that is greater than `f`.

Irregulars:

    - `inf` => `nan`
    
    - `float.max` => `inf`
    
    - `-inf` => `-float.max`
    
    - `nan` => `nan`

### previous_float64

`previous_float64(f)` computes the previous representable float.

Given a 64-bit float `f`, returns the maximal representable float that is smaller then `f`.

Irregulars:

    - `-inf` => `nan`
    
    - `-float.max` => `-inf`
    
    - `inf` => `float.max`
    
    - `nan` => `nan`

## Installation

is not recommended.

## Usage

Copy, Paste, and Call.

## Author

[Ariya ISIHARA](https://github.com/AriyaISIHARA)
