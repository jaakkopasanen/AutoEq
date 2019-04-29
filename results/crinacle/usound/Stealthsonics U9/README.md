# Stealthsonics U9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.9; 23 -9.8; 25 -9.8; 28 -9.7; 31 -9.6; 34 -9.5; 37 -9.3; 41 -9.2; 45 -9.0; 49 -8.9; 54 -8.7; 60 -8.6; 66 -8.5; 72 -8.5; 79 -8.5; 87 -8.5; 96 -8.6; 106 -8.6; 116 -8.6; 128 -8.6; 141 -8.6; 155 -8.6; 170 -8.5; 187 -8.4; 206 -8.3; 227 -8.2; 249 -8.1; 274 -8.0; 302 -7.9; 332 -7.9; 365 -7.9; 402 -7.9; 442 -8.0; 486 -8.1; 535 -8.2; 588 -8.3; 647 -8.6; 712 -8.9; 783 -9.2; 861 -9.6; 947 -10.0; 1042 -10.6; 1146 -10.7; 1261 -10.3; 1387 -9.0; 1526 -7.5; 1678 -6.7; 1846 -6.6; 2031 -6.6; 2234 -5.9; 2457 -4.6; 2703 -3.4; 2973 -2.8; 3270 -3.1; 3597 -2.5; 3957 -0.8; 4353 -0.5; 4788 -0.5; 5267 -3.1; 5793 -4.2; 6373 -4.2; 7010 -5.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -11.7; 16529 -14.3; 18182 -14.8; 20000 -16.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stealthsonics U9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stealthsonics U9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.72 | -2.8 dB |
| Peaking | 139 Hz   | 0.24 | -1.8 dB |
| Peaking | 1077 Hz  | 1.69 | -4.2 dB |
| Peaking | 4114 Hz  | 1.46 | 6.2 dB  |
| Peaking | 2732 Hz  | 6.2  | 1.5 dB  |
| Peaking | 11157 Hz | 0.88 | 3.1 dB  |
| Peaking | 13512 Hz | 3.13 | 4.1 dB  |
| Peaking | 18912 Hz | 0.27 | -4.0 dB |
| Peaking | 19100 Hz | 0.25 | -5.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -4.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -8.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Stealthsonics%20U9/Stealthsonics%20U9.png)