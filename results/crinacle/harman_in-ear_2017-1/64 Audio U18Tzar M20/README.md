# 64 Audio U18Tzar M20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.4; 25 -6.9; 28 -7.4; 31 -7.8; 34 -8.0; 37 -8.3; 41 -8.6; 45 -9.0; 49 -9.3; 54 -9.5; 60 -9.7; 66 -10.0; 72 -10.4; 79 -10.6; 87 -10.9; 96 -11.1; 106 -11.3; 116 -11.6; 128 -11.7; 141 -11.7; 155 -11.6; 170 -11.6; 187 -11.5; 206 -11.4; 227 -11.1; 249 -10.8; 274 -10.5; 302 -10.2; 332 -9.7; 365 -9.3; 402 -8.9; 442 -8.5; 486 -8.2; 535 -7.8; 588 -7.4; 647 -7.0; 712 -6.5; 783 -6.1; 861 -5.7; 947 -5.7; 1042 -6.0; 1146 -6.5; 1261 -6.9; 1387 -6.9; 1526 -6.5; 1678 -6.0; 1846 -5.6; 2031 -5.3; 2234 -5.1; 2457 -2.7; 2703 -1.0; 2973 -0.9; 3270 -1.3; 3597 -1.3; 3957 -0.5; 4353 -0.5; 4788 -1.9; 5267 -2.6; 5793 -0.9; 6373 -2.2; 7010 -4.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -16.1; 15026 -26.7; 16529 -33.2; 18182 -32.3; 20000 -15.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio U18Tzar M20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio U18Tzar M20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 77 Hz    | 0.64 | -2.3 dB  |
| Peaking | 189 Hz   | 0.57 | -4.3 dB  |
| Peaking | 5154 Hz  | 0.61 | 11.4 dB  |
| Peaking | 11994 Hz | 1.56 | 14.4 dB  |
| Peaking | 16800 Hz | 0.49 | -31.9 dB |
| Peaking | 16 Hz    | 2.17 | 1.5 dB   |
| Peaking | 1951 Hz  | 1.58 | -1.8 dB  |
| Peaking | 2764 Hz  | 3.26 | 2.9 dB   |
| Peaking | 5091 Hz  | 8.31 | -2.6 dB  |
| Peaking | 5967 Hz  | 6.43 | 1.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 16000 Hz | 1.41 | -30.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20U18Tzar%20M20/64%20Audio%20U18Tzar%20M20.png)