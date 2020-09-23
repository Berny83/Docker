Rails.application.routes.draw do
	get 'posts/index'
	root 'posts#index', as: 'home'
	
	get 'about' => 'pages#about', as: 'about'
	resources :posts do
		resources :comments
	end
end
