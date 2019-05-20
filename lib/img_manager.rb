require 'rmagick'

class ImgManager
  def self.crop(name, x, y, width, height, cate)
    # path = Rails.root.join('app', 'assets', 'images', name)
    # img = Magick::Image.read(path)[0]

    # chopped = img.crop(x.to_i, y.to_i, width.to_i, height.to_i)
    # timestamp = Time.now.to_i.to_s
    # save_path = Rails.root.join('public', "#{Time.now.to_i.to_s}.jpg")
    # chopped.write(save_path)

    # Search file
    # binding.pry

    # file = save_path.to_s.split('/')[-1]
    # `"cd python && python3 query.py ../public/#{file} #{cate}"`
    # a = `python3 python/query.py #{save_path} cate`
    sleep(3)
    return
  end
end
