# Stealthsonics U2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.2; 23 -10.4; 25 -10.5; 28 -10.7; 31 -10.8; 34 -10.9; 37 -10.9; 41 -11.0; 45 -11.1; 49 -11.2; 54 -11.3; 60 -11.5; 66 -11.6; 72 -11.8; 79 -12.0; 87 -12.2; 96 -12.4; 106 -12.5; 116 -12.6; 128 -12.6; 141 -12.5; 155 -12.4; 170 -12.2; 187 -11.9; 206 -11.5; 227 -11.1; 249 -10.6; 274 -10.0; 302 -9.5; 332 -8.9; 365 -8.2; 402 -7.6; 442 -7.0; 486 -6.3; 535 -5.6; 588 -4.9; 647 -4.2; 712 -3.5; 783 -2.8; 861 -2.3; 947 -1.9; 1042 -2.2; 1146 -3.0; 1261 -3.9; 1387 -4.7; 1526 -5.0; 1678 -4.9; 1846 -4.5; 2031 -3.4; 2234 -1.8; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.1; 3957 -4.1; 4353 -6.6; 4788 -6.5; 5267 -6.3; 5793 -9.6; 6373 -13.5; 7010 -9.5; 7711 -9.1; 8482 -8.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -10.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stealthsonics U2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stealthsonics U2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.28 | -3.8 dB |
| Peaking | 157 Hz  | 0.59 | -4.6 dB |
| Peaking | 862 Hz  | 1.34 | 4.8 dB  |
| Peaking | 2910 Hz | 1.7  | 6.7 dB  |
| Peaking | 6396 Hz | 3.51 | -7.1 dB |
| Peaking | 1544 Hz | 1.4  | 1.2 dB  |
| Peaking | 1589 Hz | 2.47 | -2.1 dB |
| Peaking | 4381 Hz | 5.22 | -4.1 dB |
| Peaking | 4491 Hz | 2.08 | 2.2 dB  |
| Peaking | 8173 Hz | 8.85 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Stealthsonics%20U2/Stealthsonics%20U2.png)