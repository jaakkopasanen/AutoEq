# Zipbuds Pro Mic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -8.2; 25 -8.6; 28 -9.0; 31 -9.3; 34 -9.4; 37 -9.5; 41 -9.7; 45 -10.0; 49 -10.2; 54 -10.3; 60 -10.5; 66 -10.6; 72 -10.6; 79 -10.9; 87 -11.0; 96 -11.2; 106 -11.0; 116 -10.9; 128 -10.9; 141 -10.7; 155 -10.5; 170 -10.2; 187 -9.8; 206 -9.5; 227 -8.9; 249 -8.5; 274 -7.9; 302 -7.4; 332 -6.7; 365 -6.1; 402 -5.4; 442 -4.6; 486 -4.2; 535 -3.5; 588 -2.6; 647 -2.0; 712 -1.5; 783 -0.9; 861 -0.8; 947 -0.7; 1042 -0.9; 1146 -0.5; 1261 -0.9; 1387 -1.5; 1526 -2.5; 1678 -3.4; 1846 -3.9; 2031 -4.2; 2234 -4.5; 2457 -4.4; 2703 -4.8; 2973 -4.2; 3270 -3.2; 3597 -2.4; 3957 -4.0; 4353 -8.1; 4788 -12.8; 5267 -12.2; 5793 -6.3; 6373 -3.3; 7010 -4.1; 7711 -8.6; 8482 -11.2; 9330 -6.8; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Zipbuds Pro Mic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Zipbuds Pro Mic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.39 | -2.5 dB |
| Peaking | 151 Hz  | 0.4  | -4.4 dB |
| Peaking | 883 Hz  | 0.56 | 5.7 dB  |
| Peaking | 5025 Hz | 5.22 | -7.7 dB |
| Peaking | 9948 Hz | 3.44 | -2.4 dB |
| Peaking | 3674 Hz | 2.69 | 7.4 dB  |
| Peaking | 4403 Hz | 1.01 | -5.4 dB |
| Peaking | 6497 Hz | 2.59 | 6.8 dB  |
| Peaking | 8341 Hz | 3.56 | -7.5 dB |
| Peaking | 9787 Hz | 3.03 | 4.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Zipbuds%20Pro%20Mic/Zipbuds%20Pro%20Mic.png)