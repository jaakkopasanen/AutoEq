# Sennheiser HD 600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.7; 54 -1.3; 60 -1.9; 66 -2.5; 72 -3.0; 79 -3.6; 87 -4.2; 96 -4.8; 106 -5.3; 116 -5.8; 128 -6.2; 141 -6.5; 155 -6.7; 170 -6.8; 187 -6.7; 206 -6.6; 227 -6.4; 249 -6.2; 274 -6.1; 302 -6.1; 332 -6.1; 365 -6.0; 402 -6.0; 442 -6.0; 486 -6.1; 535 -6.1; 588 -6.0; 647 -5.9; 712 -5.8; 783 -5.7; 861 -5.7; 947 -5.4; 1042 -5.4; 1146 -6.0; 1261 -6.5; 1387 -7.2; 1526 -7.7; 1678 -8.1; 1846 -8.7; 2031 -9.0; 2234 -8.6; 2457 -8.3; 2703 -8.0; 2973 -8.3; 3270 -8.5; 3597 -8.5; 3957 -7.4; 4353 -5.9; 4788 -6.8; 5267 -6.8; 5793 -5.5; 6373 -5.1; 7010 -6.2; 7711 -7.0; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.9; 16529 -7.5; 18182 -8.5; 20000 -13.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.68 | 6.8 dB  |
| Peaking | 989 Hz   | 1.24 | 1.5 dB  |
| Peaking | 1947 Hz  | 1.39 | -2.7 dB |
| Peaking | 3395 Hz  | 4.38 | -1.6 dB |
| Peaking | 6199 Hz  | 6.1  | 1.8 dB  |
| Peaking | 30 Hz    | 0.11 | 1.9 dB  |
| Peaking | 33 Hz    | 1.54 | -2.6 dB |
| Peaking | 140 Hz   | 0.86 | -2.4 dB |
| Peaking | 20090 Hz | 1.03 | -7.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | 0.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20600/Sennheiser%20HD%20600.png)