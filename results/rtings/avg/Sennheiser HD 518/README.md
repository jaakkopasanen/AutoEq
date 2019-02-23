# Sennheiser HD 518
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.8; 37 -1.5; 41 -2.3; 45 -3.0; 49 -3.7; 54 -4.4; 60 -5.1; 66 -5.8; 72 -6.4; 79 -6.9; 87 -7.5; 96 -8.0; 106 -8.6; 116 -9.1; 128 -9.5; 141 -9.7; 155 -9.8; 170 -9.9; 187 -9.8; 206 -9.6; 227 -9.3; 249 -9.1; 274 -9.0; 302 -8.9; 332 -8.8; 365 -8.6; 402 -8.5; 442 -8.4; 486 -8.2; 535 -8.0; 588 -7.8; 647 -7.3; 712 -6.6; 783 -6.6; 861 -6.5; 947 -6.3; 1042 -5.9; 1146 -5.3; 1261 -4.7; 1387 -4.0; 1526 -2.8; 1678 -2.3; 1846 -2.6; 2031 -3.2; 2234 -3.5; 2457 -3.7; 2703 -3.6; 2973 -4.6; 3270 -6.3; 3597 -6.9; 3957 -7.2; 4353 -8.4; 4788 -6.9; 5267 -5.5; 5793 -4.7; 6373 -2.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.6; 18182 -10.1; 20000 -10.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 518 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 518 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.49 | 7.4 dB  |
| Peaking | 132 Hz   | 0.34 | -4.3 dB |
| Peaking | 1834 Hz  | 1.2  | 4.3 dB  |
| Peaking | 4254 Hz  | 3.94 | -2.6 dB |
| Peaking | 6470 Hz  | 5.32 | 4.6 dB  |
| Peaking | 257 Hz   | 4.35 | 0.4 dB  |
| Peaking | 2140 Hz  | 4.44 | -0.9 dB |
| Peaking | 2972 Hz  | 2.12 | 1.6 dB  |
| Peaking | 3332 Hz  | 4.97 | -2.1 dB |
| Peaking | 19182 Hz | 1.34 | -5.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.4 dB |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20518/Sennheiser%20HD%20518.png)