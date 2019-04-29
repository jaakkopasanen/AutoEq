# Earsonics ES5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.5; 23 -10.7; 25 -10.9; 28 -11.1; 31 -11.2; 34 -11.3; 37 -11.4; 41 -11.5; 45 -11.6; 49 -11.6; 54 -11.6; 60 -11.7; 66 -11.8; 72 -12.0; 79 -12.1; 87 -12.2; 96 -12.3; 106 -12.3; 116 -12.2; 128 -12.0; 141 -11.9; 155 -11.5; 170 -11.2; 187 -10.8; 206 -10.1; 227 -9.5; 249 -8.9; 274 -8.3; 302 -7.5; 332 -6.7; 365 -6.1; 402 -5.8; 442 -5.5; 486 -5.3; 535 -5.4; 588 -5.6; 647 -6.2; 712 -6.9; 783 -7.8; 861 -8.8; 947 -10.0; 1042 -11.2; 1146 -12.1; 1261 -12.4; 1387 -11.9; 1526 -11.0; 1678 -9.8; 1846 -8.2; 2031 -5.8; 2234 -2.9; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.8; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -5.7; 6373 -6.8; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.1; 15026 -22.9; 16529 -27.4; 18182 -27.6; 20000 -22.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics ES5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics ES5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 43 Hz    | 0.3  | -4.7 dB  |
| Peaking | 153 Hz   | 0.76 | -3.6 dB  |
| Peaking | 1292 Hz  | 0.88 | -17.3 dB |
| Peaking | 5768 Hz  | 0.1  | 15.4 dB  |
| Peaking | 17406 Hz | 0.38 | -33.5 dB |
| Peaking | 1901 Hz  | 3.29 | -3.2 dB  |
| Peaking | 2362 Hz  | 2.01 | 2.7 dB   |
| Peaking | 6156 Hz  | 6.96 | -5.9 dB  |
| Peaking | 12895 Hz | 2.88 | 7.8 dB   |
| Peaking | 15101 Hz | 2.83 | -6.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.0 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB  |
| Peaking | 250 Hz   | 1.41 | -2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 3.7 dB   |
| Peaking | 1000 Hz  | 1.41 | -6.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 16000 Hz | 1.41 | -23.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Earsonics%20ES5/Earsonics%20ES5.png)