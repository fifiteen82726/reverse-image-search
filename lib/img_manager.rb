require 'rmagick'

class ImgManager
  def self.crop
    path = Rails.root.join('app', 'assets', 'images', 'paris', 'louvre')
    path += 'paris_louvre_000022.jpg'
    img = Magick::Image.read(path)[0]

    chopped = img.crop(311, 270, 369, 226)
    timestamp = Time.now.to_i.to_s
    name = "python/img/#{Time.now.to_i.to_s}.jpg"
    chopped.write(name)

    `python python/feature-extraction.py #{timestamp}`
  end
end
