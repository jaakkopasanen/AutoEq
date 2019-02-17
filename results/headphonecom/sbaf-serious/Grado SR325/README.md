# Grado SR325
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.8; 49 -1.7; 54 -2.8; 60 -3.9; 66 -4.7; 72 -5.4; 79 -6.0; 87 -6.5; 96 -6.9; 106 -7.1; 116 -7.1; 128 -7.1; 141 -7.1; 155 -7.2; 170 -7.1; 187 -7.0; 206 -7.0; 227 -7.0; 249 -6.8; 274 -6.7; 302 -6.6; 332 -6.4; 365 -6.2; 402 -6.1; 442 -6.0; 486 -6.1; 535 -6.0; 588 -6.0; 647 -5.9; 712 -5.9; 783 -6.0; 861 -6.1; 947 -6.3; 1042 -6.7; 1146 -7.0; 1261 -7.5; 1387 -8.4; 1526 -9.6; 1678 -10.6; 1846 -12.4; 2031 -14.8; 2234 -14.0; 2457 -12.5; 2703 -10.9; 2973 -9.4; 3270 -7.8; 3597 -7.1; 3957 -10.1; 4353 -18.4; 4788 -17.5; 5267 -12.9; 5793 -10.6; 6373 -11.7; 7010 -12.8; 7711 -13.6; 8482 -16.3; 9330 -18.9; 10263 -17.7; 11289 -14.8; 12418 -10.7; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR325 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 61 Hz    | 0.19 | 11.0 dB  |
| Peaking | 114 Hz   | 0.41 | -11.0 dB |
| Peaking | 2082 Hz  | 2.52 | -8.4 dB  |
| Peaking | 4579 Hz  | 5.77 | -12.4 dB |
| Peaking | 9475 Hz  | 1.75 | -12.8 dB |
| Peaking | 2661 Hz  | 6.07 | -1.1 dB  |
| Peaking | 3717 Hz  | 4.11 | 5.0 dB   |
| Peaking | 4034 Hz  | 2.91 | -3.0 dB  |
| Peaking | 11733 Hz | 3.07 | -3.5 dB  |
| Peaking | 13364 Hz | 1.85 | 3.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB   |
| Peaking | 62 Hz    | 1.41 | 1.1 dB   |
| Peaking | 125 Hz   | 1.41 | -1.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -10.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR325/Grado%20SR325.png)