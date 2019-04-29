# 64 Audio U18Tzar
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -7.0; 25 -7.3; 28 -7.8; 31 -8.2; 34 -8.5; 37 -8.8; 41 -9.1; 45 -9.4; 49 -9.5; 54 -9.7; 60 -10.0; 66 -10.2; 72 -10.5; 79 -10.7; 87 -11.0; 96 -11.2; 106 -11.4; 116 -11.5; 128 -11.6; 141 -11.7; 155 -11.6; 170 -11.5; 187 -11.4; 206 -11.2; 227 -11.0; 249 -10.7; 274 -10.5; 302 -10.1; 332 -9.7; 365 -9.3; 402 -8.9; 442 -8.6; 486 -8.3; 535 -7.9; 588 -7.5; 647 -7.1; 712 -6.7; 783 -6.3; 861 -5.9; 947 -5.9; 1042 -6.1; 1146 -6.6; 1261 -6.9; 1387 -6.9; 1526 -6.5; 1678 -6.0; 1846 -5.5; 2031 -5.2; 2234 -4.9; 2457 -3.2; 2703 -1.6; 2973 -1.7; 3270 -2.2; 3597 -1.7; 3957 -0.5; 4353 -0.5; 4788 -2.0; 5267 -3.1; 5793 -2.5; 6373 -4.5; 7010 -4.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -15.4; 15026 -26.2; 16529 -35.3; 18182 -36.1; 20000 -18.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio U18Tzar GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio U18Tzar ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 47 Hz    | 1.06 | -1.1 dB  |
| Peaking | 149 Hz   | 0.45 | -5.1 dB  |
| Peaking | 4691 Hz  | 0.62 | 12.2 dB  |
| Peaking | 11915 Hz | 1.12 | 17.9 dB  |
| Peaking | 17012 Hz | 0.42 | -36.9 dB |
| Peaking | 891 Hz   | 2.35 | 1.2 dB   |
| Peaking | 1338 Hz  | 2.48 | -1.3 dB  |
| Peaking | 2413 Hz  | 1.89 | -1.5 dB  |
| Peaking | 2687 Hz  | 4.13 | 3.1 dB   |
| Peaking | 18271 Hz | 5.43 | -3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -4.4 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.5 dB   |
| Peaking | 16000 Hz | 1.41 | -32.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20U18Tzar/64%20Audio%20U18Tzar.png)