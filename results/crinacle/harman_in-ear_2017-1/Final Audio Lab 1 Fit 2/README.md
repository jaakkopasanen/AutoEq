# Final Audio Lab 1 Fit 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.0; 66 -2.2; 72 -3.3; 79 -4.5; 87 -5.8; 96 -7.1; 106 -8.3; 116 -9.4; 128 -10.4; 141 -11.3; 155 -12.0; 170 -12.4; 187 -12.7; 206 -12.8; 227 -12.8; 249 -12.7; 274 -12.6; 302 -12.4; 332 -12.1; 365 -11.8; 402 -11.7; 442 -11.6; 486 -11.6; 535 -11.6; 588 -11.6; 647 -11.3; 712 -11.2; 783 -11.2; 861 -11.3; 947 -11.2; 1042 -10.8; 1146 -10.4; 1261 -10.3; 1387 -10.3; 1526 -10.2; 1678 -9.6; 1846 -7.8; 2031 -5.2; 2234 -2.3; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -4.4; 4788 -5.7; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.3; 15026 -21.1; 16529 -27.4; 18182 -23.8; 20000 -15.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Lab 1 Fit 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Lab 1 Fit 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 45 Hz    | 0.63 | 10.2 dB  |
| Peaking | 413 Hz   | 0.12 | -7.2 dB  |
| Peaking | 3660 Hz  | 0.54 | 11.2 dB  |
| Peaking | 12941 Hz | 1.03 | 14.9 dB  |
| Peaking | 16367 Hz | 0.63 | -28.6 dB |
| Peaking | 508 Hz   | 1.67 | 1.3 dB   |
| Peaking | 1676 Hz  | 2.11 | -3.4 dB  |
| Peaking | 2386 Hz  | 2.84 | 3.8 dB   |
| Peaking | 4627 Hz  | 6.87 | -6.4 dB  |
| Peaking | 5890 Hz  | 3.63 | 3.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 5.1 dB   |
| Peaking | 125 Hz   | 1.41 | -4.3 dB  |
| Peaking | 250 Hz   | 1.41 | -5.7 dB  |
| Peaking | 500 Hz   | 1.41 | -3.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 16000 Hz | 1.41 | -20.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Final%20Audio%20Lab%201%20Fit%202/Final%20Audio%20Lab%201%20Fit%202.png)