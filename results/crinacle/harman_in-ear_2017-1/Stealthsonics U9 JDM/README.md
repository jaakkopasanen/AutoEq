# Stealthsonics U9 JDM
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.6; 23 -9.7; 25 -9.8; 28 -9.9; 31 -10.0; 34 -10.0; 37 -10.0; 41 -9.9; 45 -9.9; 49 -9.9; 54 -9.8; 60 -9.8; 66 -9.8; 72 -9.8; 79 -9.8; 87 -9.8; 96 -10.0; 106 -10.0; 116 -10.0; 128 -10.0; 141 -9.9; 155 -9.9; 170 -9.7; 187 -9.6; 206 -9.4; 227 -9.2; 249 -9.0; 274 -8.8; 302 -8.5; 332 -8.2; 365 -8.0; 402 -7.9; 442 -7.7; 486 -7.5; 535 -7.3; 588 -7.2; 647 -7.0; 712 -6.8; 783 -6.5; 861 -6.5; 947 -6.7; 1042 -7.2; 1146 -8.1; 1261 -9.0; 1387 -9.6; 1526 -10.0; 1678 -10.4; 1846 -10.2; 2031 -8.9; 2234 -6.8; 2457 -4.7; 2703 -3.4; 2973 -3.0; 3270 -1.9; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.8; 5267 -4.4; 5793 -4.5; 6373 -3.6; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.3; 13660 -21.3; 15026 -33.6; 16529 -38.2; 18182 -37.0; 20000 -32.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stealthsonics U9 JDM GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stealthsonics U9 JDM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 84 Hz    | 0.15 | -3.7 dB  |
| Peaking | 1715 Hz  | 1.39 | -7.5 dB  |
| Peaking | 4064 Hz  | 0.27 | 25.5 dB  |
| Peaking | 11715 Hz | 0.97 | 23.2 dB  |
| Peaking | 15886 Hz | 0.18 | -49.0 dB |
| Peaking | 861 Hz   | 5.05 | 0.5 dB   |
| Peaking | 4813 Hz  | 4.47 | 1.7 dB   |
| Peaking | 5369 Hz  | 5.11 | -3.3 dB  |
| Peaking | 6686 Hz  | 4.72 | 2.0 dB   |
| Peaking | 17931 Hz | 3.14 | -1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB  |
| Peaking | 62 Hz    | 1.41 | -2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB  |
| Peaking | 250 Hz   | 1.41 | -2.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 12.3 dB  |
| Peaking | 16000 Hz | 1.41 | -42.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Stealthsonics%20U9%20JDM/Stealthsonics%20U9%20JDM.png)