require "mathcessor/version"
require "numbers_in_words"
require "numbers_in_words/duck_punch"

module Mathcessor
  refine Array do
    def method_missing(method, *args, &block)
      method = method.to_s
      match = /(square_root_of_((?:[a-z]+_)+[a-z]+))/.match(method)
      if match[1] == method && method.start_with?("square_root_of_")
        radicand = match[2].in_numbers
        sqrt = Math.sqrt(radicand).to_i
        self[sqrt-1]
      else
        puts "nope"
      end
    end
  end
end
