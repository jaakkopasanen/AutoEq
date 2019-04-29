# Noble Audio K10 Encore
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -4.0; 25 -4.3; 28 -4.7; 31 -5.0; 34 -5.3; 37 -5.6; 41 -5.8; 45 -6.1; 49 -6.3; 54 -6.6; 60 -6.9; 66 -7.3; 72 -7.6; 79 -8.0; 87 -8.4; 96 -8.9; 106 -9.2; 116 -9.5; 128 -9.8; 141 -10.1; 155 -10.3; 170 -10.3; 187 -10.4; 206 -10.3; 227 -10.2; 249 -10.1; 274 -9.9; 302 -9.6; 332 -9.2; 365 -8.9; 402 -8.5; 442 -8.2; 486 -7.9; 535 -7.6; 588 -7.2; 647 -6.9; 712 -6.4; 783 -6.0; 861 -5.7; 947 -5.6; 1042 -5.9; 1146 -6.4; 1261 -6.8; 1387 -6.7; 1526 -6.3; 1678 -5.7; 1846 -5.1; 2031 -4.5; 2234 -4.1; 2457 -3.8; 2703 -3.0; 2973 -1.5; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.9; 5267 -3.9; 5793 -7.4; 6373 -8.8; 7010 -9.0; 7711 -9.5; 8482 -6.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.5; 15026 -22.1; 16529 -25.7; 18182 -23.0; 20000 -15.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noble Audio K10 Encore GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble Audio K10 Encore ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 10 Hz    | 0.33 | 3.6 dB   |
| Peaking | 185 Hz   | 0.5  | -4.1 dB  |
| Peaking | 7133 Hz  | 1.89 | -11.5 dB |
| Peaking | 8796 Hz  | 0.37 | 14.6 dB  |
| Peaking | 16626 Hz | 0.63 | -26.9 dB |
| Peaking | 1628 Hz  | 1.75 | -1.9 dB  |
| Peaking | 4623 Hz  | 1.21 | 2.5 dB   |
| Peaking | 5783 Hz  | 5.2  | -4.1 dB  |
| Peaking | 12836 Hz | 3.22 | 9.0 dB   |
| Peaking | 13277 Hz | 1.26 | -5.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB   |
| Peaking | 62 Hz    | 1.41 | -0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.0 dB  |
| Peaking | 250 Hz   | 1.41 | -3.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -20.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Noble%20Audio%20K10%20Encore/Noble%20Audio%20K10%20Encore.png)