# MEE audio X7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.5; 28 -2.2; 31 -2.7; 34 -3.2; 37 -3.5; 41 -4.0; 45 -4.4; 49 -4.7; 54 -5.0; 60 -5.4; 66 -5.8; 72 -6.1; 79 -6.4; 87 -6.7; 96 -7.0; 106 -7.2; 116 -7.4; 128 -7.5; 141 -7.4; 155 -7.3; 170 -7.1; 187 -6.9; 206 -6.7; 227 -6.4; 249 -6.1; 274 -5.7; 302 -5.2; 332 -4.7; 365 -4.2; 402 -3.6; 442 -3.2; 486 -2.7; 535 -2.0; 588 -1.9; 647 -1.7; 712 -1.3; 783 -1.1; 861 -1.5; 947 -2.1; 1042 -2.5; 1146 -3.0; 1261 -3.4; 1387 -3.7; 1526 -4.0; 1678 -4.4; 1846 -5.1; 2031 -5.7; 2234 -6.2; 2457 -6.7; 2703 -8.2; 2973 -10.3; 3270 -11.9; 3597 -12.5; 3957 -13.7; 4353 -16.8; 4788 -17.8; 5267 -11.8; 5793 -5.9; 6373 -2.7; 7010 -3.4; 7711 -5.5; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -6.7; 15026 -8.1; 16529 -7.8; 18182 -9.6; 20000 -8.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio X7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio X7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 1.58 | 5.2 dB   |
| Peaking | 812 Hz   | 0.86 | 4.9 dB   |
| Peaking | 4694 Hz  | 1.75 | -16.5 dB |
| Peaking | 6166 Hz  | 2.03 | 10.4 dB  |
| Peaking | 18710 Hz | 0.84 | -4.0 dB  |
| Peaking | 144 Hz   | 1.01 | -2.0 dB  |
| Peaking | 462 Hz   | 2.47 | 0.9 dB   |
| Peaking | 2732 Hz  | 1.43 | 1.3 dB   |
| Peaking | 3083 Hz  | 4.2  | -2.7 dB  |
| Peaking | 11878 Hz | 3.64 | 0.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.2 dB   |
| Peaking | 62 Hz    | 1.41 | -0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB  |
| Peaking | 250 Hz   | 1.41 | -0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 3.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 4000 Hz  | 1.41 | -10.6 dB |
| Peaking | 8000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 16000 Hz | 1.41 | -3.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/MEE%20audio%20X7/MEE%20audio%20X7.png)