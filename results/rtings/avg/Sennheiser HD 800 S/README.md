# Sennheiser HD 800 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -0.9; 28 -1.1; 31 -1.3; 34 -1.4; 37 -1.6; 41 -1.7; 45 -1.9; 49 -2.1; 54 -2.4; 60 -2.8; 66 -3.3; 72 -3.7; 79 -4.1; 87 -4.6; 96 -5.0; 106 -5.6; 116 -6.1; 128 -6.5; 141 -6.9; 155 -7.2; 170 -7.3; 187 -7.4; 206 -7.4; 227 -7.3; 249 -7.3; 274 -7.4; 302 -7.4; 332 -7.5; 365 -7.4; 402 -7.4; 442 -7.4; 486 -7.4; 535 -7.3; 588 -7.1; 647 -6.9; 712 -6.6; 783 -6.4; 861 -6.0; 947 -5.8; 1042 -5.6; 1146 -5.3; 1261 -5.1; 1387 -4.9; 1526 -4.5; 1678 -4.4; 1846 -5.6; 2031 -6.5; 2234 -5.6; 2457 -4.9; 2703 -3.9; 2973 -4.6; 3270 -4.4; 3597 -6.4; 3957 -7.1; 4353 -5.6; 4788 -5.0; 5267 -6.2; 5793 -8.4; 6373 -9.8; 7010 -8.3; 7711 -7.9; 8482 -6.5; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -9.5; 13660 -8.6; 15026 -6.3; 16529 -6.3; 18182 -7.9; 20000 -13.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.05 | 5.6 dB  |
| Peaking | 53 Hz    | 1.67 | 3.0 dB  |
| Peaking | 2494 Hz  | 0.82 | 1.5 dB  |
| Peaking | 6456 Hz  | 3.63 | -3.7 dB |
| Peaking | 20069 Hz | 1.11 | -6.6 dB |
| Peaking | 364 Hz   | 0.53 | -1.5 dB |
| Peaking | 2047 Hz  | 0.73 | 2.3 dB  |
| Peaking | 2075 Hz  | 3.04 | -3.6 dB |
| Peaking | 3790 Hz  | 6.74 | -2.8 dB |
| Peaking | 12779 Hz | 5.75 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20800%20S/Sennheiser%20HD%20800%20S.png)