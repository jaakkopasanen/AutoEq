# Satolex Tubomi DH302-A1Bs
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.9; 25 -5.4; 28 -6.0; 31 -6.5; 34 -6.9; 37 -7.3; 41 -7.7; 45 -8.1; 49 -8.4; 54 -8.7; 60 -9.1; 66 -9.4; 72 -9.7; 79 -10.1; 87 -10.4; 96 -10.7; 106 -10.8; 116 -11.0; 128 -11.0; 141 -11.0; 155 -11.2; 170 -11.1; 187 -11.0; 206 -10.6; 227 -10.2; 249 -9.8; 274 -9.2; 302 -8.7; 332 -8.2; 365 -7.5; 402 -6.9; 442 -6.3; 486 -5.7; 535 -5.0; 588 -4.3; 647 -3.6; 712 -2.8; 783 -2.0; 861 -1.2; 947 -0.6; 1042 -0.5; 1146 -0.9; 1261 -1.3; 1387 -1.6; 1526 -1.4; 1678 -1.0; 1846 -0.7; 2031 -0.9; 2234 -2.4; 2457 -4.1; 2703 -4.4; 2973 -4.3; 3270 -3.7; 3597 -2.5; 3957 -1.6; 4353 -2.0; 4788 -3.5; 5267 -6.9; 5793 -7.0; 6373 -2.6; 7010 -2.5; 7711 -4.7; 8482 -4.9; 9330 -5.0; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -5.6; 16529 -6.2; 18182 -5.6; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Satolex Tubomi DH302-A1Bs GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Satolex Tubomi DH302-A1Bs ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 62 Hz    | 0.92 | -1.2 dB |
| Peaking | 165 Hz   | 0.42 | -6.2 dB |
| Peaking | 1013 Hz  | 0.68 | 4.9 dB  |
| Peaking | 1920 Hz  | 4.28 | 2.0 dB  |
| Peaking | 6764 Hz  | 9.35 | 3.5 dB  |
| Peaking | 19 Hz    | 2.39 | 1.5 dB  |
| Peaking | 2869 Hz  | 2.57 | -2.0 dB |
| Peaking | 4132 Hz  | 1.9  | 3.5 dB  |
| Peaking | 5500 Hz  | 5.97 | -4.9 dB |
| Peaking | 16543 Hz | 1.8  | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Satolex%20Tubomi%20DH302-A1Bs/Satolex%20Tubomi%20DH302-A1Bs.png)