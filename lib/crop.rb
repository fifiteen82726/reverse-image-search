require 'rmagick'

class Crop
  def self.hihi
    p 'hihi'
    path = Rails.root.join('app', 'assets', 'images', 'paris', 'louvre')
    path += 'paris_louvre_000008.jpg'
    img = Magick::Image.read(path)[0]

    chopped = img.crop(0, 0, 107, 139)
    chopped.write('python/new.jpg')

    `python python/feature-extraction.py`
  end
end
