class ImagesController < ApplicationController
  def show
    @image = Image.find(params[:id])
  end

  def search
    info = params['info']
    cate = info['img'].split('/')[0]
    ImgManager.crop(info['img'], info['x'], info['y'], info['width'], info['height'], cate)
    return
  end

  def show_search
  end
end
