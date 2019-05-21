class ImagesController < ApplicationController
  def show
    @image = Image.find(params[:id])
  end

  def search
    info = params['info']
    cate = info['img'].split('/')[0]

    info = ImgManager.crop(info['img'], info['x'], info['y'], info['width'], info['height'], cate)

    session[:target] = info[:target]
    session[:urls] = info[:urls]

    redirect_to show_search_path
  end

  def show_search
    @target = session[:target]
    @urls = session[:urls]
  end
end
