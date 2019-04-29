# Final Audio E4000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.7; 25 -7.3; 28 -7.9; 31 -8.5; 34 -9.0; 37 -9.4; 41 -9.8; 45 -10.1; 49 -10.4; 54 -10.8; 60 -11.1; 66 -11.5; 72 -11.7; 79 -12.0; 87 -12.3; 96 -12.5; 106 -12.8; 116 -12.9; 128 -12.9; 141 -13.0; 155 -12.9; 170 -12.7; 187 -12.5; 206 -12.2; 227 -11.8; 249 -11.4; 274 -11.0; 302 -10.5; 332 -10.0; 365 -9.4; 402 -8.9; 442 -8.5; 486 -8.0; 535 -7.4; 588 -6.9; 647 -6.4; 712 -5.8; 783 -5.3; 861 -5.1; 947 -5.0; 1042 -4.8; 1146 -5.2; 1261 -5.9; 1387 -6.1; 1526 -5.8; 1678 -5.4; 1846 -5.0; 2031 -4.5; 2234 -4.0; 2457 -3.6; 2703 -3.2; 2973 -2.8; 3270 -2.2; 3597 -1.6; 3957 -1.2; 4353 -0.9; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -0.9; 7010 -3.8; 7711 -6.0; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -11.5; 15026 -22.6; 16529 -25.2; 18182 -20.8; 20000 -14.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E4000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E4000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 51 Hz    | 1.05 | -1.3 dB  |
| Peaking | 142 Hz   | 0.45 | -6.5 dB  |
| Peaking | 794 Hz   | 2.4  | 1.7 dB   |
| Peaking | 10196 Hz | 0.27 | 11.5 dB  |
| Peaking | 16423 Hz | 0.66 | -28.4 dB |
| Peaking | 1622 Hz  | 2.43 | -1.2 dB  |
| Peaking | 6274 Hz  | 1.43 | 4.0 dB   |
| Peaking | 7757 Hz  | 1.88 | -5.8 dB  |
| Peaking | 12882 Hz | 2.95 | 5.7 dB   |
| Peaking | 14764 Hz | 4.06 | -4.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB  |
| Peaking | 62 Hz    | 1.41 | -4.1 dB  |
| Peaking | 125 Hz   | 1.41 | -5.7 dB  |
| Peaking | 250 Hz   | 1.41 | -4.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 16000 Hz | 1.41 | -20.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Final%20Audio%20E4000/Final%20Audio%20E4000.png)