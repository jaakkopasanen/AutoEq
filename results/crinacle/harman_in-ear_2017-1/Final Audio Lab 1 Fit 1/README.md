# Final Audio Lab 1 Fit 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.5; 25 -6.6; 28 -6.8; 31 -6.9; 34 -7.0; 37 -7.1; 41 -7.3; 45 -7.5; 49 -7.6; 54 -7.9; 60 -8.2; 66 -8.6; 72 -8.9; 79 -9.3; 87 -9.7; 96 -10.3; 106 -10.8; 116 -11.2; 128 -11.6; 141 -12.1; 155 -12.5; 170 -12.9; 187 -13.2; 206 -13.4; 227 -13.7; 249 -14.0; 274 -14.3; 302 -14.5; 332 -14.6; 365 -15.0; 402 -15.3; 442 -15.8; 486 -16.5; 535 -17.1; 588 -18.1; 647 -18.7; 712 -18.2; 783 -17.3; 861 -16.7; 947 -15.2; 1042 -13.5; 1146 -12.3; 1261 -11.3; 1387 -9.9; 1526 -7.7; 1678 -5.1; 1846 -2.3; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.0; 4788 -2.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -17.2; 16529 -24.7; 18182 -21.1; 20000 -11.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Lab 1 Fit 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Lab 1 Fit 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 168 Hz   | 0.59 | -4.3 dB  |
| Peaking | 730 Hz   | 0.59 | -12.4 dB |
| Peaking | 2059 Hz  | 2.24 | 5.0 dB   |
| Peaking | 3577 Hz  | 0.43 | 7.2 dB   |
| Peaking | 17214 Hz | 1.3  | -20.2 dB |
| Peaking | 3223 Hz  | 2.79 | 0.7 dB   |
| Peaking | 6191 Hz  | 2.99 | 5.4 dB   |
| Peaking | 7055 Hz  | 1.29 | -4.5 dB  |
| Peaking | 13809 Hz | 1.84 | 7.0 dB   |
| Peaking | 15591 Hz | 3.18 | -8.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB   |
| Peaking | 62 Hz    | 1.41 | -0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB  |
| Peaking | 250 Hz   | 1.41 | -5.1 dB  |
| Peaking | 500 Hz   | 1.41 | -9.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -9.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 16000 Hz | 1.41 | -16.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Final%20Audio%20Lab%201%20Fit%201/Final%20Audio%20Lab%201%20Fit%201.png)