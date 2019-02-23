# JBL Free X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.3; 23 -13.4; 25 -13.5; 28 -13.5; 31 -13.5; 34 -13.4; 37 -13.3; 41 -13.1; 45 -12.9; 49 -12.8; 54 -12.6; 60 -12.5; 66 -12.3; 72 -12.2; 79 -12.0; 87 -11.8; 96 -11.5; 106 -11.1; 116 -10.7; 128 -10.5; 141 -10.3; 155 -9.6; 170 -9.0; 187 -8.5; 206 -8.0; 227 -7.7; 249 -7.4; 274 -7.4; 302 -7.3; 332 -7.0; 365 -6.7; 402 -6.6; 442 -6.3; 486 -6.1; 535 -5.8; 588 -5.5; 647 -5.2; 712 -4.9; 783 -4.7; 861 -4.7; 947 -4.9; 1042 -5.2; 1146 -5.5; 1261 -5.5; 1387 -5.4; 1526 -5.1; 1678 -4.9; 1846 -4.9; 2031 -4.9; 2234 -5.1; 2457 -5.8; 2703 -6.5; 2973 -5.9; 3270 -4.0; 3597 -2.3; 3957 -1.2; 4353 -0.7; 4788 -0.5; 5267 -0.9; 5793 -2.3; 6373 -5.2; 7010 -5.4; 7711 -5.4; 8482 -5.6; 9330 -6.1; 10263 -10.6; 11289 -11.9; 12418 -13.0; 13660 -19.8; 15026 -29.1; 16529 -30.6; 18182 -23.2; 20000 -11.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Free X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Free X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.19 | -7.8 dB  |
| Peaking | 803 Hz   | 1.37 | 1.2 dB   |
| Peaking | 4663 Hz  | 1.77 | 7.1 dB   |
| Peaking | 9779 Hz  | 0.74 | 8.4 dB   |
| Peaking | 15976 Hz | 0.71 | -29.5 dB |
| Peaking | 2776 Hz  | 3.76 | -3.4 dB  |
| Peaking | 2782 Hz  | 1.34 | 1.7 dB   |
| Peaking | 6717 Hz  | 5.95 | -1.3 dB  |
| Peaking | 8902 Hz  | 3.9  | 1.1 dB   |
| Peaking | 9941 Hz  | 4.08 | -1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -8.1 dB  |
| Peaking | 62 Hz    | 1.41 | -5.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | -1.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 16000 Hz | 1.41 | -32.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/JBL%20Free%20X/JBL%20Free%20X.png)