# Beyerdynamic Custom One Pro switch position 4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.4; 25 -7.8; 28 -8.4; 31 -8.8; 34 -9.1; 37 -9.4; 41 -9.7; 45 -9.9; 49 -10.1; 54 -10.1; 60 -10.2; 66 -10.3; 72 -10.4; 79 -10.4; 87 -8.7; 96 -6.9; 106 -7.7; 116 -10.3; 128 -12.1; 141 -12.9; 155 -12.5; 170 -11.0; 187 -12.2; 206 -11.3; 227 -10.0; 249 -9.3; 274 -8.7; 302 -8.2; 332 -8.1; 365 -7.9; 402 -8.0; 442 -7.9; 486 -8.2; 535 -8.3; 588 -8.0; 647 -8.0; 712 -8.2; 783 -7.2; 861 -7.1; 947 -7.3; 1042 -7.3; 1146 -7.3; 1261 -7.5; 1387 -8.1; 1526 -8.9; 1678 -9.7; 1846 -9.9; 2031 -9.8; 2234 -9.0; 2457 -6.9; 2703 -5.0; 2973 -3.3; 3270 -2.4; 3597 -1.4; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Custom One Pro switch position 4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Custom One Pro switch position 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 1.12 | -3.7 dB |
| Peaking | 164 Hz  | 1.42 | -5.7 dB |
| Peaking | 562 Hz  | 1.36 | -1.4 dB |
| Peaking | 1924 Hz | 1.94 | -5.1 dB |
| Peaking | 4385 Hz | 1.14 | 7.1 dB  |
| Peaking | 76 Hz   | 3.96 | -2.0 dB |
| Peaking | 97 Hz   | 3.51 | 3.3 dB  |
| Peaking | 126 Hz  | 5.02 | -2.0 dB |
| Peaking | 6357 Hz | 3.46 | 4.3 dB  |
| Peaking | 7355 Hz | 1.53 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20Custom%20One%20Pro%20switch%20position%204/Beyerdynamic%20Custom%20One%20Pro%20switch%20position%204.png)