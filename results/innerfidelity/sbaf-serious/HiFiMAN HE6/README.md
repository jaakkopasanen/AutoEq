# HiFiMAN HE6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.1; 28 -1.3; 31 -1.5; 34 -1.6; 37 -1.6; 41 -1.6; 45 -1.7; 49 -1.8; 54 -1.9; 60 -1.8; 66 -1.9; 72 -2.4; 79 -2.6; 87 -2.8; 96 -3.3; 106 -3.4; 116 -3.5; 128 -3.8; 141 -3.9; 155 -4.1; 170 -4.0; 187 -4.0; 206 -4.1; 227 -3.9; 249 -4.0; 274 -4.1; 302 -4.2; 332 -4.3; 365 -4.4; 402 -4.5; 442 -4.2; 486 -4.4; 535 -4.4; 588 -4.2; 647 -4.2; 712 -4.5; 783 -4.3; 861 -4.6; 947 -4.9; 1042 -4.5; 1146 -3.6; 1261 -3.9; 1387 -3.6; 1526 -2.9; 1678 -2.4; 1846 -1.4; 2031 -1.7; 2234 -2.3; 2457 -1.9; 2703 -2.5; 2973 -3.5; 3270 -4.7; 3597 -4.5; 3957 -6.1; 4353 -5.9; 4788 -4.5; 5267 -6.7; 5793 -10.3; 6373 -9.4; 7010 -8.4; 7711 -8.0; 8482 -10.7; 9330 -11.7; 10263 -6.8; 11289 -4.7; 12418 -4.7; 13660 -6.7; 15026 -7.1; 16529 -5.2; 18182 -5.0; 20000 -9.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 1.23 | 4.0 dB  |
| Peaking | 44 Hz    | 0.47 | 2.7 dB  |
| Peaking | 2046 Hz  | 1.58 | 3.3 dB  |
| Peaking | 6072 Hz  | 3.29 | -5.3 dB |
| Peaking | 8988 Hz  | 3.99 | -7.3 dB |
| Peaking | 2647 Hz  | 7.01 | 0.8 dB  |
| Peaking | 4415 Hz  | 2.54 | -1.4 dB |
| Peaking | 4889 Hz  | 8.64 | 3.1 dB  |
| Peaking | 11923 Hz | 2.25 | 2.9 dB  |
| Peaking | 13939 Hz | 1.3  | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | -5.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE6/HiFiMAN%20HE6.png)