# Campfire Audio Solaris sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -7.1; 25 -7.3; 28 -7.5; 31 -7.6; 34 -7.7; 37 -7.8; 41 -7.9; 45 -8.0; 49 -8.2; 54 -8.3; 60 -8.5; 66 -8.8; 72 -9.0; 79 -9.3; 87 -9.6; 96 -9.9; 106 -10.3; 116 -10.6; 128 -10.8; 141 -10.9; 155 -11.1; 170 -11.1; 187 -11.2; 206 -11.2; 227 -11.1; 249 -11.0; 274 -10.8; 302 -10.6; 332 -10.3; 365 -9.9; 402 -9.7; 442 -9.4; 486 -9.0; 535 -8.6; 588 -8.2; 647 -7.9; 712 -7.5; 783 -7.2; 861 -7.2; 947 -7.0; 1042 -6.7; 1146 -6.7; 1261 -6.8; 1387 -6.7; 1526 -6.6; 1678 -6.8; 1846 -7.6; 2031 -8.4; 2234 -7.2; 2457 -4.1; 2703 -1.4; 2973 -0.5; 3270 -2.0; 3597 -2.9; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.9; 10263 -8.2; 11289 -7.0; 12418 -8.0; 13660 -15.9; 15026 -25.4; 16529 -28.7; 18182 -26.6; 20000 -22.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Solaris sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Solaris sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 74 Hz    | 0.36 | -0.9 dB  |
| Peaking | 205 Hz   | 0.5  | -4.3 dB  |
| Peaking | 4933 Hz  | 0.6  | 16.4 dB  |
| Peaking | 12397 Hz | 0.86 | 20.8 dB  |
| Peaking | 15486 Hz | 0.29 | -34.5 dB |
| Peaking | 1007 Hz  | 1.49 | 0.5 dB   |
| Peaking | 2088 Hz  | 3.96 | -3.4 dB  |
| Peaking | 2833 Hz  | 3.41 | 5.4 dB   |
| Peaking | 3270 Hz  | 1.58 | -1.7 dB  |
| Peaking | 6315 Hz  | 7.12 | 2.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 16000 Hz | 1.41 | -27.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Campfire%20Audio%20Solaris%20sample%202/Campfire%20Audio%20Solaris%20sample%202.png)