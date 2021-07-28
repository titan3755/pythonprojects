#include <iostream>
#include "../weed/External/include/SFML/Graphics.hpp"
#include "../weed/External/include/SFML/System.hpp"
#include "../weed/External/include/SFML/Window.hpp"
#include "../weed/External/include/SFML/Audio.hpp"
#include "../weed/External/include/SFML/Network.hpp"

int main() {
	sf::RenderWindow MainWindowObj(sf::VideoMode(700, 400), "Gaymer", sf::Style::Titlebar | sf::Style::Close);
	sf::Event MainEvent;
	while (MainWindowObj.isOpen()) {
		while (MainWindowObj.pollEvent(MainEvent)) {

			switch (MainEvent.type) {
			case sf::Event::Closed:
				MainWindowObj.close();

			case sf::Event::KeyPressed:
				if (MainEvent.key.code == sf::Keyboard::Escape) {
					break;
				}
			}

		}
		MainWindowObj.clear(sf::Color(0, 0, 255));

		MainWindowObj.display();
	}



	return 0;
}