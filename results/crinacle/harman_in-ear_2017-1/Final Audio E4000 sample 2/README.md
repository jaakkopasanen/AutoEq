# Final Audio E4000 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -7.4; 25 -7.9; 28 -8.6; 31 -9.2; 34 -9.6; 37 -10.0; 41 -10.4; 45 -10.7; 49 -11.0; 54 -11.3; 60 -11.7; 66 -12.0; 72 -12.2; 79 -12.5; 87 -12.7; 96 -12.9; 106 -13.2; 116 -13.2; 128 -13.3; 141 -13.3; 155 -13.2; 170 -13.0; 187 -12.8; 206 -12.5; 227 -12.1; 249 -11.6; 274 -11.4; 302 -10.9; 332 -10.3; 365 -9.8; 402 -9.3; 442 -8.8; 486 -8.4; 535 -7.9; 588 -7.4; 647 -6.9; 712 -6.5; 783 -6.0; 861 -5.6; 947 -5.5; 1042 -5.4; 1146 -5.9; 1261 -6.7; 1387 -6.8; 1526 -6.4; 1678 -5.9; 1846 -5.4; 2031 -4.8; 2234 -4.1; 2457 -3.6; 2703 -3.3; 2973 -2.9; 3270 -2.2; 3597 -1.7; 3957 -1.3; 4353 -0.9; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.9; 15026 -23.3; 16529 -27.1; 18182 -21.0; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E4000 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E4000 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 51 Hz    | 0.77 | -2.0 dB  |
| Peaking | 148 Hz   | 0.46 | -6.4 dB  |
| Peaking | 816 Hz   | 2.59 | 1.5 dB   |
| Peaking | 5260 Hz  | 0.62 | 6.4 dB   |
| Peaking | 16664 Hz | 1.34 | -23.2 dB |
| Peaking | 1449 Hz  | 4.1  | -1.3 dB  |
| Peaking | 6471 Hz  | 2.45 | 2.4 dB   |
| Peaking | 7591 Hz  | 2.57 | -4.2 dB  |
| Peaking | 12787 Hz | 2.35 | 6.7 dB   |
| Peaking | 14895 Hz | 3.24 | -6.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.9 dB  |
| Peaking | 250 Hz   | 1.41 | -4.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 16000 Hz | 1.41 | -21.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Final%20Audio%20E4000%20sample%202/Final%20Audio%20E4000%20sample%202.png)