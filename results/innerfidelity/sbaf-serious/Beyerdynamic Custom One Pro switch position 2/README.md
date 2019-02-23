# Beyerdynamic Custom One Pro switch position 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.5; 25 -7.9; 28 -8.4; 31 -8.7; 34 -8.9; 37 -9.0; 41 -9.1; 45 -9.1; 49 -8.7; 54 -7.9; 60 -6.6; 66 -6.2; 72 -6.3; 79 -4.8; 87 -2.5; 96 -1.6; 106 -2.9; 116 -4.4; 128 -6.3; 141 -8.1; 155 -8.4; 170 -8.6; 187 -11.1; 206 -11.2; 227 -11.0; 249 -10.9; 274 -10.9; 302 -10.6; 332 -10.3; 365 -10.0; 402 -9.7; 442 -9.4; 486 -9.3; 535 -9.1; 588 -8.7; 647 -8.5; 712 -8.6; 783 -7.5; 861 -7.3; 947 -7.4; 1042 -7.3; 1146 -7.3; 1261 -7.5; 1387 -8.1; 1526 -8.8; 1678 -9.6; 1846 -10.0; 2031 -10.1; 2234 -9.4; 2457 -7.4; 2703 -5.7; 2973 -3.9; 3270 -3.0; 3597 -2.2; 3957 -1.1; 4353 -0.8; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Custom One Pro switch position 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Custom One Pro switch position 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 1.19 | -2.8 dB |
| Peaking | 98 Hz   | 1.96 | 7.3 dB  |
| Peaking | 238 Hz  | 0.58 | -4.9 dB |
| Peaking | 1953 Hz | 2.17 | -4.8 dB |
| Peaking | 4599 Hz | 1.26 | 6.9 dB  |
| Peaking | 351 Hz  | 4.74 | 0.3 dB  |
| Peaking | 3114 Hz | 5.03 | 1.0 dB  |
| Peaking | 4614 Hz | 4.16 | -0.7 dB |
| Peaking | 6324 Hz | 3.14 | 4.1 dB  |
| Peaking | 7561 Hz | 1.53 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | 2.4 dB  |
| Peaking | 250 Hz   | 1.41 | -5.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20Custom%20One%20Pro%20switch%20position%202/Beyerdynamic%20Custom%20One%20Pro%20switch%20position%202.png)