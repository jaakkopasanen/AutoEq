# Delta Air complimentary earphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -1.2; 128 -3.9; 141 -5.0; 155 -6.4; 170 -7.5; 187 -10.0; 206 -11.1; 227 -12.7; 249 -13.4; 274 -15.5; 302 -17.7; 332 -19.8; 365 -21.7; 402 -23.1; 442 -24.3; 486 -25.7; 535 -27.2; 588 -27.8; 647 -26.7; 712 -24.8; 783 -21.3; 861 -17.8; 947 -16.1; 1042 -12.7; 1146 -10.4; 1261 -8.0; 1387 -5.0; 1526 -1.0; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.9; 2973 -2.7; 3270 -1.4; 3597 -0.7; 3957 -0.8; 4353 -3.7; 4788 -1.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -11.4; 16529 -19.6; 18182 -18.2; 20000 -7.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Delta Air complimentary earphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Delta Air complimentary earphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 104 Hz   | 0.29 | 19.0 dB  |
| Peaking | 573 Hz   | 0.28 | -35.1 dB |
| Peaking | 1610 Hz  | 0.68 | 19.7 dB  |
| Peaking | 4132 Hz  | 0.43 | 9.8 dB   |
| Peaking | 17426 Hz | 1.42 | -15.4 dB |
| Peaking | 23 Hz    | 2.22 | 1.7 dB   |
| Peaking | 6160 Hz  | 2.66 | 6.5 dB   |
| Peaking | 6937 Hz  | 1.26 | -4.8 dB  |
| Peaking | 14349 Hz | 1.87 | 4.9 dB   |
| Peaking | 15765 Hz | 3.38 | -5.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB   |
| Peaking | 62 Hz    | 1.41 | 5.5 dB   |
| Peaking | 125 Hz   | 1.41 | 5.4 dB   |
| Peaking | 250 Hz   | 1.41 | -3.2 dB  |
| Peaking | 500 Hz   | 1.41 | -23.6 dB |
| Peaking | 1000 Hz  | 1.41 | -4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 9.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 16000 Hz | 1.41 | -11.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Delta%20Air%20complimentary%20earphones/Delta%20Air%20complimentary%20earphones.png)