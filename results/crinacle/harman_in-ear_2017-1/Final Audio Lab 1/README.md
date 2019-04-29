# Final Audio Lab 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -4.0; 25 -4.5; 28 -5.1; 31 -5.6; 34 -6.0; 37 -6.3; 41 -6.8; 45 -7.3; 49 -7.7; 54 -8.1; 60 -8.5; 66 -8.9; 72 -9.4; 79 -9.8; 87 -10.2; 96 -10.7; 106 -11.1; 116 -11.5; 128 -11.7; 141 -11.9; 155 -12.0; 170 -12.1; 187 -12.2; 206 -12.2; 227 -12.1; 249 -11.8; 274 -11.6; 302 -11.3; 332 -10.9; 365 -10.4; 402 -10.0; 442 -9.6; 486 -9.2; 535 -8.6; 588 -8.1; 647 -7.5; 712 -6.8; 783 -6.2; 861 -5.6; 947 -5.3; 1042 -5.4; 1146 -5.7; 1261 -5.9; 1387 -5.6; 1526 -5.0; 1678 -4.3; 1846 -3.6; 2031 -2.9; 2234 -2.7; 2457 -3.6; 2703 -4.7; 2973 -4.9; 3270 -2.8; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.7; 5793 -4.7; 6373 -5.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.6; 16529 -8.9; 18182 -10.6; 20000 -8.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Lab 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Lab 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.77 | 4.1 dB  |
| Peaking | 186 Hz   | 0.42 | -5.9 dB |
| Peaking | 1684 Hz  | 0.51 | 2.4 dB  |
| Peaking | 4388 Hz  | 2.01 | 5.8 dB  |
| Peaking | 18503 Hz | 1.14 | -4.5 dB |
| Peaking | 907 Hz   | 3.11 | 1.0 dB  |
| Peaking | 1322 Hz  | 2.48 | -1.4 dB |
| Peaking | 2229 Hz  | 2.41 | 2.6 dB  |
| Peaking | 2894 Hz  | 2.02 | -2.8 dB |
| Peaking | 3505 Hz  | 5.59 | 2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Final%20Audio%20Lab%201/Final%20Audio%20Lab%201.png)