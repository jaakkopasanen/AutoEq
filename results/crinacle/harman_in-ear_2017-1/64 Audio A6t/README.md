# 64 Audio A6t
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -11.8; 25 -11.9; 28 -12.1; 31 -12.2; 34 -12.2; 37 -12.2; 41 -12.2; 45 -12.2; 49 -12.1; 54 -12.1; 60 -12.0; 66 -12.0; 72 -12.0; 79 -11.9; 87 -11.9; 96 -12.0; 106 -11.9; 116 -11.8; 128 -11.7; 141 -11.6; 155 -11.4; 170 -11.3; 187 -11.1; 206 -10.8; 227 -10.6; 249 -10.3; 274 -10.2; 302 -9.9; 332 -9.7; 365 -9.5; 402 -9.3; 442 -9.2; 486 -9.1; 535 -8.8; 588 -8.5; 647 -8.1; 712 -7.5; 783 -6.9; 861 -6.4; 947 -6.0; 1042 -5.9; 1146 -6.2; 1261 -6.3; 1387 -6.1; 1526 -5.7; 1678 -5.4; 1846 -5.1; 2031 -4.9; 2234 -4.2; 2457 -3.3; 2703 -2.4; 2973 -1.7; 3270 -0.8; 3597 -0.5; 3957 -1.0; 4353 -2.2; 4788 -3.1; 5267 -1.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -13.9; 15026 -26.0; 16529 -34.1; 18182 -34.1; 20000 -18.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio A6t GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio A6t ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.1  | -5.6 dB  |
| Peaking | 5554 Hz  | 0.54 | 12.5 dB  |
| Peaking | 11538 Hz | 1.62 | 10.1 dB  |
| Peaking | 13074 Hz | 4.21 | 7.9 dB   |
| Peaking | 17077 Hz | 0.43 | -32.6 dB |
| Peaking | 1896 Hz  | 1.96 | -1.0 dB  |
| Peaking | 3549 Hz  | 1.85 | 2.5 dB   |
| Peaking | 4801 Hz  | 2.27 | -3.7 dB  |
| Peaking | 5848 Hz  | 4.06 | 3.1 dB   |
| Peaking | 15436 Hz | 6.77 | -1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB  |
| Peaking | 62 Hz    | 1.41 | -4.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB  |
| Peaking | 250 Hz   | 1.41 | -2.9 dB  |
| Peaking | 500 Hz   | 1.41 | -2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.8 dB   |
| Peaking | 16000 Hz | 1.41 | -31.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20A6t/64%20Audio%20A6t.png)