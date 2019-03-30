# Dunu DN-900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.0; 23 -11.8; 25 -11.6; 28 -11.3; 31 -11.0; 34 -10.8; 37 -10.6; 41 -10.3; 45 -10.1; 49 -9.9; 54 -9.7; 60 -9.5; 66 -9.3; 72 -9.2; 79 -9.0; 87 -8.9; 96 -8.8; 106 -8.6; 116 -8.5; 128 -8.5; 141 -8.5; 155 -8.5; 170 -8.6; 187 -8.3; 206 -8.2; 227 -8.2; 249 -8.2; 274 -8.2; 302 -8.2; 332 -8.2; 365 -8.0; 402 -7.9; 442 -7.9; 486 -7.9; 535 -7.9; 588 -7.9; 647 -7.9; 712 -7.9; 783 -7.9; 861 -7.9; 947 -7.9; 1042 -7.9; 1146 -8.0; 1261 -8.3; 1387 -8.6; 1526 -9.1; 1678 -9.5; 1846 -9.5; 2031 -8.9; 2234 -7.9; 2457 -6.6; 2703 -6.2; 2973 -6.8; 3270 -6.9; 3597 -6.1; 3957 -4.6; 4353 -3.5; 4788 -3.0; 5267 -2.5; 5793 -0.8; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DN-900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN-900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.75 | -5.4 dB |
| Peaking | 25 Hz   | 0.47 | -3.1 dB |
| Peaking | 243 Hz  | 0.19 | -2.1 dB |
| Peaking | 1740 Hz | 2.03 | -3.0 dB |
| Peaking | 5852 Hz | 2.5  | 5.8 dB  |
| Peaking | 2638 Hz | 4.04 | 1.8 dB  |
| Peaking | 3085 Hz | 1.59 | -1.6 dB |
| Peaking | 4245 Hz | 4.1  | 1.9 dB  |
| Peaking | 8107 Hz | 4.53 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Dunu%20DN-900/Dunu%20DN-900.png)