# Campfire Audio Polaris
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.3; 23 -11.3; 25 -11.2; 28 -11.2; 31 -11.1; 34 -11.1; 37 -11.0; 41 -11.0; 45 -10.9; 49 -10.8; 54 -10.7; 60 -10.6; 66 -10.5; 72 -10.6; 79 -10.5; 87 -10.5; 96 -10.5; 106 -10.5; 116 -10.4; 128 -10.2; 141 -10.1; 155 -10.0; 170 -9.6; 187 -9.3; 206 -8.9; 227 -8.5; 249 -8.1; 274 -7.7; 302 -7.2; 332 -6.7; 365 -6.2; 402 -5.8; 442 -5.5; 486 -5.1; 535 -4.8; 588 -4.5; 647 -4.3; 712 -4.1; 783 -4.0; 861 -4.0; 947 -4.3; 1042 -5.2; 1146 -6.5; 1261 -7.6; 1387 -8.4; 1526 -8.7; 1678 -8.7; 1846 -8.6; 2031 -8.0; 2234 -6.7; 2457 -5.3; 2703 -2.7; 2973 -0.6; 3270 -0.5; 3597 -1.9; 3957 -3.3; 4353 -3.0; 4788 -3.2; 5267 -6.2; 5793 -8.0; 6373 -5.7; 7010 -5.9; 7711 -8.9; 8482 -8.3; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -8.2; 15026 -19.0; 16529 -25.0; 18182 -25.0; 20000 -20.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Polaris GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Polaris ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.22 | -4.8 dB  |
| Peaking | 144 Hz   | 0.95 | -2.2 dB  |
| Peaking | 652 Hz   | 1.78 | 2.8 dB   |
| Peaking | 3359 Hz  | 2.54 | 6.4 dB   |
| Peaking | 18024 Hz | 1.04 | -21.8 dB |
| Peaking | 939 Hz   | 3.17 | 2.1 dB   |
| Peaking | 1651 Hz  | 1.45 | -3.3 dB  |
| Peaking | 2840 Hz  | 5.83 | 2.5 dB   |
| Peaking | 13100 Hz | 1.59 | 7.7 dB   |
| Peaking | 15599 Hz | 2.09 | -9.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB  |
| Peaking | 250 Hz   | 1.41 | -1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 2.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 16000 Hz | 1.41 | -19.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Campfire%20Audio%20Polaris/Campfire%20Audio%20Polaris.png)