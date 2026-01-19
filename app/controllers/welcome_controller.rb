class WelcomeController < ApplicationController
  def index
    @proyectos = Proyecto.all # Esto trae todo de PostgreSQL
  end
end
