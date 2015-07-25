# Mathcessor

Ridiculous mathy methods for array element retrieval!

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'mathcessor'
```

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install mathcessor

## Usage

```ruby
class Goo
  using Mathcessor
  def your_awesome_method
    p ['kitties',
      'puppies',
      'piggies',
      'cowwies',
      'donkies',
      'sheepies',
      'chickies',
      'bears'].square_root_of_thirty_six
  end
end
Goo.new.your_awesome_method # => 'chickies'

animals = ['kitties', 'puppies', 'piggies', 'cowwies', 'donkies', 'sheepies', 'chickies', 'bears']

# Square root
animals.square_root_of_thirty_six # => 'chickies'

# Cube root
animals.cube_root_of_twenty_seven # => 'cowwies'
```

## Contributing

1. Fork it ( https://github.com/mlaco/mathcessor/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
