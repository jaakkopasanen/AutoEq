# Campfire Audio Polaris sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.4; 23 -11.4; 25 -11.4; 28 -11.4; 31 -11.3; 34 -11.2; 37 -11.2; 41 -11.1; 45 -11.1; 49 -11.0; 54 -10.8; 60 -10.6; 66 -10.5; 72 -10.5; 79 -10.5; 87 -10.5; 96 -10.4; 106 -10.4; 116 -10.4; 128 -10.2; 141 -10.1; 155 -10.0; 170 -9.6; 187 -9.3; 206 -8.9; 227 -8.5; 249 -8.1; 274 -7.7; 302 -7.2; 332 -6.7; 365 -6.3; 402 -5.9; 442 -5.6; 486 -5.3; 535 -5.1; 588 -4.8; 647 -4.6; 712 -4.5; 783 -4.4; 861 -4.5; 947 -5.0; 1042 -6.1; 1146 -7.4; 1261 -8.5; 1387 -9.3; 1526 -9.3; 1678 -8.7; 1846 -8.1; 2031 -7.1; 2234 -5.7; 2457 -4.8; 2703 -2.6; 2973 -0.6; 3270 -0.5; 3597 -1.9; 3957 -3.0; 4353 -2.6; 4788 -3.6; 5267 -7.6; 5793 -8.5; 6373 -4.5; 7010 -4.2; 7711 -8.0; 8482 -9.1; 9330 -7.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.6; 15026 -18.8; 16529 -26.4; 18182 -26.7; 20000 -20.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Polaris sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Polaris sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.36 | -4.9 dB  |
| Peaking | 137 Hz   | 1.27 | -2.6 dB  |
| Peaking | 1668 Hz  | 2.26 | -4.3 dB  |
| Peaking | 3243 Hz  | 1.27 | 6.1 dB   |
| Peaking | 17974 Hz | 1.14 | -23.7 dB |
| Peaking | 675 Hz   | 1.71 | 2.4 dB   |
| Peaking | 4690 Hz  | 5.99 | 1.2 dB   |
| Peaking | 5511 Hz  | 8.28 | -4.4 dB  |
| Peaking | 13272 Hz | 1.69 | 8.2 dB   |
| Peaking | 15775 Hz | 2.05 | -9.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.1 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 2.3 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 16000 Hz | 1.41 | -20.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Campfire%20Audio%20Polaris%20sample%202/Campfire%20Audio%20Polaris%20sample%202.png)