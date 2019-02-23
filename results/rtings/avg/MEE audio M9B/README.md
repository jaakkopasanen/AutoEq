# MEE audio M9B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.8; 23 -15.4; 25 -14.8; 28 -13.6; 31 -12.5; 34 -11.7; 37 -11.2; 41 -10.7; 45 -10.6; 49 -10.6; 54 -10.6; 60 -10.5; 66 -10.3; 72 -9.9; 79 -9.3; 87 -8.7; 96 -8.3; 106 -8.1; 116 -8.0; 128 -7.9; 141 -7.7; 155 -7.5; 170 -7.2; 187 -6.9; 206 -6.5; 227 -6.0; 249 -5.5; 274 -5.1; 302 -4.6; 332 -4.1; 365 -3.5; 402 -3.0; 442 -2.4; 486 -1.8; 535 -1.3; 588 -0.8; 647 -0.5; 712 -0.5; 783 -0.7; 861 -1.3; 947 -1.8; 1042 -1.9; 1146 -2.0; 1261 -2.0; 1387 -2.0; 1526 -1.9; 1678 -1.9; 1846 -1.9; 2031 -1.8; 2234 -1.3; 2457 -1.1; 2703 -3.0; 2973 -5.9; 3270 -8.8; 3597 -10.0; 3957 -9.2; 4353 -8.5; 4788 -7.7; 5267 -8.1; 5793 -10.7; 6373 -16.2; 7010 -13.6; 7711 -7.6; 8482 -5.2; 9330 -9.3; 10263 -13.0; 11289 -9.4; 12418 -5.2; 13660 -5.4; 15026 -10.0; 16529 -12.3; 18182 -12.1; 20000 -16.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio M9B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio M9B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.79 | -10.5 dB |
| Peaking | 73 Hz    | 0.9  | -3.4 dB  |
| Peaking | 6441 Hz  | 4.11 | -11.3 dB |
| Peaking | 10328 Hz | 5.92 | -6.9 dB  |
| Peaking | 19636 Hz | 0.53 | -10.0 dB |
| Peaking | 660 Hz   | 1.19 | 4.5 dB   |
| Peaking | 2674 Hz  | 1    | 10.0 dB  |
| Peaking | 3394 Hz  | 1.39 | -11.9 dB |
| Peaking | 5260 Hz  | 3.56 | 1.6 dB   |
| Peaking | 8266 Hz  | 9.14 | 3.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 3.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.7 dB |
| Peaking | 8000 Hz  | 1.41 | -4.7 dB |
| Peaking | 16000 Hz | 1.41 | -7.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/MEE%20audio%20M9B/MEE%20audio%20M9B.png)