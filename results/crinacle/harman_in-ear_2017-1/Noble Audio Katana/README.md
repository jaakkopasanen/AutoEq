# Noble Audio Katana
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.4; 25 -5.7; 28 -6.0; 31 -6.3; 34 -6.5; 37 -6.7; 41 -7.0; 45 -7.2; 49 -7.4; 54 -7.6; 60 -7.9; 66 -8.3; 72 -8.6; 79 -9.0; 87 -9.3; 96 -9.8; 106 -10.2; 116 -10.4; 128 -10.7; 141 -10.9; 155 -11.1; 170 -11.2; 187 -11.2; 206 -11.1; 227 -11.0; 249 -10.8; 274 -10.6; 302 -10.3; 332 -9.9; 365 -9.4; 402 -9.0; 442 -8.7; 486 -8.2; 535 -7.8; 588 -7.4; 647 -7.0; 712 -6.5; 783 -6.1; 861 -5.8; 947 -5.7; 1042 -5.9; 1146 -6.4; 1261 -6.9; 1387 -6.9; 1526 -6.5; 1678 -6.0; 1846 -5.4; 2031 -4.8; 2234 -4.3; 2457 -3.8; 2703 -2.9; 2973 -1.7; 3270 -1.0; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.9; 5793 -6.4; 6373 -5.5; 7010 -4.5; 7711 -6.5; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.0; 15026 -19.7; 16529 -24.7; 18182 -24.9; 20000 -16.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noble Audio Katana GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble Audio Katana ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 1.21 | 1.7 dB   |
| Peaking | 142 Hz   | 0.68 | -4.0 dB  |
| Peaking | 285 Hz   | 1.09 | -2.1 dB  |
| Peaking | 3968 Hz  | 1.04 | 6.6 dB   |
| Peaking | 17783 Hz | 1.05 | -21.6 dB |
| Peaking | 901 Hz   | 2.84 | 1.2 dB   |
| Peaking | 1382 Hz  | 2.62 | -1.3 dB  |
| Peaking | 5850 Hz  | 8.68 | -3.5 dB  |
| Peaking | 12820 Hz | 1.68 | 7.1 dB   |
| Peaking | 15211 Hz | 1.95 | -7.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB   |
| Peaking | 62 Hz    | 1.41 | -1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.7 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 16000 Hz | 1.41 | -19.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Noble%20Audio%20Katana/Noble%20Audio%20Katana.png)