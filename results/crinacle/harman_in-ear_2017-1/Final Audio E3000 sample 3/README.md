# Final Audio E3000 sample 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.4; 25 -5.1; 28 -6.0; 31 -6.7; 34 -7.4; 37 -7.9; 41 -8.5; 45 -8.9; 49 -9.4; 54 -9.9; 60 -10.5; 66 -11.0; 72 -11.5; 79 -12.0; 87 -12.4; 96 -12.9; 106 -13.2; 116 -13.5; 128 -13.6; 141 -13.7; 155 -13.7; 170 -13.7; 187 -13.5; 206 -13.3; 227 -12.9; 249 -12.4; 274 -11.9; 302 -11.7; 332 -11.1; 365 -10.6; 402 -10.0; 442 -9.5; 486 -8.9; 535 -8.3; 588 -7.7; 647 -7.0; 712 -6.3; 783 -5.5; 861 -5.3; 947 -5.0; 1042 -5.0; 1146 -5.6; 1261 -6.0; 1387 -5.9; 1526 -5.4; 1678 -4.7; 1846 -4.0; 2031 -3.5; 2234 -2.9; 2457 -2.4; 2703 -2.1; 2973 -1.7; 3270 -1.1; 3597 -0.9; 3957 -0.8; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.6; 15026 -23.3; 16529 -26.1; 18182 -20.8; 20000 -11.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E3000 sample 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E3000 sample 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 1.59 | 3.7 dB   |
| Peaking | 119 Hz   | 0.52 | -6.4 dB  |
| Peaking | 267 Hz   | 0.87 | -2.6 dB  |
| Peaking | 9178 Hz  | 0.24 | 9.9 dB   |
| Peaking | 16374 Hz | 0.77 | -28.2 dB |
| Peaking | 1456 Hz  | 4.22 | -1.5 dB  |
| Peaking | 6452 Hz  | 1.53 | 3.3 dB   |
| Peaking | 7694 Hz  | 2.07 | -5.6 dB  |
| Peaking | 12728 Hz | 2.89 | 5.8 dB   |
| Peaking | 14689 Hz | 3.91 | -4.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB   |
| Peaking | 62 Hz    | 1.41 | -3.7 dB  |
| Peaking | 125 Hz   | 1.41 | -6.3 dB  |
| Peaking | 250 Hz   | 1.41 | -5.3 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 16000 Hz | 1.41 | -21.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Final%20Audio%20E3000%20sample%203/Final%20Audio%20E3000%20sample%203.png)