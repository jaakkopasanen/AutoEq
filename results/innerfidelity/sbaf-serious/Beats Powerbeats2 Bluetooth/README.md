# Beats Powerbeats2 Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -6.9; 25 -7.0; 28 -7.1; 31 -7.2; 34 -7.3; 37 -7.4; 41 -7.6; 45 -7.7; 49 -7.8; 54 -7.9; 60 -8.0; 66 -8.2; 72 -8.4; 79 -8.7; 87 -9.1; 96 -9.4; 106 -9.7; 116 -9.8; 128 -10.1; 141 -10.4; 155 -10.6; 170 -10.5; 187 -10.6; 206 -10.7; 227 -10.5; 249 -10.5; 274 -10.3; 302 -10.2; 332 -10.0; 365 -9.7; 402 -9.5; 442 -9.1; 486 -9.0; 535 -8.5; 588 -7.9; 647 -7.5; 712 -7.2; 783 -6.6; 861 -6.4; 947 -6.2; 1042 -6.2; 1146 -6.0; 1261 -5.8; 1387 -5.9; 1526 -5.9; 1678 -5.9; 1846 -5.5; 2031 -4.9; 2234 -4.0; 2457 -2.5; 2703 -1.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.4; 4788 -2.9; 5267 -2.9; 5793 -2.9; 6373 -4.0; 7010 -5.8; 7711 -7.7; 8482 -8.7; 9330 -7.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -9.2; 16529 -10.1; 18182 -9.5; 20000 -10.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Powerbeats2 Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Powerbeats2 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 133 Hz   | 0.57 | -2.8 dB |
| Peaking | 303 Hz   | 0.73 | -2.5 dB |
| Peaking | 3756 Hz  | 0.95 | 7.3 dB  |
| Peaking | 12661 Hz | 1.59 | 4.1 dB  |
| Peaking | 15489 Hz | 0.26 | -4.4 dB |
| Peaking | 1892 Hz  | 3.11 | -1.1 dB |
| Peaking | 2743 Hz  | 5.57 | 1.4 dB  |
| Peaking | 4862 Hz  | 2.98 | -2.1 dB |
| Peaking | 5743 Hz  | 2.08 | 2.4 dB  |
| Peaking | 8162 Hz  | 4.68 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -3.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Powerbeats2%20Bluetooth/Beats%20Powerbeats2%20Bluetooth.png)