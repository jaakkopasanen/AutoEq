# Mpow H5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -1.8; 28 -2.6; 31 -3.2; 34 -3.7; 37 -4.1; 41 -4.6; 45 -5.0; 49 -5.3; 54 -5.7; 60 -6.2; 66 -6.8; 72 -7.3; 79 -7.9; 87 -8.4; 96 -9.0; 106 -9.4; 116 -9.8; 128 -10.2; 141 -10.5; 155 -10.6; 170 -10.7; 187 -10.6; 206 -10.5; 227 -10.2; 249 -10.1; 274 -9.8; 302 -9.6; 332 -9.8; 365 -9.7; 402 -9.1; 442 -8.1; 486 -6.7; 535 -5.2; 588 -4.0; 647 -3.0; 712 -2.3; 783 -1.5; 861 -0.6; 947 -0.6; 1042 -0.6; 1146 -1.8; 1261 -3.6; 1387 -5.4; 1526 -6.1; 1678 -6.2; 1846 -6.0; 2031 -6.2; 2234 -5.4; 2457 -4.6; 2703 -4.9; 2973 -6.3; 3270 -7.7; 3597 -9.0; 3957 -7.6; 4353 -5.0; 4788 -3.5; 5267 -3.5; 5793 -1.2; 6373 -2.5; 7010 -5.8; 7711 -7.4; 8482 -10.5; 9330 -13.0; 10263 -11.9; 11289 -8.9; 12418 -6.6; 13660 -6.6; 15026 -8.0; 16529 -8.8; 18182 -7.9; 20000 -9.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mpow H5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mpow H5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.32 | 7.2 dB  |
| Peaking | 196 Hz  | 0.4  | -4.6 dB |
| Peaking | 848 Hz  | 1.31 | 7.6 dB  |
| Peaking | 5928 Hz | 3.42 | 6.3 dB  |
| Peaking | 9479 Hz | 2.68 | -7.2 dB |
| Peaking | 1118 Hz | 4.37 | 2.2 dB  |
| Peaking | 1447 Hz | 1.61 | -1.6 dB |
| Peaking | 2593 Hz | 3.22 | 2.4 dB  |
| Peaking | 3626 Hz | 2.96 | -3.3 dB |
| Peaking | 4596 Hz | 5.27 | 2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Mpow%20H5/Mpow%20H5.png)