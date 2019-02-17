# Sennheiser HD 650
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.0; 37 -1.5; 41 -2.1; 45 -2.5; 49 -2.9; 54 -3.4; 60 -4.0; 66 -4.5; 72 -5.0; 79 -5.5; 87 -6.1; 96 -6.6; 106 -7.1; 116 -7.6; 128 -8.0; 141 -8.3; 155 -8.5; 170 -8.6; 187 -8.7; 206 -8.5; 227 -8.4; 249 -8.2; 274 -8.2; 302 -8.1; 332 -8.1; 365 -8.0; 402 -8.0; 442 -8.0; 486 -7.9; 535 -7.9; 588 -7.7; 647 -7.6; 712 -7.4; 783 -7.4; 861 -7.3; 947 -6.7; 1042 -6.9; 1146 -7.2; 1261 -7.6; 1387 -7.9; 1526 -8.1; 1678 -8.3; 1846 -8.5; 2031 -8.7; 2234 -8.0; 2457 -7.7; 2703 -7.7; 2973 -8.2; 3270 -8.4; 3597 -8.1; 3957 -7.3; 4353 -6.6; 4788 -6.8; 5267 -6.5; 5793 -5.3; 6373 -4.2; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.2; 16529 -7.0; 18182 -7.9; 20000 -11.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.36 | 6.6 dB  |
| Peaking | 144 Hz   | 0.38 | -3.1 dB |
| Peaking | 1835 Hz  | 1.74 | -1.9 dB |
| Peaking | 3306 Hz  | 3.34 | -1.7 dB |
| Peaking | 6591 Hz  | 5.09 | 3.2 dB  |
| Peaking | 165 Hz   | 1.29 | -1.0 dB |
| Peaking | 227 Hz   | 0.62 | 1.0 dB  |
| Peaking | 486 Hz   | 0.8  | -0.6 dB |
| Peaking | 989 Hz   | 8.35 | 0.8 dB  |
| Peaking | 19862 Hz | 1.08 | -4.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20650/Sennheiser%20HD%20650.png)