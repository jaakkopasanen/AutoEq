# Final Audio Lab 1 Fit 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.0; 72 -2.1; 79 -3.4; 87 -4.7; 96 -5.9; 106 -7.1; 116 -8.2; 128 -9.2; 141 -10.1; 155 -10.8; 170 -11.3; 187 -11.5; 206 -11.6; 227 -11.6; 249 -11.6; 274 -11.5; 302 -11.3; 332 -11.2; 365 -11.0; 402 -10.9; 442 -10.8; 486 -10.8; 535 -10.9; 588 -10.9; 647 -10.6; 712 -10.5; 783 -10.5; 861 -10.6; 947 -10.4; 1042 -10.0; 1146 -9.6; 1261 -9.8; 1387 -10.2; 1526 -10.3; 1678 -9.7; 1846 -8.0; 2031 -5.7; 2234 -3.4; 2457 -1.4; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.1; 4353 -5.5; 4788 -6.6; 5267 -1.0; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.5; 18182 -7.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Lab 1 Fit 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Lab 1 Fit 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 62 Hz    |  0.36 | 11.3 dB  |
| Peaking | 149 Hz   |  0.46 | -11.1 dB |
| Peaking | 2154 Hz  |  0.38 | -7.1 dB  |
| Peaking | 2902 Hz  |  1.15 | 13.6 dB  |
| Peaking | 6002 Hz  |  3.45 | 7.1 dB   |
| Peaking | 1145 Hz  |  4.19 | 0.9 dB   |
| Peaking | 1603 Hz  |  5.61 | -1.5 dB  |
| Peaking | 3869 Hz  |  7.27 | 2.6 dB   |
| Peaking | 4586 Hz  | 10.37 | -4.0 dB  |
| Peaking | 16941 Hz |  3.25 | -2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 5.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | -4.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Final%20Audio%20Lab%201%20Fit%202/Final%20Audio%20Lab%201%20Fit%202.png)