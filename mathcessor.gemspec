# coding: utf-8
lib = File.expand_path('../lib', __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require 'mathcessor/version'

Gem::Specification.new do |spec|
  spec.name          = "mathcessor"
  spec.version       = Mathcessor::VERSION
  spec.authors       = ["Morgan Laco"]
  spec.email         = ["morgan@codeschool.com"]
  spec.summary       = "Ridiculous mathy ways to access array elements!"
  spec.description   = "Ridiculous mathy ways to access array elements!"
  spec.homepage      = ""
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0")
  spec.executables   = spec.files.grep(%r{^bin/}) { |f| File.basename(f) }
  spec.test_files    = spec.files.grep(%r{^(test|spec|features)/})
  spec.require_paths = ["lib"]

  spec.add_development_dependency "bundler", "~> 1.7"
  spec.add_development_dependency "rake", "~> 10.0"
  spec.add_runtime_dependency "numbers_in_words", "0.2.0"
  spec.add_runtime_dependency "numbers_in_words/duck_punch"
end
