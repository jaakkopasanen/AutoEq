# FitEar Monet 17
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.4; 23 -8.6; 25 -8.9; 28 -9.2; 31 -9.5; 34 -9.7; 37 -9.9; 41 -10.1; 45 -10.3; 49 -10.4; 54 -10.6; 60 -10.9; 66 -11.1; 72 -11.5; 79 -11.8; 87 -12.1; 96 -12.5; 106 -12.8; 116 -13.0; 128 -13.2; 141 -13.4; 155 -13.5; 170 -13.4; 187 -13.4; 206 -13.2; 227 -12.9; 249 -12.6; 274 -12.3; 302 -11.8; 332 -11.2; 365 -10.5; 402 -9.9; 442 -9.3; 486 -8.6; 535 -7.9; 588 -7.1; 647 -6.2; 712 -5.4; 783 -4.4; 861 -3.6; 947 -3.0; 1042 -2.7; 1146 -2.5; 1261 -2.3; 1387 -1.8; 1526 -1.1; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.7; 2457 -1.4; 2703 -1.1; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.8; 4788 -5.1; 5267 -9.4; 5793 -9.7; 6373 -7.8; 7010 -5.8; 7711 -6.2; 8482 -6.5; 9330 -7.6; 10263 -11.0; 11289 -7.8; 12418 -6.7; 13660 -13.8; 15026 -21.1; 16529 -19.6; 18182 -13.8; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar Monet 17 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar Monet 17 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 65 Hz    | 0.3  | -3.0 dB  |
| Peaking | 203 Hz   | 0.51 | -5.4 dB  |
| Peaking | 1587 Hz  | 0.69 | 6.1 dB   |
| Peaking | 3538 Hz  | 2.83 | 4.6 dB   |
| Peaking | 15984 Hz | 1.4  | -15.9 dB |
| Peaking | 4360 Hz  | 4.66 | 3.1 dB   |
| Peaking | 5527 Hz  | 3.59 | -5.6 dB  |
| Peaking | 8168 Hz  | 1.52 | 4.7 dB   |
| Peaking | 11031 Hz | 0.97 | -6.8 dB  |
| Peaking | 12270 Hz | 3.12 | 10.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB  |
| Peaking | 125 Hz   | 1.41 | -5.8 dB  |
| Peaking | 250 Hz   | 1.41 | -5.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -15.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FitEar%20Monet%2017/FitEar%20Monet%2017.png)