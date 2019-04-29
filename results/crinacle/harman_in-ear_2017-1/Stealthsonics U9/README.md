# Stealthsonics U9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -11.0; 25 -11.0; 28 -10.9; 31 -10.8; 34 -10.6; 37 -10.5; 41 -10.3; 45 -10.2; 49 -10.0; 54 -9.9; 60 -9.7; 66 -9.6; 72 -9.6; 79 -9.6; 87 -9.7; 96 -9.7; 106 -9.7; 116 -9.8; 128 -9.7; 141 -9.7; 155 -9.7; 170 -9.6; 187 -9.6; 206 -9.5; 227 -9.4; 249 -9.3; 274 -9.2; 302 -9.0; 332 -8.9; 365 -8.7; 402 -8.7; 442 -8.8; 486 -8.8; 535 -8.9; 588 -9.0; 647 -9.3; 712 -9.5; 783 -9.9; 861 -10.3; 947 -10.8; 1042 -11.4; 1146 -11.5; 1261 -10.7; 1387 -9.1; 1526 -7.5; 1678 -6.6; 1846 -6.4; 2031 -6.1; 2234 -4.7; 2457 -2.9; 2703 -1.3; 2973 -0.5; 3270 -0.9; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.2; 5793 -3.1; 6373 -2.7; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.9; 15026 -28.1; 16529 -33.1; 18182 -31.2; 20000 -28.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stealthsonics U9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stealthsonics U9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.58 | -4.0 dB  |
| Peaking | 224 Hz   | 0.23 | -3.2 dB  |
| Peaking | 1142 Hz  | 1    | -8.5 dB  |
| Peaking | 8374 Hz  | 0.17 | 23.1 dB  |
| Peaking | 17024 Hz | 0.31 | -43.7 dB |
| Peaking | 2100 Hz  | 3.41 | -2.9 dB  |
| Peaking | 2829 Hz  | 1.03 | 2.1 dB   |
| Peaking | 7782 Hz  | 4.48 | -2.3 dB  |
| Peaking | 12527 Hz | 3.05 | 10.0 dB  |
| Peaking | 18395 Hz | 0.18 | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB  |
| Peaking | 250 Hz   | 1.41 | -2.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 16000 Hz | 1.41 | -31.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Stealthsonics%20U9/Stealthsonics%20U9.png)