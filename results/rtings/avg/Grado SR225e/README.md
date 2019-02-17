# Grado SR225e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.8; 37 -1.3; 41 -2.2; 45 -2.9; 49 -3.6; 54 -4.2; 60 -4.8; 66 -5.4; 72 -5.8; 79 -6.1; 87 -6.5; 96 -6.7; 106 -6.9; 116 -7.2; 128 -7.3; 141 -7.4; 155 -7.4; 170 -7.4; 187 -7.3; 206 -7.1; 227 -6.8; 249 -6.8; 274 -7.5; 302 -7.4; 332 -7.1; 365 -7.1; 402 -7.1; 442 -7.2; 486 -7.2; 535 -7.2; 588 -7.1; 647 -6.9; 712 -6.8; 783 -6.6; 861 -6.5; 947 -6.5; 1042 -6.5; 1146 -6.7; 1261 -6.9; 1387 -7.5; 1526 -8.1; 1678 -9.1; 1846 -12.6; 2031 -15.6; 2234 -15.2; 2457 -13.5; 2703 -11.7; 2973 -10.6; 3270 -10.1; 3597 -8.3; 3957 -7.6; 4353 -12.9; 4788 -11.8; 5267 -11.1; 5793 -11.8; 6373 -9.4; 7010 -8.0; 7711 -10.2; 8482 -13.6; 9330 -16.3; 10263 -17.4; 11289 -16.9; 12418 -15.1; 13660 -11.4; 15026 -7.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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
| Peaking | 28 Hz    | 0.6  | 7.1 dB  |
| Peaking | 84 Hz    | 0.39 | -1.9 dB |
| Peaking | 2213 Hz  | 2.24 | -9.0 dB |
| Peaking | 10096 Hz | 1.17 | -9.1 dB |
| Peaking | 11852 Hz | 2.75 | -3.4 dB |
| Peaking | 1726 Hz  | 1.15 | 1.5 dB  |
| Peaking | 1954 Hz  | 6.94 | -3.0 dB |
| Peaking | 4740 Hz  | 3.35 | -4.2 dB |
| Peaking | 7127 Hz  | 6.27 | 3.7 dB  |
| Peaking | 15834 Hz | 2.83 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.2 dB |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | -7.9 dB |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Grado%20SR225e/Grado%20SR225e.png)