# Sennheiser HD 599
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.5; 28 -2.1; 31 -2.7; 34 -3.2; 37 -3.6; 41 -4.0; 45 -4.4; 49 -4.8; 54 -5.3; 60 -5.9; 66 -6.5; 72 -7.0; 79 -7.4; 87 -8.0; 96 -8.5; 106 -9.0; 116 -9.5; 128 -9.9; 141 -10.2; 155 -10.3; 170 -10.3; 187 -10.2; 206 -9.9; 227 -9.6; 249 -9.3; 274 -9.1; 302 -8.9; 332 -8.7; 365 -8.5; 402 -8.2; 442 -8.0; 486 -7.8; 535 -7.6; 588 -7.3; 647 -6.7; 712 -6.2; 783 -5.8; 861 -5.6; 947 -5.4; 1042 -5.2; 1146 -4.8; 1261 -4.6; 1387 -4.1; 1526 -3.2; 1678 -3.0; 1846 -3.9; 2031 -5.3; 2234 -5.7; 2457 -4.9; 2703 -5.6; 2973 -7.2; 3270 -8.5; 3597 -8.0; 3957 -8.1; 4353 -9.6; 4788 -8.2; 5267 -6.5; 5793 -6.7; 6373 -5.2; 7010 -3.8; 7711 -5.1; 8482 -8.1; 9330 -7.6; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -6.0; 18182 -11.4; 20000 -11.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 599 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 599 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 10 Hz    | 0.27 | 5.8 dB  |
| Peaking | 165 Hz   | 0.44 | -5.2 dB |
| Peaking | 1578 Hz  | 2.13 | 2.7 dB  |
| Peaking | 4020 Hz  | 1.84 | -3.8 dB |
| Peaking | 19344 Hz | 1.28 | -8.2 dB |
| Peaking | 6028 Hz  | 3.97 | -1.3 dB |
| Peaking | 6944 Hz  | 3.88 | 3.0 dB  |
| Peaking | 8888 Hz  | 6.27 | -3.9 dB |
| Peaking | 16765 Hz | 0.81 | 1.5 dB  |
| Peaking | 17833 Hz | 2.63 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.8 dB |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20599/Sennheiser%20HD%20599.png)