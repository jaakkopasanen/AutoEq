# MEE audio M6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.2; 23 -13.0; 25 -12.9; 28 -12.6; 31 -12.3; 34 -12.0; 37 -11.8; 41 -11.4; 45 -11.1; 49 -10.8; 54 -10.6; 60 -10.6; 66 -10.7; 72 -10.7; 79 -10.7; 87 -10.7; 96 -10.9; 106 -11.1; 116 -11.3; 128 -11.5; 141 -11.5; 155 -11.5; 170 -11.3; 187 -11.0; 206 -10.7; 227 -10.2; 249 -9.6; 274 -9.0; 302 -8.4; 332 -7.8; 365 -7.1; 402 -6.2; 442 -5.4; 486 -4.4; 535 -3.5; 588 -2.9; 647 -2.2; 712 -1.8; 783 -1.5; 861 -1.9; 947 -2.4; 1042 -2.8; 1146 -3.1; 1261 -3.3; 1387 -3.5; 1526 -3.6; 1678 -4.0; 1846 -4.6; 2031 -5.3; 2234 -5.7; 2457 -6.7; 2703 -8.9; 2973 -11.0; 3270 -11.5; 3597 -12.0; 3957 -14.1; 4353 -18.7; 4788 -16.4; 5267 -8.5; 5793 -3.1; 6373 -1.4; 7010 -0.5; 7711 -2.4; 8482 -3.2; 9330 -2.7; 10263 -2.7; 11289 -2.7; 12418 -2.7; 13660 -2.7; 15026 -2.7; 16529 -2.7; 18182 -2.7; 20000 -2.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio M6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio M6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 11 Hz   | 0.86 | -10.2 dB |
| Peaking | 40 Hz   | 0.28 | -7.2 dB  |
| Peaking | 187 Hz  | 0.89 | -5.8 dB  |
| Peaking | 4523 Hz | 1.75 | -21.0 dB |
| Peaking | 6038 Hz | 1.68 | 10.4 dB  |
| Peaking | 356 Hz  | 1.95 | -1.6 dB  |
| Peaking | 732 Hz  | 1.63 | 2.1 dB   |
| Peaking | 3028 Hz | 3.85 | -2.9 dB  |
| Peaking | 3340 Hz | 0.08 | 0.3 dB   |
| Peaking | 3816 Hz | 6.71 | 0.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.7 dB  |
| Peaking | 125 Hz   | 1.41 | -7.2 dB  |
| Peaking | 250 Hz   | 1.41 | -6.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -13.9 dB |
| Peaking | 8000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 16000 Hz | 1.41 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/MEE%20audio%20M6/MEE%20audio%20M6.png)