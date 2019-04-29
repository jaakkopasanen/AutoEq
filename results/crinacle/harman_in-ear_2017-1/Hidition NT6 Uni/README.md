# Hidition NT6 Uni
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.6; 25 -3.0; 28 -3.4; 31 -3.7; 34 -3.9; 37 -4.0; 41 -4.2; 45 -4.4; 49 -4.6; 54 -4.8; 60 -5.0; 66 -5.2; 72 -5.5; 79 -5.8; 87 -6.1; 96 -6.4; 106 -6.8; 116 -7.1; 128 -7.3; 141 -7.5; 155 -7.6; 170 -7.8; 187 -7.9; 206 -8.0; 227 -8.0; 249 -7.9; 274 -7.8; 302 -7.7; 332 -7.5; 365 -7.2; 402 -7.0; 442 -6.9; 486 -6.7; 535 -6.5; 588 -6.3; 647 -6.2; 712 -6.1; 783 -5.9; 861 -5.9; 947 -6.1; 1042 -6.6; 1146 -7.2; 1261 -7.7; 1387 -7.7; 1526 -7.4; 1678 -6.8; 1846 -6.2; 2031 -5.5; 2234 -5.0; 2457 -4.5; 2703 -3.0; 2973 -1.5; 3270 -1.1; 3597 -1.4; 3957 -0.5; 4353 -0.7; 4788 -2.9; 5267 -5.4; 5793 -4.9; 6373 -3.3; 7010 -3.5; 7711 -5.7; 8482 -8.8; 9330 -11.0; 10263 -9.9; 11289 -6.3; 12418 -6.0; 13660 -7.7; 15026 -16.1; 16529 -18.6; 18182 -12.4; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hidition NT6 Uni GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hidition NT6 Uni ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 1.23 | 3.6 dB   |
| Peaking | 3730 Hz  | 1.94 | 5.9 dB   |
| Peaking | 6748 Hz  | 6.2  | 3.3 dB   |
| Peaking | 9325 Hz  | 4.86 | -5.3 dB  |
| Peaking | 16453 Hz | 1.85 | -14.3 dB |
| Peaking | 216 Hz   | 0.89 | -2.2 dB  |
| Peaking | 1389 Hz  | 2.61 | -2.1 dB  |
| Peaking | 2836 Hz  | 7.1  | 1.6 dB   |
| Peaking | 12976 Hz | 3.39 | 3.6 dB   |
| Peaking | 14986 Hz | 4.75 | -3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.9 dB   |
| Peaking | 62 Hz    | 1.41 | 0.7 dB   |
| Peaking | 125 Hz   | 1.41 | -1.3 dB  |
| Peaking | 250 Hz   | 1.41 | -2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.0 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -12.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Hidition%20NT6%20Uni/Hidition%20NT6%20Uni.png)