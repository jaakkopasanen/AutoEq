# Campfire Audio Polaris sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.1; 23 -11.0; 25 -10.9; 28 -10.9; 31 -10.8; 34 -10.8; 37 -10.7; 41 -10.7; 45 -10.6; 49 -10.5; 54 -10.5; 60 -10.4; 66 -10.4; 72 -10.5; 79 -10.4; 87 -10.4; 96 -10.5; 106 -10.4; 116 -10.3; 128 -10.2; 141 -10.0; 155 -9.9; 170 -9.6; 187 -9.2; 206 -8.8; 227 -8.4; 249 -8.0; 274 -7.6; 302 -7.1; 332 -6.5; 365 -6.0; 402 -5.5; 442 -5.2; 486 -4.7; 535 -4.4; 588 -4.1; 647 -3.9; 712 -3.6; 783 -3.4; 861 -3.4; 947 -3.5; 1042 -4.2; 1146 -5.4; 1261 -6.6; 1387 -7.4; 1526 -7.9; 1678 -8.6; 1846 -9.0; 2031 -8.7; 2234 -7.5; 2457 -5.8; 2703 -2.7; 2973 -0.6; 3270 -0.5; 3597 -1.9; 3957 -3.3; 4353 -3.1; 4788 -2.8; 5267 -4.6; 5793 -7.4; 6373 -6.7; 7010 -7.4; 7711 -9.7; 8482 -7.3; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -9.0; 15026 -19.1; 16529 -23.5; 18182 -23.1; 20000 -21.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Polaris sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Polaris sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.2  | -4.7 dB  |
| Peaking | 143 Hz   | 0.9  | -2.3 dB  |
| Peaking | 684 Hz   | 1.65 | 3.2 dB   |
| Peaking | 3366 Hz  | 2.77 | 6.2 dB   |
| Peaking | 18112 Hz | 0.9  | -19.8 dB |
| Peaking | 968 Hz   | 3.94 | 2.0 dB   |
| Peaking | 1864 Hz  | 1.78 | -3.8 dB  |
| Peaking | 2811 Hz  | 5.43 | 2.9 dB   |
| Peaking | 12848 Hz | 1.74 | 7.1 dB   |
| Peaking | 15482 Hz | 2.22 | -8.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.6 dB  |
| Peaking | 250 Hz   | 1.41 | -1.7 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -18.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Campfire%20Audio%20Polaris%20sample%201/Campfire%20Audio%20Polaris%20sample%201.png)