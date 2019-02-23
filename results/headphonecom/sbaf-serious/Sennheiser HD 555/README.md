# Sennheiser HD 555
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -1.0; 34 -1.5; 37 -2.0; 41 -2.6; 45 -3.0; 49 -3.5; 54 -3.7; 60 -3.9; 66 -3.7; 72 -3.5; 79 -4.9; 87 -5.8; 96 -6.3; 106 -6.7; 116 -7.0; 128 -7.3; 141 -7.7; 155 -7.8; 170 -7.9; 187 -8.1; 206 -8.3; 227 -8.3; 249 -8.3; 274 -8.2; 302 -8.1; 332 -7.9; 365 -7.8; 402 -7.5; 442 -7.3; 486 -7.2; 535 -7.2; 588 -6.7; 647 -6.8; 712 -6.7; 783 -6.9; 861 -6.7; 947 -7.0; 1042 -7.1; 1146 -6.9; 1261 -6.5; 1387 -6.0; 1526 -5.6; 1678 -5.4; 1846 -6.3; 2031 -6.5; 2234 -6.7; 2457 -6.7; 2703 -6.2; 2973 -6.8; 3270 -7.9; 3597 -7.3; 3957 -5.2; 4353 -4.8; 4788 -7.3; 5267 -4.1; 5793 -0.6; 6373 -3.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.7; 18182 -10.2; 20000 -9.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 555 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 555 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.66 | 6.2 dB  |
| Peaking | 70 Hz    | 4.31 | 1.8 dB  |
| Peaking | 206 Hz   | 0.67 | -2.0 dB |
| Peaking | 5898 Hz  | 4.73 | 6.2 dB  |
| Peaking | 19028 Hz | 1.34 | -4.8 dB |
| Peaking | 1596 Hz  | 5.65 | 1.3 dB  |
| Peaking | 3422 Hz  | 4.95 | -1.8 dB |
| Peaking | 4178 Hz  | 7.86 | 3.2 dB  |
| Peaking | 4707 Hz  | 8.8  | -2.6 dB |
| Peaking | 15888 Hz | 2.92 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20555/Sennheiser%20HD%20555.png)