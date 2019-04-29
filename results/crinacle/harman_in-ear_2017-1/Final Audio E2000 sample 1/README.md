# Final Audio E2000 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.6; 25 -3.3; 28 -4.1; 31 -4.8; 34 -5.4; 37 -6.0; 41 -6.6; 45 -7.1; 49 -7.6; 54 -8.2; 60 -8.8; 66 -9.3; 72 -9.8; 79 -10.3; 87 -10.8; 96 -11.3; 106 -11.8; 116 -12.1; 128 -12.4; 141 -12.6; 155 -12.8; 170 -12.7; 187 -12.7; 206 -12.5; 227 -12.2; 249 -11.9; 274 -11.5; 302 -11.1; 332 -10.8; 365 -10.2; 402 -9.7; 442 -9.2; 486 -8.7; 535 -8.1; 588 -7.5; 647 -6.9; 712 -6.3; 783 -5.6; 861 -5.3; 947 -5.0; 1042 -4.9; 1146 -4.9; 1261 -5.4; 1387 -5.7; 1526 -5.4; 1678 -4.8; 1846 -3.9; 2031 -3.1; 2234 -2.2; 2457 -1.7; 2703 -1.9; 2973 -1.4; 3270 -0.8; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.0; 5267 -2.9; 5793 -5.2; 6373 -5.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.1; 15026 -24.4; 16529 -24.3; 18182 -18.4; 20000 -18.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E2000 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E2000 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.89 | 5.6 dB   |
| Peaking | 146 Hz   | 0.52 | -6.1 dB  |
| Peaking | 324 Hz   | 1.01 | -1.5 dB  |
| Peaking | 11271 Hz | 0.2  | 18.2 dB  |
| Peaking | 16058 Hz | 0.48 | -35.6 dB |
| Peaking | 900 Hz   | 2.45 | 0.8 dB   |
| Peaking | 1484 Hz  | 2.78 | -2.0 dB  |
| Peaking | 4510 Hz  | 1.1  | 6.7 dB   |
| Peaking | 5681 Hz  | 0.97 | -6.6 dB  |
| Peaking | 12658 Hz | 4.58 | 6.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB   |
| Peaking | 62 Hz    | 1.41 | -2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -4.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 16000 Hz | 1.41 | -20.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Final%20Audio%20E2000%20sample%201/Final%20Audio%20E2000%20sample%201.png)