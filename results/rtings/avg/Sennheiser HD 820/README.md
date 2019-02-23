# Sennheiser HD 820
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.1; 25 -5.2; 28 -5.2; 31 -5.1; 34 -5.0; 37 -4.9; 41 -4.9; 45 -4.9; 49 -4.9; 54 -5.0; 60 -5.1; 66 -5.4; 72 -5.8; 79 -6.3; 87 -7.0; 96 -7.5; 106 -8.1; 116 -8.6; 128 -8.9; 141 -9.1; 155 -9.1; 170 -8.9; 187 -8.2; 206 -6.8; 227 -4.6; 249 -1.9; 274 -0.5; 302 -0.5; 332 -1.6; 365 -3.6; 402 -5.2; 442 -6.2; 486 -7.0; 535 -7.5; 588 -8.1; 647 -8.8; 712 -9.5; 783 -10.0; 861 -10.2; 947 -10.2; 1042 -9.9; 1146 -9.6; 1261 -9.1; 1387 -8.6; 1526 -7.8; 1678 -7.1; 1846 -7.1; 2031 -7.8; 2234 -7.6; 2457 -6.6; 2703 -6.3; 2973 -5.0; 3270 -1.1; 3597 -0.5; 3957 -1.6; 4353 -4.0; 4788 -5.2; 5267 -6.4; 5793 -7.8; 6373 -9.3; 7010 -6.7; 7711 -6.6; 8482 -8.2; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -9.7; 15026 -7.8; 16529 -6.5; 18182 -6.5; 20000 -8.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 820 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 820 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 162 Hz   | 1.55 | -4.1 dB |
| Peaking | 287 Hz   | 1.92 | 8.0 dB  |
| Peaking | 886 Hz   | 0.89 | -4.0 dB |
| Peaking | 3618 Hz  | 3.31 | 7.0 dB  |
| Peaking | 6171 Hz  | 5.42 | -3.2 dB |
| Peaking | 44 Hz    | 0.56 | 1.9 dB  |
| Peaking | 105 Hz   | 1.95 | -1.4 dB |
| Peaking | 2190 Hz  | 5.7  | -0.9 dB |
| Peaking | 13303 Hz | 6.27 | -2.1 dB |
| Peaking | 14436 Hz | 4.41 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | 5.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -4.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20820/Sennheiser%20HD%20820.png)