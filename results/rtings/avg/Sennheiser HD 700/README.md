# Sennheiser HD 700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.9; 31 -1.4; 34 -1.8; 37 -2.1; 41 -2.5; 45 -2.8; 49 -3.2; 54 -3.7; 60 -4.3; 66 -4.8; 72 -5.3; 79 -5.8; 87 -6.4; 96 -6.9; 106 -7.4; 116 -7.8; 128 -8.3; 141 -8.6; 155 -8.8; 170 -8.9; 187 -8.9; 206 -8.8; 227 -8.7; 249 -8.6; 274 -8.5; 302 -8.4; 332 -8.3; 365 -8.1; 402 -8.0; 442 -7.8; 486 -7.8; 535 -7.6; 588 -7.4; 647 -7.1; 712 -6.7; 783 -6.3; 861 -5.8; 947 -5.6; 1042 -5.2; 1146 -4.6; 1261 -4.0; 1387 -3.5; 1526 -3.1; 1678 -2.7; 1846 -2.5; 2031 -2.9; 2234 -2.6; 2457 -2.9; 2703 -2.8; 2973 -2.9; 3270 -2.7; 3597 -3.1; 3957 -4.1; 4353 -4.8; 4788 -6.6; 5267 -9.3; 5793 -11.0; 6373 -14.4; 7010 -10.8; 7711 -9.1; 8482 -7.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.2; 18182 -13.6; 20000 -16.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.6  | 6.7 dB  |
| Peaking | 59 Hz   | 1.01 | 2.2 dB  |
| Peaking | 148 Hz  | 0.23 | -2.9 dB |
| Peaking | 2427 Hz | 0.5  | 4.6 dB  |
| Peaking | 6291 Hz | 2.61 | -9.3 dB |
| Peaking | 1653 Hz | 1.73 | 1.3 dB  |
| Peaking | 2039 Hz | 0.79 | -1.1 dB |
| Peaking | 3512 Hz | 2.82 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20700/Sennheiser%20HD%20700.png)