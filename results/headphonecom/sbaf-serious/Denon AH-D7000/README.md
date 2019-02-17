# Denon AH-D7000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.7; 25 -2.7; 28 -3.8; 31 -4.7; 34 -5.2; 37 -5.4; 41 -5.8; 45 -6.1; 49 -6.1; 54 -5.7; 60 -5.6; 66 -5.8; 72 -5.8; 79 -5.8; 87 -5.8; 96 -5.6; 106 -5.6; 116 -5.5; 128 -5.4; 141 -5.4; 155 -5.2; 170 -4.7; 187 -4.7; 206 -4.4; 227 -4.1; 249 -3.8; 274 -3.5; 302 -3.1; 332 -2.6; 365 -2.1; 402 -2.0; 442 -2.4; 486 -3.2; 535 -3.7; 588 -4.5; 647 -5.1; 712 -5.4; 783 -5.9; 861 -5.4; 947 -4.4; 1042 -5.1; 1146 -4.7; 1261 -4.1; 1387 -3.6; 1526 -3.5; 1678 -3.2; 1846 -2.9; 2031 -3.0; 2234 -2.5; 2457 -2.1; 2703 -2.0; 2973 -2.4; 3270 -4.0; 3597 -5.1; 3957 -4.7; 4353 -4.9; 4788 -6.0; 5267 -3.7; 5793 -3.3; 6373 -6.0; 7010 -6.5; 7711 -5.2; 8482 -5.1; 9330 -5.2; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D7000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 3.07 | 4.4 dB  |
| Peaking | 374 Hz  | 1.95 | 3.3 dB  |
| Peaking | 2449 Hz | 1.29 | 3.3 dB  |
| Peaking | 5464 Hz | 1.62 | -2.9 dB |
| Peaking | 5538 Hz | 5.03 | 4.8 dB  |
| Peaking | 22 Hz   | 1.26 | 2.1 dB  |
| Peaking | 43 Hz   | 0.71 | -1.3 dB |
| Peaking | 784 Hz  | 5.27 | -1.4 dB |
| Peaking | 1589 Hz | 2.17 | 0.6 dB  |
| Peaking | 2093 Hz | 6.05 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | 1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D7000/Denon%20AH-D7000.png)