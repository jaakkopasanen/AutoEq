# Advanced GT3 Superbassef
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.2; 23 -11.3; 25 -11.4; 28 -11.4; 31 -11.4; 34 -11.3; 37 -11.2; 41 -11.1; 45 -11.0; 49 -10.9; 54 -10.8; 60 -10.7; 66 -10.7; 72 -10.7; 79 -10.8; 87 -10.9; 96 -11.1; 106 -11.2; 116 -11.4; 128 -11.5; 141 -11.6; 155 -11.8; 170 -11.8; 187 -11.9; 206 -11.9; 227 -11.9; 249 -11.8; 274 -11.8; 302 -11.7; 332 -11.5; 365 -11.3; 402 -11.2; 442 -11.0; 486 -10.6; 535 -10.7; 588 -10.3; 647 -9.8; 712 -9.3; 783 -8.8; 861 -8.5; 947 -8.2; 1042 -8.2; 1146 -8.2; 1261 -8.1; 1387 -7.6; 1526 -6.6; 1678 -5.5; 1846 -4.2; 2031 -2.8; 2234 -1.3; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -1.0; 3597 -2.5; 3957 -4.5; 4353 -5.3; 4788 -3.3; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -14.6; 15026 -26.2; 16529 -31.4; 18182 -31.5; 20000 -27.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced GT3 Superbassef GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced GT3 Superbassef ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.72 | -4.1 dB  |
| Peaking | 260 Hz   | 0.21 | -5.2 dB  |
| Peaking | 2627 Hz  | 1.59 | 5.8 dB   |
| Peaking | 9873 Hz  | 0.26 | 24.1 dB  |
| Peaking | 17088 Hz | 0.27 | -41.6 dB |
| Peaking | 4318 Hz  | 4.35 | -4.0 dB  |
| Peaking | 5913 Hz  | 1.73 | 6.3 dB   |
| Peaking | 7877 Hz  | 1.56 | -5.4 dB  |
| Peaking | 12757 Hz | 2.82 | 7.6 dB   |
| Peaking | 14863 Hz | 2.66 | -6.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.1 dB  |
| Peaking | 62 Hz    | 1.41 | -2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | -4.5 dB  |
| Peaking | 500 Hz   | 1.41 | -3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.9 dB   |
| Peaking | 16000 Hz | 1.41 | -30.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Advanced%20GT3%20Superbassef/Advanced%20GT3%20Superbassef.png)