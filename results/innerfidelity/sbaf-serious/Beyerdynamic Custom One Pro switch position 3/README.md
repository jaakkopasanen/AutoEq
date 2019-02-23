# Beyerdynamic Custom One Pro switch position 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -7.3; 25 -7.7; 28 -8.3; 31 -8.7; 34 -9.0; 37 -9.2; 41 -9.4; 45 -9.6; 49 -9.6; 54 -9.2; 60 -8.7; 66 -8.5; 72 -9.0; 79 -8.3; 87 -5.8; 96 -3.8; 106 -5.6; 116 -8.2; 128 -10.3; 141 -11.0; 155 -9.7; 170 -8.8; 187 -10.0; 206 -9.7; 227 -9.5; 249 -9.6; 274 -9.7; 302 -9.6; 332 -9.4; 365 -9.3; 402 -9.1; 442 -8.9; 486 -8.9; 535 -8.8; 588 -8.5; 647 -8.6; 712 -8.5; 783 -7.6; 861 -7.4; 947 -7.5; 1042 -7.5; 1146 -7.4; 1261 -7.6; 1387 -8.2; 1526 -9.0; 1678 -9.8; 1846 -10.1; 2031 -10.1; 2234 -9.3; 2457 -7.2; 2703 -5.4; 2973 -3.6; 3270 -2.7; 3597 -1.7; 3957 -0.7; 4353 -1.1; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Custom One Pro switch position 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Custom One Pro switch position 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 1.68 | -3.4 dB |
| Peaking | 139 Hz  | 5.64 | -3.5 dB |
| Peaking | 321 Hz  | 0.71 | -3.2 dB |
| Peaking | 1929 Hz | 1.96 | -5.0 dB |
| Peaking | 4478 Hz | 1.17 | 6.9 dB  |
| Peaking | 76 Hz   | 3.62 | -2.1 dB |
| Peaking | 97 Hz   | 3.57 | 5.9 dB  |
| Peaking | 115 Hz  | 1.87 | -2.0 dB |
| Peaking | 6360 Hz | 3.52 | 4.2 dB  |
| Peaking | 7465 Hz | 1.49 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20Custom%20One%20Pro%20switch%20position%203/Beyerdynamic%20Custom%20One%20Pro%20switch%20position%203.png)