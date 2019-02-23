# Grado RS1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.8; 60 -2.1; 66 -3.3; 72 -4.4; 79 -5.3; 87 -5.9; 96 -6.4; 106 -6.8; 116 -7.0; 128 -7.0; 141 -6.8; 155 -6.6; 170 -6.2; 187 -6.0; 206 -5.9; 227 -5.5; 249 -5.2; 274 -4.7; 302 -3.7; 332 -4.0; 365 -4.8; 402 -4.3; 442 -4.1; 486 -3.7; 535 -3.6; 588 -3.3; 647 -3.1; 712 -3.0; 783 -3.0; 861 -2.9; 947 -3.1; 1042 -3.3; 1146 -3.5; 1261 -3.8; 1387 -4.7; 1526 -5.7; 1678 -7.9; 1846 -12.4; 2031 -11.4; 2234 -10.5; 2457 -9.4; 2703 -7.8; 2973 -5.8; 3270 -4.0; 3597 -2.6; 3957 -4.1; 4353 -11.5; 4788 -17.0; 5267 -12.6; 5793 -12.2; 6373 -6.8; 7010 -4.1; 7711 -6.8; 8482 -12.8; 9330 -16.1; 10263 -13.3; 11289 -7.7; 12418 -6.5; 13660 -7.9; 15026 -7.3; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 33 Hz   | 0.92 | 7.1 dB   |
| Peaking | 2044 Hz | 1.4  | -15.9 dB |
| Peaking | 2512 Hz | 0.32 | 10.8 dB  |
| Peaking | 4889 Hz | 3.38 | -16.5 dB |
| Peaking | 9413 Hz | 2.88 | -13.3 dB |
| Peaking | 54 Hz   | 3.69 | 2.3 dB   |
| Peaking | 112 Hz  | 1.87 | -1.7 dB  |
| Peaking | 3765 Hz | 5.78 | 4.5 dB   |
| Peaking | 5385 Hz | 0.88 | -1.9 dB  |
| Peaking | 6988 Hz | 6.42 | 4.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20RS1/Grado%20RS1.png)