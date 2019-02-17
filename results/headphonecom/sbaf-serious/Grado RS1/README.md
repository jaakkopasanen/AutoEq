# Grado RS1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.9; 45 -1.9; 49 -2.8; 54 -4.0; 60 -5.4; 66 -6.6; 72 -7.7; 79 -8.6; 87 -9.2; 96 -9.7; 106 -10.1; 116 -10.3; 128 -10.3; 141 -10.1; 155 -9.9; 170 -9.5; 187 -9.3; 206 -9.2; 227 -8.9; 249 -8.5; 274 -8.0; 302 -7.0; 332 -7.3; 365 -8.1; 402 -7.7; 442 -7.4; 486 -7.1; 535 -6.9; 588 -6.7; 647 -6.4; 712 -6.3; 783 -6.3; 861 -6.2; 947 -6.4; 1042 -6.6; 1146 -6.8; 1261 -7.2; 1387 -8.0; 1526 -9.0; 1678 -11.3; 1846 -15.7; 2031 -14.8; 2234 -13.8; 2457 -12.7; 2703 -11.1; 2973 -9.1; 3270 -7.3; 3597 -6.0; 3957 -7.4; 4353 -14.8; 4788 -20.3; 5267 -15.9; 5793 -15.5; 6373 -10.1; 7010 -6.5; 7711 -9.8; 8482 -16.1; 9330 -19.4; 10263 -16.6; 11289 -11.0; 12418 -9.2; 13660 -11.2; 15026 -10.5; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.53 | 8.1 dB   |
| Peaking | 98 Hz    | 0.64 | -6.5 dB  |
| Peaking | 2013 Hz  | 2.83 | -9.3 dB  |
| Peaking | 4885 Hz  | 4.64 | -13.4 dB |
| Peaking | 9483 Hz  | 2.72 | -13.2 dB |
| Peaking | 2597 Hz  | 6.33 | -2.1 dB  |
| Peaking | 3677 Hz  | 6.31 | 4.2 dB   |
| Peaking | 5830 Hz  | 7.57 | -4.5 dB  |
| Peaking | 7021 Hz  | 6.41 | 4.9 dB   |
| Peaking | 14301 Hz | 3.64 | -4.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.8 dB |
| Peaking | 4000 Hz  | 1.41 | -2.3 dB |
| Peaking | 8000 Hz  | 1.41 | -8.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20RS1/Grado%20RS1.png)