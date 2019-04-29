# 64 Audio A2e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.5; 25 -4.9; 28 -5.4; 31 -5.8; 34 -6.1; 37 -6.4; 41 -6.7; 45 -7.0; 49 -7.3; 54 -7.6; 60 -8.0; 66 -8.3; 72 -8.7; 79 -9.1; 87 -9.4; 96 -9.9; 106 -10.2; 116 -10.5; 128 -10.8; 141 -11.0; 155 -11.2; 170 -11.3; 187 -11.3; 206 -11.2; 227 -11.1; 249 -11.1; 274 -11.0; 302 -10.8; 332 -10.4; 365 -10.1; 402 -9.7; 442 -9.4; 486 -9.0; 535 -8.6; 588 -8.3; 647 -7.9; 712 -7.4; 783 -6.9; 861 -6.5; 947 -6.3; 1042 -6.4; 1146 -6.7; 1261 -6.8; 1387 -6.4; 1526 -5.6; 1678 -4.9; 1846 -4.6; 2031 -4.5; 2234 -3.8; 2457 -2.5; 2703 -1.2; 2973 -0.6; 3270 -0.9; 3597 -2.0; 3957 -4.0; 4353 -5.4; 4788 -1.3; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.6; 8482 -9.1; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.2; 15026 -21.7; 16529 -16.1; 18182 -6.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio A2e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio A2e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 1    | 3.1 dB   |
| Peaking | 190 Hz   | 0.48 | -5.0 dB  |
| Peaking | 2901 Hz  | 1.78 | 5.8 dB   |
| Peaking | 5726 Hz  | 3.03 | 6.4 dB   |
| Peaking | 15353 Hz | 2.79 | -17.1 dB |
| Peaking | 4262 Hz  | 4.32 | -1.9 dB  |
| Peaking | 8294 Hz  | 4.64 | -4.3 dB  |
| Peaking | 8481 Hz  | 0.5  | 1.3 dB   |
| Peaking | 12924 Hz | 3.85 | 4.2 dB   |
| Peaking | 14134 Hz | 2.86 | -3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.5 dB   |
| Peaking | 62 Hz    | 1.41 | -1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.7 dB  |
| Peaking | 250 Hz   | 1.41 | -4.2 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 16000 Hz | 1.41 | -12.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20A2e/64%20Audio%20A2e.png)