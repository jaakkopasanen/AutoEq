# Final Audio E2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -2.2; 25 -2.8; 28 -3.7; 31 -4.5; 34 -5.1; 37 -5.6; 41 -6.2; 45 -6.8; 49 -7.3; 54 -7.8; 60 -8.4; 66 -9.0; 72 -9.5; 79 -10.0; 87 -10.5; 96 -11.1; 106 -11.5; 116 -11.9; 128 -12.1; 141 -12.4; 155 -12.5; 170 -12.5; 187 -12.5; 206 -12.3; 227 -12.0; 249 -11.8; 274 -11.4; 302 -11.0; 332 -10.5; 365 -9.9; 402 -9.5; 442 -9.1; 486 -8.5; 535 -8.0; 588 -7.4; 647 -6.8; 712 -6.2; 783 -5.6; 861 -5.0; 947 -4.8; 1042 -4.8; 1146 -5.1; 1261 -5.6; 1387 -5.9; 1526 -5.6; 1678 -5.2; 1846 -4.6; 2031 -3.9; 2234 -3.3; 2457 -2.9; 2703 -2.8; 2973 -2.1; 3270 -1.1; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.7; 5267 -2.0; 5793 -4.1; 6373 -5.5; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.7; 15026 -24.0; 16529 -26.8; 18182 -21.5; 20000 -15.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.92 | 5.9 dB   |
| Peaking | 137 Hz   | 0.59 | -5.5 dB  |
| Peaking | 291 Hz   | 1.02 | -2.1 dB  |
| Peaking | 11035 Hz | 0.22 | 16.1 dB  |
| Peaking | 16344 Hz | 0.54 | -35.1 dB |
| Peaking | 1569 Hz  | 3.48 | -1.6 dB  |
| Peaking | 4394 Hz  | 1.46 | 4.3 dB   |
| Peaking | 6600 Hz  | 0.85 | -3.8 dB  |
| Peaking | 12937 Hz | 2.33 | 6.9 dB   |
| Peaking | 14721 Hz | 3.79 | -6.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.5 dB   |
| Peaking | 62 Hz    | 1.41 | -2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB  |
| Peaking | 250 Hz   | 1.41 | -4.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 16000 Hz | 1.41 | -21.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Final%20Audio%20E2000/Final%20Audio%20E2000.png)