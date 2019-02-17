# Grado GR10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.0; 25 -3.1; 28 -3.2; 31 -3.2; 34 -3.3; 37 -3.4; 41 -3.7; 45 -3.8; 49 -4.0; 54 -4.2; 60 -4.5; 66 -4.8; 72 -5.2; 79 -5.6; 87 -5.9; 96 -6.2; 106 -6.5; 116 -6.7; 128 -7.0; 141 -7.3; 155 -7.5; 170 -7.7; 187 -7.8; 206 -7.9; 227 -8.0; 249 -8.0; 274 -8.0; 302 -7.9; 332 -7.7; 365 -7.6; 402 -7.5; 442 -7.4; 486 -7.3; 535 -7.1; 588 -6.9; 647 -6.9; 712 -6.6; 783 -5.9; 861 -5.8; 947 -6.1; 1042 -6.6; 1146 -6.9; 1261 -7.2; 1387 -7.7; 1526 -8.2; 1678 -8.4; 1846 -8.2; 2031 -8.0; 2234 -7.8; 2457 -7.7; 2703 -7.6; 2973 -5.9; 3270 -1.2; 3597 -0.5; 3957 -1.1; 4353 -6.9; 4788 -5.2; 5267 -2.4; 5793 -1.2; 6373 -2.7; 7010 -7.4; 7711 -11.7; 8482 -11.4; 9330 -8.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado GR10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GR10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.25 | 3.6 dB  |
| Peaking | 51 Hz   | 2.09 | 2.0 dB  |
| Peaking | 3604 Hz | 2.74 | 12.4 dB |
| Peaking | 4733 Hz | 0.63 | -7.6 dB |
| Peaking | 5734 Hz | 3.18 | 11.7 dB |
| Peaking | 246 Hz  | 0.89 | -1.6 dB |
| Peaking | 858 Hz  | 3.51 | 1.5 dB  |
| Peaking | 6562 Hz | 7.38 | 3.3 dB  |
| Peaking | 8022 Hz | 2.54 | -6.3 dB |
| Peaking | 9819 Hz | 1.39 | 3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20GR10/Grado%20GR10.png)