Rails.application.routes.draw do
  get 'images/show'

  resources :orders
  root 'homes#index'
  resources :homes
  resources :images
end
