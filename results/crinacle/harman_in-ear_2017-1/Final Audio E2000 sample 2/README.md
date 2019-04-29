# Final Audio E2000 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.0; 23 -1.7; 25 -2.4; 28 -3.3; 31 -4.1; 34 -4.7; 37 -5.3; 41 -5.9; 45 -6.4; 49 -6.9; 54 -7.5; 60 -8.1; 66 -8.7; 72 -9.2; 79 -9.7; 87 -10.3; 96 -10.8; 106 -11.3; 116 -11.6; 128 -11.9; 141 -12.2; 155 -12.3; 170 -12.3; 187 -12.3; 206 -12.1; 227 -11.9; 249 -11.6; 274 -11.3; 302 -10.9; 332 -10.2; 365 -9.6; 402 -9.3; 442 -8.9; 486 -8.4; 535 -7.8; 588 -7.3; 647 -6.7; 712 -6.1; 783 -5.5; 861 -4.7; 947 -4.5; 1042 -4.6; 1146 -5.2; 1261 -5.8; 1387 -6.1; 1526 -5.9; 1678 -5.5; 1846 -5.2; 2031 -4.7; 2234 -4.3; 2457 -4.0; 2703 -3.6; 2973 -2.7; 3270 -1.4; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.2; 5793 -3.0; 6373 -5.6; 7010 -4.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.3; 15026 -23.6; 16529 -29.3; 18182 -24.6; 20000 -12.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E2000 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E2000 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.71 | 7.1 dB   |
| Peaking | 164 Hz   | 0.47 | -6.1 dB  |
| Peaking | 864 Hz   | 2.86 | 2.2 dB   |
| Peaking | 10091 Hz | 0.26 | 11.3 dB  |
| Peaking | 16658 Hz | 0.75 | -32.4 dB |
| Peaking | 2148 Hz  | 1.17 | -1.5 dB  |
| Peaking | 4661 Hz  | 1.07 | 4.8 dB   |
| Peaking | 6761 Hz  | 1.1  | -5.1 dB  |
| Peaking | 12907 Hz | 2.38 | 6.7 dB   |
| Peaking | 15008 Hz | 3.41 | -5.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB   |
| Peaking | 62 Hz    | 1.41 | -1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -4.9 dB  |
| Peaking | 250 Hz   | 1.41 | -4.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 16000 Hz | 1.41 | -23.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Final%20Audio%20E2000%20sample%202/Final%20Audio%20E2000%20sample%202.png)