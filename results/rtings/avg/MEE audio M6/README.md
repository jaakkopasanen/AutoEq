# MEE audio M6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.2; 23 -12.0; 25 -11.8; 28 -11.5; 31 -11.3; 34 -11.0; 37 -10.7; 41 -10.4; 45 -10.1; 49 -9.8; 54 -9.6; 60 -9.6; 66 -9.7; 72 -9.6; 79 -9.6; 87 -9.7; 96 -9.8; 106 -10.0; 116 -10.2; 128 -10.4; 141 -10.5; 155 -10.4; 170 -10.2; 187 -10.0; 206 -9.6; 227 -9.2; 249 -8.5; 274 -7.9; 302 -7.3; 332 -6.7; 365 -6.0; 402 -5.2; 442 -4.3; 486 -3.4; 535 -2.4; 588 -1.8; 647 -1.1; 712 -0.7; 783 -0.5; 861 -0.8; 947 -1.3; 1042 -1.7; 1146 -2.1; 1261 -2.3; 1387 -2.4; 1526 -2.6; 1678 -2.9; 1846 -3.5; 2031 -4.2; 2234 -4.7; 2457 -5.7; 2703 -7.9; 2973 -9.9; 3270 -10.5; 3597 -11.0; 3957 -13.1; 4353 -17.7; 4788 -15.4; 5267 -7.4; 5793 -2.0; 6373 -0.5; 7010 -3.3; 7711 -5.5; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio M6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio M6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 0.63 | -5.9 dB  |
| Peaking | 227 Hz  | 0.39 | -6.8 dB  |
| Peaking | 673 Hz  | 0.44 | 8.0 dB   |
| Peaking | 4587 Hz | 1.82 | -18.3 dB |
| Peaking | 5842 Hz | 2.13 | 13.5 dB  |
| Peaking | 1135 Hz | 4.21 | -0.8 dB  |
| Peaking | 2529 Hz | 1.6  | 1.6 dB   |
| Peaking | 2952 Hz | 3.19 | -2.9 dB  |
| Peaking | 3755 Hz | 7.67 | 1.4 dB   |
| Peaking | 7833 Hz | 8.45 | -0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -9.2 dB |
| Peaking | 8000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/MEE%20audio%20M6/MEE%20audio%20M6.png)