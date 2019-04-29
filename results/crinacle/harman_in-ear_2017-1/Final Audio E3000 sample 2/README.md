# Final Audio E3000 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -5.2; 25 -5.9; 28 -6.7; 31 -7.3; 34 -7.9; 37 -8.4; 41 -8.9; 45 -9.4; 49 -9.8; 54 -10.3; 60 -10.8; 66 -11.3; 72 -11.6; 79 -12.0; 87 -12.4; 96 -12.8; 106 -13.1; 116 -13.3; 128 -13.4; 141 -13.4; 155 -13.4; 170 -13.3; 187 -13.0; 206 -12.6; 227 -12.4; 249 -12.2; 274 -11.9; 302 -11.3; 332 -10.7; 365 -10.1; 402 -9.5; 442 -9.0; 486 -8.4; 535 -7.9; 588 -7.3; 647 -6.7; 712 -6.1; 783 -5.0; 861 -4.9; 947 -4.9; 1042 -5.1; 1146 -5.6; 1261 -6.1; 1387 -6.2; 1526 -5.6; 1678 -5.0; 1846 -4.5; 2031 -3.7; 2234 -2.8; 2457 -2.0; 2703 -2.0; 2973 -1.5; 3270 -0.9; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.9; 5793 -1.7; 6373 -2.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.3; 15026 -21.2; 16529 -22.2; 18182 -20.3; 20000 -23.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E3000 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E3000 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 1.77 | 3.0 dB   |
| Peaking | 116 Hz   | 0.48 | -6.5 dB  |
| Peaking | 272 Hz   | 1.09 | -2.1 dB  |
| Peaking | 9595 Hz  | 0.24 | 12.7 dB  |
| Peaking | 16953 Hz | 0.36 | -24.6 dB |
| Peaking | 870 Hz   | 2.45 | 1.8 dB   |
| Peaking | 1445 Hz  | 1.67 | -2.1 dB  |
| Peaking | 4253 Hz  | 1    | 1.4 dB   |
| Peaking | 7944 Hz  | 2.82 | -3.4 dB  |
| Peaking | 12683 Hz | 5.07 | 5.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB   |
| Peaking | 62 Hz    | 1.41 | -3.9 dB  |
| Peaking | 125 Hz   | 1.41 | -6.0 dB  |
| Peaking | 250 Hz   | 1.41 | -5.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 16000 Hz | 1.41 | -18.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Final%20Audio%20E3000%20sample%202/Final%20Audio%20E3000%20sample%202.png)