# Beyerdynamic Custom One Pro switch position 4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.5; 25 -6.9; 28 -7.5; 31 -7.9; 34 -8.2; 37 -8.5; 41 -8.8; 45 -9.0; 49 -9.2; 54 -9.2; 60 -9.3; 66 -9.4; 72 -9.5; 79 -9.5; 87 -7.8; 96 -6.0; 106 -6.8; 116 -9.4; 128 -11.1; 141 -12.0; 155 -11.6; 170 -10.1; 187 -11.3; 206 -10.4; 227 -9.1; 249 -8.4; 274 -7.8; 302 -7.3; 332 -7.2; 365 -7.0; 402 -7.1; 442 -7.0; 486 -7.3; 535 -7.4; 588 -7.1; 647 -7.1; 712 -7.3; 783 -6.3; 861 -6.1; 947 -6.4; 1042 -6.4; 1146 -6.3; 1261 -6.6; 1387 -7.2; 1526 -8.0; 1678 -8.7; 1846 -9.0; 2031 -8.9; 2234 -8.1; 2457 -6.0; 2703 -4.1; 2973 -2.3; 3270 -1.5; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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
| Peaking | 52 Hz   | 1.46 | -2.8 dB |
| Peaking | 163 Hz  | 1.55 | -5.1 dB |
| Peaking | 1723 Hz | 3    | -2.9 dB |
| Peaking | 2143 Hz | 3.96 | -3.2 dB |
| Peaking | 4275 Hz | 1.07 | 7.0 dB  |
| Peaking | 78 Hz   | 4.15 | -2.0 dB |
| Peaking | 97 Hz   | 3.59 | 3.3 dB  |
| Peaking | 127 Hz  | 4.99 | -2.0 dB |
| Peaking | 6362 Hz | 3.26 | 4.6 dB  |
| Peaking | 7271 Hz | 1.48 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20Custom%20One%20Pro%20switch%20position%204/Beyerdynamic%20Custom%20One%20Pro%20switch%20position%204.png)