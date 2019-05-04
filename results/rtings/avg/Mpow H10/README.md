# Mpow H10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -7.0; 25 -7.2; 28 -7.4; 31 -7.6; 34 -7.7; 37 -7.7; 41 -7.8; 45 -7.9; 49 -8.0; 54 -8.2; 60 -8.5; 66 -8.9; 72 -9.1; 79 -9.3; 87 -9.6; 96 -9.7; 106 -9.7; 116 -9.7; 128 -9.6; 141 -9.4; 155 -9.1; 170 -8.7; 187 -8.3; 206 -7.8; 227 -7.4; 249 -7.1; 274 -6.8; 302 -6.6; 332 -6.4; 365 -5.8; 402 -5.0; 442 -4.3; 486 -4.1; 535 -3.8; 588 -2.9; 647 -1.0; 712 -0.5; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.9; 1146 -1.7; 1261 -2.5; 1387 -3.6; 1526 -4.8; 1678 -6.1; 1846 -6.9; 2031 -6.6; 2234 -5.6; 2457 -4.5; 2703 -4.3; 2973 -4.8; 3270 -5.7; 3597 -7.2; 3957 -8.9; 4353 -8.8; 4788 -8.6; 5267 -9.5; 5793 -13.0; 6373 -16.9; 7010 -13.0; 7711 -11.3; 8482 -13.0; 9330 -11.1; 10263 -8.5; 11289 -12.7; 12418 -15.3; 13660 -10.4; 15026 -6.6; 16529 -8.0; 18182 -12.1; 20000 -14.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mpow H10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mpow H10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 108 Hz   | 0.58 | -3.4 dB |
| Peaking | 909 Hz   | 0.84 | 9.4 dB  |
| Peaking | 3061 Hz  | 1.03 | 9.4 dB  |
| Peaking | 4101 Hz  | 0.28 | -9.4 dB |
| Peaking | 19499 Hz | 1.34 | -7.9 dB |
| Peaking | 5138 Hz  | 4.76 | 2.8 dB  |
| Peaking | 6308 Hz  | 7.86 | -5.4 dB |
| Peaking | 10282 Hz | 4.44 | 4.8 dB  |
| Peaking | 12286 Hz | 2.97 | -6.1 dB |
| Peaking | 14964 Hz | 2.64 | 4.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB |
| Peaking | 8000 Hz  | 1.41 | -8.0 dB |
| Peaking | 16000 Hz | 1.41 | -3.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Mpow%20H10/Mpow%20H10.png)