class HomesController < ApplicationController
  def index
    @homes = Home.all.includes(:images)
  end

  def show
    @home = Home.find(params[:id])
  end
end
