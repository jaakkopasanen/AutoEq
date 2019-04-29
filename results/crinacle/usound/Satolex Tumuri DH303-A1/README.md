# Satolex Tumuri DH303-A1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.6; 28 -2.3; 31 -2.8; 34 -3.3; 37 -3.7; 41 -4.1; 45 -4.6; 49 -4.9; 54 -5.3; 60 -5.8; 66 -6.2; 72 -6.6; 79 -7.1; 87 -7.5; 96 -8.0; 106 -8.4; 116 -8.7; 128 -9.0; 141 -9.3; 155 -9.4; 170 -9.5; 187 -9.5; 206 -9.4; 227 -9.2; 249 -9.0; 274 -8.7; 302 -8.3; 332 -8.0; 365 -7.5; 402 -7.0; 442 -6.6; 486 -6.1; 535 -5.5; 588 -4.9; 647 -4.3; 712 -3.6; 783 -2.8; 861 -2.3; 947 -1.8; 1042 -1.7; 1146 -2.7; 1261 -4.1; 1387 -4.5; 1526 -4.5; 1678 -4.1; 1846 -3.8; 2031 -3.8; 2234 -4.2; 2457 -5.2; 2703 -6.4; 2973 -7.0; 3270 -6.1; 3597 -4.5; 3957 -3.2; 4353 -2.7; 4788 -3.2; 5267 -5.2; 5793 -9.2; 6373 -9.7; 7010 -6.0; 7711 -5.7; 8482 -6.5; 9330 -6.4; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -7.1; 16529 -8.3; 18182 -6.2; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Satolex Tumuri DH303-A1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Satolex Tumuri DH303-A1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.46 | 6.7 dB  |
| Peaking | 174 Hz   | 0.54 | -3.9 dB |
| Peaking | 928 Hz   | 1.12 | 4.4 dB  |
| Peaking | 4471 Hz  | 3.36 | 3.8 dB  |
| Peaking | 6019 Hz  | 6.25 | -5.5 dB |
| Peaking | 1380 Hz  | 3.57 | -1.6 dB |
| Peaking | 2253 Hz  | 1.17 | 2.0 dB  |
| Peaking | 2855 Hz  | 3.28 | -3.2 dB |
| Peaking | 7373 Hz  | 6.04 | 0.5 dB  |
| Peaking | 16237 Hz | 2.89 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Satolex%20Tumuri%20DH303-A1/Satolex%20Tumuri%20DH303-A1.png)