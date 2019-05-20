Rails.application.routes.draw do
  get 'images/show'

  resources :orders
  root 'homes#index'
  resources :homes
  resources :images
  post 'images-search' => 'images#search'
  get 'show-search' => 'images#show_search'
end
