# 1MORE Triple Driver
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -7.0; 25 -7.4; 28 -8.0; 31 -8.4; 34 -8.7; 37 -9.0; 41 -9.3; 45 -9.6; 49 -9.8; 54 -10.0; 60 -10.3; 66 -10.6; 72 -10.9; 79 -11.1; 87 -11.4; 96 -11.7; 106 -11.8; 116 -11.9; 128 -12.0; 141 -12.0; 155 -11.9; 170 -11.8; 187 -11.5; 206 -11.2; 227 -10.9; 249 -10.5; 274 -10.0; 302 -9.5; 332 -8.9; 365 -8.3; 402 -7.7; 442 -7.2; 486 -6.7; 535 -6.1; 588 -5.6; 647 -5.1; 712 -4.5; 783 -4.0; 861 -3.6; 947 -3.5; 1042 -3.8; 1146 -4.2; 1261 -4.7; 1387 -5.1; 1526 -5.1; 1678 -5.0; 1846 -5.1; 2031 -5.2; 2234 -5.2; 2457 -5.2; 2703 -4.8; 2973 -3.9; 3270 -3.2; 3597 -3.6; 3957 -5.3; 4353 -7.8; 4788 -7.3; 5267 -3.1; 5793 -0.5; 6373 -0.7; 7010 -4.3; 7711 -5.8; 8482 -6.1; 9330 -6.1; 10263 -6.1; 11289 -6.1; 12418 -6.5; 13660 -14.4; 15026 -24.9; 16529 -31.3; 18182 -32.0; 20000 -27.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Triple Driver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Triple Driver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 97 Hz    | 0.43 | -4.9 dB  |
| Peaking | 230 Hz   | 0.77 | -2.8 dB  |
| Peaking | 3927 Hz  | 0.17 | 13.1 dB  |
| Peaking | 11966 Hz | 0.45 | 23.6 dB  |
| Peaking | 16342 Hz | 0.18 | -45.3 dB |
| Peaking | 885 Hz   | 2.71 | 1.5 dB   |
| Peaking | 3576 Hz  | 2    | 8.0 dB   |
| Peaking | 4480 Hz  | 1.17 | -13.4 dB |
| Peaking | 5862 Hz  | 1.67 | 13.2 dB  |
| Peaking | 7656 Hz  | 1.98 | -3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 8.6 dB   |
| Peaking | 16000 Hz | 1.41 | -30.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/1MORE%20Triple%20Driver/1MORE%20Triple%20Driver.png)