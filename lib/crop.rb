require 'rmagick'

class Crop
  def self.hihi
    p 'hihi'
    path = Rails.root.join('app', 'assets', 'images', 'paris', 'louvre')
    path += 'paris_louvre_000008.jpg'
    img = Magick::Image.read(path)[0]

    chopped = img.crop(0, 0, 107, 139)
    timestamp = Time.now.to_i.to_s
    name = "python/img/#{Time.now.to_i.to_s}.jpg"
    chopped.write(name)

    `python python/feature-extraction.py #{timestamp}`
  end
end
