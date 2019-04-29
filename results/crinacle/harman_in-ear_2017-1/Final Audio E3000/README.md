# Final Audio E3000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.8; 25 -5.5; 28 -6.3; 31 -7.0; 34 -7.6; 37 -8.1; 41 -8.7; 45 -9.2; 49 -9.6; 54 -10.1; 60 -10.7; 66 -11.1; 72 -11.6; 79 -12.0; 87 -12.4; 96 -12.8; 106 -13.2; 116 -13.4; 128 -13.5; 141 -13.6; 155 -13.6; 170 -13.5; 187 -13.3; 206 -12.9; 227 -12.6; 249 -12.3; 274 -11.9; 302 -11.5; 332 -10.9; 365 -10.3; 402 -9.8; 442 -9.2; 486 -8.7; 535 -8.1; 588 -7.5; 647 -6.9; 712 -6.2; 783 -5.3; 861 -5.1; 947 -5.0; 1042 -5.0; 1146 -5.6; 1261 -6.1; 1387 -6.0; 1526 -5.5; 1678 -4.8; 1846 -4.2; 2031 -3.6; 2234 -2.8; 2457 -2.2; 2703 -2.0; 2973 -1.6; 3270 -1.0; 3597 -0.7; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.9; 6373 -1.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.0; 15026 -22.2; 16529 -24.2; 18182 -20.6; 20000 -17.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E3000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E3000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 1.66 | 3.3 dB   |
| Peaking | 120 Hz   | 0.51 | -6.6 dB  |
| Peaking | 275 Hz   | 1.01 | -2.1 dB  |
| Peaking | 10056 Hz | 0.23 | 12.8 dB  |
| Peaking | 16501 Hz | 0.53 | -28.3 dB |
| Peaking | 883 Hz   | 2.65 | 1.6 dB   |
| Peaking | 1417 Hz  | 1.97 | -1.8 dB  |
| Peaking | 5777 Hz  | 1    | 2.0 dB   |
| Peaking | 7922 Hz  | 2.38 | -4.5 dB  |
| Peaking | 12648 Hz | 5.29 | 5.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB   |
| Peaking | 62 Hz    | 1.41 | -3.8 dB  |
| Peaking | 125 Hz   | 1.41 | -6.2 dB  |
| Peaking | 250 Hz   | 1.41 | -5.2 dB  |
| Peaking | 500 Hz   | 1.41 | -1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 16000 Hz | 1.41 | -20.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Final%20Audio%20E3000/Final%20Audio%20E3000.png)