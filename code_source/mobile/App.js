import React, { Component } from 'react';
import { StyleSheet, Button, Text, View, Alert } from 'react-native';
import Svg, { Circle, Line } from 'react-native-svg';

// Adresse de base pour les requêtes vers le serveur
const baseURL = 'http://192.168.1.172:1665';

export default class App extends Component {
  state = {
    donneesJson: {
      snirium: '',
      angle: '',
      moteur_gauche: '',
      moteur_droite: '',
      distance: '',
    },
  };

  // Fonction pour récupérer les valeurs du robot depuis le serveur
  _onPressRecuperer = () => {
    fetch(`${baseURL}/?`, {
      method: 'GET',
    })
      .then((response) => response.json())
      .then((responseJson) => {
        console.log(responseJson);
        this.setState({
          donneesJson: responseJson,
        });
      })
      .catch((error) => {
        console.error(error);
      });
  };

  // Fonction générique pour envoyer des commandes au robot
  _sendCommand = (command) => {
    fetch(`${baseURL}/${command}`, {
      method: 'GET',
    });
  };

  // Fonctions spécifiques pour chaque commande
  _onPressAvancer = () => this._sendCommand('A');
  _onPressReculer = () => this._sendCommand('R');
  _onPressTourner = () => this._sendCommand('T');
  _onPressGauche = () => this._sendCommand('G');
  _onPressDroite = () => this._sendCommand('D');
  _onPressLeverBarre = () => this._sendCommand('X');
  _onPressBaisserBarre = () => this._sendCommand('Y');
  _onPressStop = () => this._sendCommand('S');

  render() {
    // Déstructuration des valeurs nécessaires du state
    const { distance, angle } = this.state.donneesJson;
    const radius = 10;
    const centerX = 100;
    const centerY = 100;

    // Calcul des coordonnées de l'obstacle en fonction de la distance et de l'angle
    const angleRadian = (angle * Math.PI) / 180;
    const dx = distance * Math.cos(angleRadian);
    const dy = distance * Math.sin(angleRadian);
    const obstacleX = centerX + dx;
    const obstacleY = centerY + dy;

    return (
      <View style={styles.page}>
        {/* Bouton pour récupérer les valeurs */}
        <View style={styles.buttonContainer}>
          <Button
            onPress={this._onPressRecuperer}
            title="Récupérer les valeurs"
            color="white"
            style={styles.button}
          />
        </View>

        {/* Boutons pour les commandes */}
        <View style={styles.arrowButtonsContainer}>
          <Button onPress={this._onPressAvancer} title="↑" color="white" style={styles.arrowButton} />
          <Button onPress={this._onPressDroite} title="→" color="white" style={styles.arrowButton} />
          <Button onPress={this._onPressGauche} title="←" color="white" style={styles.arrowButton} />
          <Button onPress={this._onPressReculer} title="↓" color="white" style={styles.arrowButton} />
        </View>

        <View style={styles.buttonContainer}>
          {/* Boutons supplémentaires */}
          <Button onPress={this._onPressTourner} title="Tourner" color="white" style={styles.arrowButton} />
          <Button onPress={this._onPressLeverBarre} title="Lever" color="white" style={styles.arrowButton} />
          <Button onPress={this._onPressStop} title="Stop" color="white" style={styles.button} />
          <Button onPress={this._onPressBaisserBarre} title="Baisser" color="white" style={styles.arrowButton} />
        </View>

        {/* Affichage des valeurs */}
        <Text>Sinirium: {this.state.donneesJson.snirium}</Text>
        <Text>Angle: {this.state.donneesJson.angle}</Text>
        <Text>Moteur Gauche: {this.state.donneesJson.moteur_gauche}</Text>
        <Text>Moteur Droite: {this.state.donneesJson.moteur_droite}</Text>
        <Text>Distance: {this.state.donneesJson.distance}</Text>

        {/* Affichage du robot et de la ligne avec l'obstacle */}
        <Svg height="200" width="200">
          <Circle
            cx="100"
            cy="100"
            r={radius}
            fill={`rgb(${this.state.donneesJson.snirium * 2.5}, 0, 0)`}
            strokeWidth={5}
            stroke="white"
          />
          <Line x1={centerX} y1={centerY} x2={obstacleX + distance / 10} y2={obstacleY + distance / 10} strokeWidth={5} stroke="white" />
        </Svg>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  page: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#663300', // Light Coral
  },
  buttonContainer: {
    marginVertical: 10,
  },
  button: {
    backgroundColor: '#663300', // Indian Red
  },
  arrowButtonsContainer: {
    flexDirection: 'row',
    marginVertical: 10,
  },
  arrowButton: {
    flex: 1,
    marginHorizontal: 5,
    backgroundColor: '#663300', // Indian Red
  },
});
