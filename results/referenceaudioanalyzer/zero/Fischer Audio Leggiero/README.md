# Fischer Audio Leggiero
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -18.3; 23 -18.4; 25 -18.4; 28 -18.4; 31 -18.4; 34 -18.3; 37 -18.2; 41 -18.1; 45 -18.0; 49 -17.9; 54 -17.7; 60 -17.5; 66 -17.2; 72 -17.0; 79 -16.8; 87 -16.4; 96 -16.1; 106 -15.7; 116 -15.2; 128 -14.7; 141 -14.1; 155 -13.5; 170 -13.0; 187 -12.6; 206 -12.3; 227 -11.6; 249 -10.9; 274 -10.4; 302 -9.9; 332 -9.4; 365 -8.8; 402 -8.0; 442 -7.2; 486 -6.3; 535 -5.5; 588 -4.6; 647 -3.7; 712 -2.8; 783 -2.1; 861 -1.3; 947 -0.7; 1042 -0.5; 1146 -0.9; 1261 -1.4; 1387 -1.7; 1526 -1.8; 1678 -1.9; 1846 -2.1; 2031 -2.3; 2234 -2.5; 2457 -2.8; 2703 -2.8; 2973 -2.5; 3270 -1.9; 3597 -1.4; 3957 -1.3; 4353 -1.7; 4788 -2.3; 5267 -5.1; 5793 -9.8; 6373 -10.4; 7010 -5.6; 7711 -5.0; 8482 -5.3; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio Leggiero GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio Leggiero ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 0.1  | -13.0 dB |
| Peaking | 991 Hz  | 0.92 | 5.3 dB   |
| Peaking | 4901 Hz | 0.84 | 5.4 dB   |
| Peaking | 6066 Hz | 3.39 | -10.5 dB |
| Peaking | 9732 Hz | 1.49 | -1.0 dB  |
| Peaking | 156 Hz  | 3.87 | 0.4 dB   |
| Peaking | 354 Hz  | 3.84 | -0.4 dB  |
| Peaking | 1950 Hz | 3.47 | 0.6 dB   |
| Peaking | 2902 Hz | 1.8  | -0.6 dB  |
| Peaking | 3519 Hz | 3.83 | 0.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -13.8 dB |
| Peaking | 62 Hz    | 1.41 | -8.7 dB  |
| Peaking | 125 Hz   | 1.41 | -7.3 dB  |
| Peaking | 250 Hz   | 1.41 | -4.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB  |
| Peaking | 16000 Hz | 1.41 | 0.3 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20Leggiero/Fischer%20Audio%20Leggiero.png)