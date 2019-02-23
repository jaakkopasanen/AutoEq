# Sennheiser HD 700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.1; 31 -1.6; 34 -1.9; 37 -2.2; 41 -2.6; 45 -3.0; 49 -3.4; 54 -3.8; 60 -4.4; 66 -5.0; 72 -5.5; 79 -6.0; 87 -6.6; 96 -7.1; 106 -7.6; 116 -8.1; 128 -8.5; 141 -8.8; 155 -9.0; 170 -9.1; 187 -9.0; 206 -8.8; 227 -8.7; 249 -8.6; 274 -8.5; 302 -8.4; 332 -8.3; 365 -8.2; 402 -8.0; 442 -7.9; 486 -7.8; 535 -7.6; 588 -7.3; 647 -7.0; 712 -6.6; 783 -6.1; 861 -5.7; 947 -5.4; 1042 -5.0; 1146 -4.5; 1261 -3.8; 1387 -3.3; 1526 -2.8; 1678 -2.5; 1846 -2.1; 2031 -2.4; 2234 -1.7; 2457 -2.0; 2703 -2.1; 2973 -2.9; 3270 -2.9; 3597 -3.2; 3957 -4.5; 4353 -5.2; 4788 -6.1; 5267 -9.1; 5793 -11.4; 6373 -15.6; 7010 -10.5; 7711 -8.3; 8482 -8.1; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.2; 18182 -13.7; 20000 -16.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.58 | 6.6 dB  |
| Peaking | 59 Hz   | 0.98 | 2.4 dB  |
| Peaking | 132 Hz  | 0.26 | -3.2 dB |
| Peaking | 2240 Hz | 0.65 | 5.0 dB  |
| Peaking | 6291 Hz | 3.4  | -9.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20700/Sennheiser%20HD%20700.png)