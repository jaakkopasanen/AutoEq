# Bluedio T4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.5; 23 -12.8; 25 -12.2; 28 -11.2; 31 -10.3; 34 -9.3; 37 -8.5; 41 -7.5; 45 -6.7; 49 -6.1; 54 -5.3; 60 -4.7; 66 -4.2; 72 -3.7; 79 -3.3; 87 -3.1; 96 -2.9; 106 -2.7; 116 -2.6; 128 -2.4; 141 -2.2; 155 -1.9; 170 -1.3; 187 -0.5; 206 -0.6; 227 -0.7; 249 -1.0; 274 -1.4; 302 -1.7; 332 -1.6; 365 -1.8; 402 -2.0; 442 -2.3; 486 -2.6; 535 -2.9; 588 -3.0; 647 -1.6; 712 -2.2; 783 -5.7; 861 -7.5; 947 -9.0; 1042 -9.6; 1146 -11.4; 1261 -11.1; 1387 -9.8; 1526 -9.7; 1678 -10.4; 1846 -11.4; 2031 -12.0; 2234 -12.4; 2457 -11.3; 2703 -9.9; 2973 -9.3; 3270 -8.6; 3597 -7.7; 3957 -8.3; 4353 -10.9; 4788 -10.5; 5267 -9.7; 5793 -10.4; 6373 -7.9; 7010 -4.3; 7711 -5.5; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bluedio T4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio T4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.8  | -8.3 dB |
| Peaking | 604 Hz   | 0.09 | 5.1 dB  |
| Peaking | 1114 Hz  | 1.71 | -8.0 dB |
| Peaking | 2176 Hz  | 1.28 | -9.5 dB |
| Peaking | 4939 Hz  | 1.83 | -6.6 dB |
| Peaking | 204 Hz   | 4.69 | 1.1 dB  |
| Peaking | 522 Hz   | 1.63 | -0.9 dB |
| Peaking | 680 Hz   | 8.02 | 3.9 dB  |
| Peaking | 816 Hz   | 5.29 | -1.2 dB |
| Peaking | 11627 Hz | 2.44 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.2 dB |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | 2.8 dB  |
| Peaking | 250 Hz   | 1.41 | 4.1 dB  |
| Peaking | 500 Hz   | 1.41 | 4.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.2 dB |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | -3.1 dB |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bluedio%20T4/Bluedio%20T4.png)