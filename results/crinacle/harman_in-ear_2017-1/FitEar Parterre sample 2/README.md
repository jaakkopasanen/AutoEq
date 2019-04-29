# FitEar Parterre sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.3; 25 -9.4; 28 -9.6; 31 -9.7; 34 -9.8; 37 -9.9; 41 -10.1; 45 -10.2; 49 -10.4; 54 -10.5; 60 -10.8; 66 -11.0; 72 -11.4; 79 -11.7; 87 -12.0; 96 -12.4; 106 -12.7; 116 -12.9; 128 -13.1; 141 -13.3; 155 -13.4; 170 -13.4; 187 -13.4; 206 -13.3; 227 -13.1; 249 -12.9; 274 -12.6; 302 -12.2; 332 -11.7; 365 -11.2; 402 -10.8; 442 -10.3; 486 -9.8; 535 -9.2; 588 -8.6; 647 -8.0; 712 -7.2; 783 -6.5; 861 -5.8; 947 -5.4; 1042 -5.2; 1146 -5.4; 1261 -5.4; 1387 -4.9; 1526 -4.1; 1678 -3.4; 1846 -2.9; 2031 -2.5; 2234 -1.7; 2457 -0.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.1; 4788 -1.0; 5267 -0.6; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.9; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.9; 15026 -21.1; 16529 -20.7; 18182 -8.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar Parterre sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar Parterre sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 45 Hz    | 0.23 | -2.9 dB  |
| Peaking | 153 Hz   | 0.65 | -4.1 dB  |
| Peaking | 329 Hz   | 0.83 | -3.0 dB  |
| Peaking | 3569 Hz  | 0.57 | 6.6 dB   |
| Peaking | 15829 Hz | 2.24 | -18.4 dB |
| Peaking | 903 Hz   | 5.54 | 0.9 dB   |
| Peaking | 6382 Hz  | 3.41 | 3.8 dB   |
| Peaking | 7595 Hz  | 2.28 | -3.7 dB  |
| Peaking | 13056 Hz | 2.79 | 4.5 dB   |
| Peaking | 14492 Hz | 4.68 | -4.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -5.6 dB  |
| Peaking | 250 Hz   | 1.41 | -5.6 dB  |
| Peaking | 500 Hz   | 1.41 | -2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 16000 Hz | 1.41 | -14.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FitEar%20Parterre%20sample%202/FitEar%20Parterre%20sample%202.png)