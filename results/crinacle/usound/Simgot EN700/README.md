# Simgot EN700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.0; 34 -1.3; 37 -1.6; 41 -2.0; 45 -2.3; 49 -2.6; 54 -3.0; 60 -3.5; 66 -3.9; 72 -4.3; 79 -4.8; 87 -5.3; 96 -5.8; 106 -6.3; 116 -6.7; 128 -7.1; 141 -7.5; 155 -7.8; 170 -8.0; 187 -8.1; 206 -8.2; 227 -8.1; 249 -8.1; 274 -8.0; 302 -7.8; 332 -7.6; 365 -7.4; 402 -7.1; 442 -6.8; 486 -6.4; 535 -6.1; 588 -5.7; 647 -5.3; 712 -4.8; 783 -4.4; 861 -4.0; 947 -3.8; 1042 -4.0; 1146 -4.7; 1261 -5.5; 1387 -6.0; 1526 -6.3; 1678 -6.3; 1846 -6.5; 2031 -7.1; 2234 -8.2; 2457 -9.5; 2703 -9.7; 2973 -8.6; 3270 -7.5; 3597 -7.1; 3957 -7.5; 4353 -10.8; 4788 -12.9; 5267 -7.4; 5793 -2.5; 6373 -1.0; 7010 -4.0; 7711 -7.5; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Simgot EN700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Simgot EN700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 25 Hz   |  1.2  | 6.2 dB  |
| Peaking | 51 Hz   |  1.9  | 2.7 dB  |
| Peaking | 4662 Hz |  0.75 | -1.9 dB |
| Peaking | 4738 Hz |  6.75 | -6.7 dB |
| Peaking | 6154 Hz |  3.76 | 8.1 dB  |
| Peaking | 228 Hz  |  1.02 | -2.0 dB |
| Peaking | 911 Hz  |  1.46 | 3.0 dB  |
| Peaking | 2585 Hz |  3.99 | -2.9 dB |
| Peaking | 3624 Hz |  4.99 | 1.6 dB  |
| Peaking | 7874 Hz | 12.5  | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Simgot%20EN700/Simgot%20EN700.png)