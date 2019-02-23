# Superlux HD 681
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.6; 72 -1.3; 79 -1.9; 87 -2.1; 96 -2.6; 106 -3.0; 116 -3.4; 128 -3.6; 141 -4.1; 155 -4.1; 170 -3.7; 187 -3.5; 206 -3.9; 227 -3.9; 249 -3.9; 274 -3.9; 302 -3.5; 332 -3.2; 365 -3.1; 402 -3.0; 442 -3.2; 486 -3.3; 535 -3.7; 588 -3.7; 647 -3.7; 712 -4.1; 783 -4.5; 861 -5.0; 947 -5.5; 1042 -6.0; 1146 -6.4; 1261 -7.2; 1387 -8.3; 1526 -9.2; 1678 -9.3; 1846 -10.3; 2031 -11.0; 2234 -11.1; 2457 -11.0; 2703 -9.8; 2973 -8.7; 3270 -7.2; 3597 -5.4; 3957 -5.8; 4353 -7.5; 4788 -10.8; 5267 -8.5; 5793 -10.7; 6373 -7.5; 7010 -6.0; 7711 -12.3; 8482 -15.8; 9330 -15.2; 10263 -12.0; 11289 -6.8; 12418 -6.5; 13660 -7.2; 15026 -7.5; 16529 -6.5; 18182 -6.5; 20000 -10.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 681 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 681 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 0.38 | 6.4 dB   |
| Peaking | 468 Hz   | 0.63 | 3.2 dB   |
| Peaking | 1573 Hz  | 2.12 | -2.4 dB  |
| Peaking | 2267 Hz  | 2.33 | -4.6 dB  |
| Peaking | 8873 Hz  | 2.98 | -10.2 dB |
| Peaking | 3774 Hz  | 4.07 | 4.0 dB   |
| Peaking | 5557 Hz  | 1.19 | -3.5 dB  |
| Peaking | 6769 Hz  | 6.68 | 6.6 dB   |
| Peaking | 11697 Hz | 5.08 | 2.3 dB   |
| Peaking | 19960 Hz | 3.39 | -4.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.7 dB  |
| Peaking | 125 Hz   | 1.41 | 1.6 dB  |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Superlux%20HD%20681/Superlux%20HD%20681.png)