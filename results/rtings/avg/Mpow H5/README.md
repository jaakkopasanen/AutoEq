# Mpow H5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -1.8; 28 -2.6; 31 -3.3; 34 -3.8; 37 -4.2; 41 -4.6; 45 -5.0; 49 -5.4; 54 -5.8; 60 -6.3; 66 -6.8; 72 -7.3; 79 -7.9; 87 -8.4; 96 -9.0; 106 -9.4; 116 -9.8; 128 -10.2; 141 -10.5; 155 -10.7; 170 -10.7; 187 -10.6; 206 -10.5; 227 -10.4; 249 -10.2; 274 -9.9; 302 -9.8; 332 -9.9; 365 -9.7; 402 -9.2; 442 -8.2; 486 -6.9; 535 -5.4; 588 -4.3; 647 -3.3; 712 -2.6; 783 -1.8; 861 -0.8; 947 -0.8; 1042 -0.8; 1146 -2.2; 1261 -4.1; 1387 -5.8; 1526 -6.6; 1678 -6.6; 1846 -6.6; 2031 -6.9; 2234 -6.4; 2457 -5.7; 2703 -5.7; 2973 -6.6; 3270 -7.8; 3597 -8.9; 3957 -7.4; 4353 -4.8; 4788 -4.0; 5267 -4.1; 5793 -1.3; 6373 -1.9; 7010 -6.2; 7711 -8.5; 8482 -10.5; 9330 -11.6; 10263 -11.5; 11289 -9.9; 12418 -6.9; 13660 -6.8; 15026 -7.8; 16529 -8.8; 18182 -7.9; 20000 -9.2
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
| Peaking | 11 Hz   | 0.34 | 7.5 dB  |
| Peaking | 195 Hz  | 0.43 | -4.4 dB |
| Peaking | 850 Hz  | 1.43 | 7.4 dB  |
| Peaking | 6009 Hz | 3.32 | 7.2 dB  |
| Peaking | 9336 Hz | 1.71 | -5.6 dB |
| Peaking | 1054 Hz | 6.23 | 1.7 dB  |
| Peaking | 1223 Hz | 4.2  | 1.4 dB  |
| Peaking | 1385 Hz | 1.77 | -1.9 dB |
| Peaking | 3601 Hz | 4.03 | -5.6 dB |
| Peaking | 3718 Hz | 1.76 | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Mpow%20H5/Mpow%20H5.png)