# Ultrasone Edition 8 Palladium
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.6; 23 -9.2; 25 -9.8; 28 -10.4; 31 -11.0; 34 -11.4; 37 -11.8; 41 -12.1; 45 -12.3; 49 -12.2; 54 -11.7; 60 -10.6; 66 -10.1; 72 -10.8; 79 -11.9; 87 -12.5; 96 -12.3; 106 -11.7; 116 -10.7; 128 -9.5; 141 -8.1; 155 -6.4; 170 -4.4; 187 -2.5; 206 -1.0; 227 -0.5; 249 -1.2; 274 -2.6; 302 -4.0; 332 -4.7; 365 -5.1; 402 -5.1; 442 -5.1; 486 -5.3; 535 -5.4; 588 -5.4; 647 -5.6; 712 -5.7; 783 -6.0; 861 -6.3; 947 -6.4; 1042 -6.7; 1146 -6.7; 1261 -7.0; 1387 -6.9; 1526 -6.3; 1678 -5.4; 1846 -4.5; 2031 -3.0; 2234 -0.7; 2457 -1.4; 2703 -4.3; 2973 -5.7; 3270 -5.7; 3597 -6.3; 3957 -7.0; 4353 -7.0; 4788 -8.4; 5267 -11.1; 5793 -13.5; 6373 -15.4; 7010 -14.9; 7711 -11.4; 8482 -6.9; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Edition 8 Palladium GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Edition 8 Palladium ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 39 Hz   | 0.97 | -5.5 dB  |
| Peaking | 101 Hz  | 1.34 | -5.8 dB  |
| Peaking | 219 Hz  | 1.75 | 7.0 dB   |
| Peaking | 2302 Hz | 4.04 | 6.2 dB   |
| Peaking | 6447 Hz | 2.8  | -10.3 dB |
| Peaking | 587 Hz  | 2.15 | 0.6 dB   |
| Peaking | 1360 Hz | 1.68 | -1.4 dB  |
| Peaking | 1767 Hz | 2.5  | 1.0 dB   |
| Peaking | 7518 Hz | 5.63 | -2.9 dB  |
| Peaking | 8678 Hz | 2.43 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | 6.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB |
| Peaking | 8000 Hz  | 1.41 | -5.2 dB |
| Peaking | 16000 Hz | 1.41 | 1.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ultrasone%20Edition%208%20Palladium/Ultrasone%20Edition%208%20Palladium.png)