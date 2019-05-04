# Grado SR225e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.0; 54 -1.6; 60 -2.3; 66 -2.8; 72 -3.2; 79 -3.5; 87 -3.8; 96 -4.1; 106 -4.3; 116 -4.5; 128 -4.7; 141 -4.8; 155 -4.8; 170 -4.8; 187 -4.8; 206 -4.5; 227 -4.3; 249 -4.3; 274 -5.0; 302 -5.0; 332 -4.7; 365 -4.6; 402 -4.7; 442 -4.8; 486 -4.9; 535 -4.9; 588 -4.8; 647 -4.7; 712 -4.5; 783 -4.4; 861 -4.2; 947 -4.2; 1042 -4.3; 1146 -4.3; 1261 -4.7; 1387 -5.2; 1526 -6.0; 1678 -6.9; 1846 -10.6; 2031 -13.7; 2234 -13.8; 2457 -12.0; 2703 -9.9; 2973 -8.3; 3270 -7.4; 3597 -5.5; 3957 -5.1; 4353 -10.0; 4788 -9.9; 5267 -9.2; 5793 -9.3; 6373 -6.1; 7010 -5.6; 7711 -8.7; 8482 -11.0; 9330 -12.3; 10263 -14.6; 11289 -15.6; 12418 -12.9; 13660 -8.2; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.4  | 6.2 dB  |
| Peaking | 885 Hz   | 0.43 | 2.6 dB  |
| Peaking | 2176 Hz  | 2.67 | -9.4 dB |
| Peaking | 9625 Hz  | 2.25 | -4.1 dB |
| Peaking | 11393 Hz | 2.71 | -7.8 dB |
| Peaking | 229 Hz   | 4.17 | 0.9 dB  |
| Peaking | 3869 Hz  | 4.41 | 6.2 dB  |
| Peaking | 4428 Hz  | 2.25 | -5.5 dB |
| Peaking | 6783 Hz  | 6.83 | 3.7 dB  |
| Peaking | 14647 Hz | 4.2  | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | 1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.9 dB |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Grado%20SR225e/Grado%20SR225e.png)