require "mathcessor/version"
require "numbers_in_words"
require "numbers_in_words/duck_punch"

module Mathcessor
  METHOD_FAMILIES = {square_root_of_: Proc.new {|q| Math.sqrt(q).to_i}}
  refine Array do
    def method_missing(method, *args, &block)
      method = method.to_s
      METHOD_FAMILIES.each do |family_symbol, fun|
        family = family_symbol.to_s
        regex = /(#{Regexp.quote(family)}((?:[a-z]+_)+[a-z]+))/
        match = regex.match(method)
        if match[1] == method && method.start_with?(family)
          argument = match[2].in_numbers
          result = fun.call(argument)
          return self[result]
        else
          puts "nope"
        end
      end
    end
  end
end
