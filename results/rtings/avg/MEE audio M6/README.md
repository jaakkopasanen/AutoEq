# MEE audio M6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.9; 23 -16.8; 25 -16.6; 28 -16.3; 31 -16.1; 34 -15.8; 37 -15.5; 41 -15.2; 45 -14.9; 49 -14.6; 54 -14.3; 60 -14.0; 66 -13.8; 72 -13.5; 79 -13.3; 87 -13.1; 96 -12.9; 106 -12.7; 116 -12.4; 128 -12.1; 141 -11.7; 155 -11.3; 170 -10.8; 187 -10.3; 206 -9.7; 227 -9.0; 249 -8.4; 274 -7.8; 302 -7.2; 332 -6.6; 365 -5.9; 402 -5.1; 442 -4.3; 486 -3.3; 535 -2.4; 588 -1.8; 647 -1.2; 712 -0.8; 783 -0.6; 861 -0.9; 947 -1.4; 1042 -1.8; 1146 -2.2; 1261 -2.4; 1387 -2.5; 1526 -2.7; 1678 -3.1; 1846 -3.8; 2031 -4.6; 2234 -5.5; 2457 -6.5; 2703 -8.4; 2973 -9.9; 3270 -10.2; 3597 -10.6; 3957 -12.8; 4353 -17.2; 4788 -15.3; 5267 -7.5; 5793 -2.0; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio M6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio M6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 17 Hz   | 0.49 | -8.6 dB  |
| Peaking | 108 Hz  | 0.23 | -6.3 dB  |
| Peaking | 725 Hz  | 0.49 | 7.1 dB   |
| Peaking | 4628 Hz | 1.76 | -17.4 dB |
| Peaking | 5855 Hz | 2.22 | 13.9 dB  |
| Peaking | 1157 Hz | 2.22 | -1.5 dB  |
| Peaking | 1404 Hz | 0.9  | 1.1 dB   |
| Peaking | 2966 Hz | 3.45 | -2.4 dB  |
| Peaking | 3824 Hz | 2.51 | 1.8 dB   |
| Peaking | 4401 Hz | 7.73 | -2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.2 dB |
| Peaking | 62 Hz    | 1.41 | -5.3 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB  |
| Peaking | 250 Hz   | 1.41 | -2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 3.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 4000 Hz  | 1.41 | -8.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 16000 Hz | 1.41 | -0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/MEE%20audio%20M6/MEE%20audio%20M6.png)