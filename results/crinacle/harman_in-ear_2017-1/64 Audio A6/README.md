# 64 Audio A6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.5; 23 -11.6; 25 -11.7; 28 -11.8; 31 -11.8; 34 -11.8; 37 -11.7; 41 -11.6; 45 -11.6; 49 -11.5; 54 -11.4; 60 -11.3; 66 -11.2; 72 -11.1; 79 -11.1; 87 -11.1; 96 -11.0; 106 -11.0; 116 -10.9; 128 -10.8; 141 -10.7; 155 -10.5; 170 -10.3; 187 -10.2; 206 -10.0; 227 -9.8; 249 -9.6; 274 -9.5; 302 -9.4; 332 -9.2; 365 -9.1; 402 -9.1; 442 -9.1; 486 -9.1; 535 -9.0; 588 -8.8; 647 -8.5; 712 -8.1; 783 -7.5; 861 -6.9; 947 -6.5; 1042 -6.4; 1146 -6.6; 1261 -6.7; 1387 -6.6; 1526 -6.2; 1678 -5.7; 1846 -5.3; 2031 -4.8; 2234 -4.0; 2457 -3.0; 2703 -2.2; 2973 -1.5; 3270 -1.1; 3597 -1.6; 3957 -3.0; 4353 -4.4; 4788 -4.6; 5267 -2.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -13.6; 15026 -24.3; 16529 -31.7; 18182 -32.0; 20000 -18.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio A6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio A6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.14 | -5.1 dB  |
| Peaking | 429 Hz   | 0.27 | -2.3 dB  |
| Peaking | 6305 Hz  | 0.39 | 12.3 dB  |
| Peaking | 12422 Hz | 1.89 | 12.2 dB  |
| Peaking | 16938 Hz | 0.41 | -31.4 dB |
| Peaking | 3237 Hz  | 2.96 | 2.4 dB   |
| Peaking | 4707 Hz  | 2.33 | -4.7 dB  |
| Peaking | 5947 Hz  | 2.58 | 4.7 dB   |
| Peaking | 7659 Hz  | 4.09 | -2.3 dB  |
| Peaking | 10116 Hz | 5.67 | 1.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.6 dB  |
| Peaking | 62 Hz    | 1.41 | -3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB  |
| Peaking | 250 Hz   | 1.41 | -2.2 dB  |
| Peaking | 500 Hz   | 1.41 | -2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 16000 Hz | 1.41 | -28.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20A6/64%20Audio%20A6.png)