# Beyerdynamic Custom One Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.1; 23 -11.2; 25 -11.2; 28 -11.2; 31 -11.1; 34 -10.8; 37 -10.4; 41 -9.6; 45 -8.5; 49 -7.1; 54 -5.4; 60 -4.1; 66 -4.0; 72 -4.2; 79 -4.7; 87 -5.8; 96 -7.5; 106 -8.6; 116 -8.6; 128 -7.5; 141 -5.3; 155 -3.3; 170 -2.4; 187 -2.5; 206 -3.0; 227 -3.4; 249 -3.7; 274 -3.7; 302 -3.7; 332 -3.5; 365 -3.3; 402 -3.1; 442 -2.9; 486 -2.5; 535 -2.3; 588 -2.1; 647 -2.1; 712 -1.8; 783 -1.4; 861 -1.1; 947 -1.0; 1042 -0.8; 1146 -0.6; 1261 -0.5; 1387 -0.8; 1526 -1.1; 1678 -1.8; 1846 -2.9; 2031 -4.5; 2234 -6.3; 2457 -7.2; 2703 -7.0; 2973 -6.4; 3270 -6.1; 3597 -5.8; 3957 -5.1; 4353 -3.5; 4788 -1.4; 5267 -3.8; 5793 -8.7; 6373 -10.2; 7010 -7.3; 7711 -3.3; 8482 -3.5; 9330 -3.6; 10263 -3.6; 11289 -3.6; 12418 -3.6; 13660 -3.6; 15026 -3.6; 16529 -3.6; 18182 -3.6; 20000 -3.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Custom One Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Custom One Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 27 Hz   | 1.14 | -8.7 dB  |
| Peaking | 111 Hz  | 3.72 | -5.4 dB  |
| Peaking | 2224 Hz | 0.44 | 6.9 dB   |
| Peaking | 2629 Hz | 1.18 | -10.6 dB |
| Peaking | 6306 Hz | 4.46 | -8.8 dB  |
| Peaking | 25 Hz   | 1.18 | -1.9 dB  |
| Peaking | 26 Hz   | 3.49 | 2.7 dB   |
| Peaking | 176 Hz  | 5.68 | 1.9 dB   |
| Peaking | 4655 Hz | 2.24 | -2.5 dB  |
| Peaking | 4811 Hz | 5.57 | 5.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.3 dB |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20Custom%20One%20Pro/Beyerdynamic%20Custom%20One%20Pro.png)