# 64 Audio U18Tzar sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -8.1; 25 -8.3; 28 -8.6; 31 -8.9; 34 -9.2; 37 -9.4; 41 -9.6; 45 -9.7; 49 -9.8; 54 -9.9; 60 -10.1; 66 -10.3; 72 -10.5; 79 -10.7; 87 -10.9; 96 -11.1; 106 -11.3; 116 -11.4; 128 -11.4; 141 -11.5; 155 -11.5; 170 -11.4; 187 -11.2; 206 -11.0; 227 -10.9; 249 -10.6; 274 -10.4; 302 -10.0; 332 -9.6; 365 -9.2; 402 -8.9; 442 -8.5; 486 -8.2; 535 -7.8; 588 -7.4; 647 -7.1; 712 -6.6; 783 -6.2; 861 -5.9; 947 -5.8; 1042 -6.1; 1146 -6.6; 1261 -6.9; 1387 -6.8; 1526 -6.4; 1678 -5.8; 1846 -5.3; 2031 -4.9; 2234 -4.6; 2457 -3.5; 2703 -1.6; 2973 -1.6; 3270 -2.0; 3597 -1.3; 3957 -0.5; 4353 -0.5; 4788 -2.6; 5267 -3.2; 5793 -3.1; 6373 -5.8; 7010 -5.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -15.5; 15026 -25.4; 16529 -35.9; 18182 -37.0; 20000 -15.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio U18Tzar sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio U18Tzar sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 35 Hz    | 1.17 | -0.8 dB  |
| Peaking | 66 Hz    | 0.34 | -1.2 dB  |
| Peaking | 162 Hz   | 0.4  | -4.1 dB  |
| Peaking | 8997 Hz  | 0.31 | 15.0 dB  |
| Peaking | 17259 Hz | 0.65 | -42.1 dB |
| Peaking | 1547 Hz  | 2.08 | -1.9 dB  |
| Peaking | 3970 Hz  | 1.27 | 3.1 dB   |
| Peaking | 7040 Hz  | 1.32 | -3.5 dB  |
| Peaking | 12375 Hz | 2.39 | 7.4 dB   |
| Peaking | 15440 Hz | 1.9  | -5.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 16000 Hz | 1.41 | -32.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20U18Tzar%20sample%201/64%20Audio%20U18Tzar%20sample%201.png)