# Bluedio U Plus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.9; 23 -14.3; 25 -14.7; 28 -15.0; 31 -15.1; 34 -15.1; 37 -15.1; 41 -15.1; 45 -15.2; 49 -15.3; 54 -15.5; 60 -15.7; 66 -15.9; 72 -16.1; 79 -16.3; 87 -16.6; 96 -16.8; 106 -17.1; 116 -17.3; 128 -17.3; 141 -17.1; 155 -16.5; 170 -15.5; 187 -14.1; 206 -12.4; 227 -10.1; 249 -7.3; 274 -5.6; 302 -4.0; 332 -1.5; 365 -0.5; 402 -0.5; 442 -0.5; 486 -0.5; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.5; 783 -0.5; 861 -2.5; 947 -6.3; 1042 -8.8; 1146 -8.9; 1261 -8.3; 1387 -8.4; 1526 -9.1; 1678 -9.9; 1846 -9.8; 2031 -10.7; 2234 -12.3; 2457 -13.3; 2703 -14.1; 2973 -14.3; 3270 -13.5; 3597 -10.9; 3957 -7.8; 4353 -4.3; 4788 -6.5; 5267 -9.3; 5793 -8.1; 6373 -5.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -11.9; 10263 -9.3; 11289 -6.5; 12418 -6.6; 13660 -7.1; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bluedio U Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio U Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.35 | -7.9 dB |
| Peaking | 109 Hz  | 0.94 | -5.6 dB |
| Peaking | 172 Hz  | 1.38 | -6.3 dB |
| Peaking | 437 Hz  | 0.82 | 8.6 dB  |
| Peaking | 2511 Hz | 1.27 | -7.9 dB |
| Peaking | 801 Hz  | 3.71 | 4.2 dB  |
| Peaking | 1046 Hz | 3.11 | -4.4 dB |
| Peaking | 6733 Hz | 9.64 | 4.2 dB  |
| Peaking | 8991 Hz | 1.64 | 2.2 dB  |
| Peaking | 9565 Hz | 5.3  | -8.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -8.4 dB  |
| Peaking | 62 Hz    | 1.41 | -5.9 dB  |
| Peaking | 125 Hz   | 1.41 | -11.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 9.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bluedio%20U%20Plus/Bluedio%20U%20Plus.png)