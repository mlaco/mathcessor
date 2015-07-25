require "mathcessor/version"
require "numbers_in_words"
require "numbers_in_words/duck_punch"

module Mathcessor
  METHOD_FAMILIES = {
    square_root_of: Proc.new {|q| Math.sqrt(q).to_i},
    cube_root_of:   Proc.new {|q| (q ** (1.0/3)).to_i},
    factorial:      Proc.new {|q| ((1..q).inject(:*)).to_i}
  }
  refine Array do
    def method_missing(method, *args, &block)
      method = method.to_s
      METHOD_FAMILIES.each do |family_symbol, fun|
        family = "#{family_symbol.to_s}_"
        regex = /(#{Regexp.quote(family)}((?:[a-z]+_)*[a-z]+))/
        match = regex.match(method)
        if match && match[1] == method && method.start_with?(family)
          argument = match[2].in_numbers
          result = fun.call(argument)
          return self[result]
        end
      end
      false
    end
  end
end
