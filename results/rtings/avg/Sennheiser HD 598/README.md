# Sennheiser HD 598
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -1.0; 49 -1.6; 54 -2.3; 60 -3.1; 66 -3.8; 72 -4.4; 79 -5.0; 87 -5.7; 96 -6.3; 106 -6.8; 116 -7.3; 128 -7.7; 141 -8.0; 155 -8.3; 170 -8.4; 187 -8.3; 206 -8.2; 227 -8.0; 249 -7.8; 274 -7.6; 302 -7.5; 332 -7.3; 365 -7.0; 402 -6.8; 442 -6.7; 486 -6.8; 535 -6.5; 588 -5.7; 647 -5.7; 712 -5.5; 783 -5.3; 861 -5.0; 947 -4.9; 1042 -4.9; 1146 -4.7; 1261 -4.9; 1387 -5.0; 1526 -4.9; 1678 -4.9; 1846 -5.3; 2031 -6.1; 2234 -6.9; 2457 -6.9; 2703 -6.5; 2973 -6.2; 3270 -6.8; 3597 -7.4; 3957 -8.0; 4353 -9.0; 4788 -7.8; 5267 -6.3; 5793 -6.2; 6373 -4.2; 7010 -4.1; 7711 -6.2; 8482 -7.4; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.6; 18182 -11.1; 20000 -13.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.41 | 6.8 dB  |
| Peaking | 133 Hz   | 0.58 | -3.5 dB |
| Peaking | 1063 Hz  | 0.94 | 1.9 dB  |
| Peaking | 4276 Hz  | 3.75 | -2.6 dB |
| Peaking | 6663 Hz  | 6.68 | 3.5 dB  |
| Peaking | 1704 Hz  | 5.23 | 0.8 dB  |
| Peaking | 2280 Hz  | 5.41 | -1.0 dB |
| Peaking | 19396 Hz | 1.31 | -7.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20598/Sennheiser%20HD%20598.png)