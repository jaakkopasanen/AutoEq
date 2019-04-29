# Campfire Audio Solaris sample 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -6.9; 25 -7.0; 28 -7.2; 31 -7.3; 34 -7.4; 37 -7.4; 41 -7.5; 45 -7.6; 49 -7.7; 54 -7.8; 60 -8.0; 66 -8.2; 72 -8.4; 79 -8.6; 87 -8.8; 96 -9.1; 106 -9.4; 116 -9.6; 128 -9.8; 141 -9.8; 155 -9.9; 170 -9.9; 187 -9.9; 206 -9.8; 227 -9.7; 249 -9.5; 274 -9.3; 302 -9.1; 332 -9.0; 365 -8.7; 402 -8.5; 442 -8.4; 486 -8.2; 535 -8.0; 588 -7.9; 647 -7.7; 712 -7.6; 783 -7.3; 861 -7.0; 947 -6.6; 1042 -6.3; 1146 -6.2; 1261 -6.2; 1387 -5.9; 1526 -5.5; 1678 -5.1; 1846 -5.3; 2031 -6.4; 2234 -7.3; 2457 -6.5; 2703 -4.4; 2973 -3.3; 3270 -3.6; 3597 -1.6; 3957 -0.5; 4353 -0.5; 4788 -1.2; 5267 -0.7; 5793 -0.7; 6373 -3.8; 7010 -6.3; 7711 -7.9; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.7; 16529 -12.8; 18182 -13.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Solaris sample 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Solaris sample 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 152 Hz   | 1.05 | -0.5 dB |
| Peaking | 179 Hz   | 0.38 | -2.9 dB |
| Peaking | 1539 Hz  | 3.39 | 1.0 dB  |
| Peaking | 4484 Hz  | 1.6  | 6.7 dB  |
| Peaking | 17614 Hz | 1.43 | -8.3 dB |
| Peaking | 2312 Hz  | 4.3  | -4.0 dB |
| Peaking | 2419 Hz  | 1.97 | 2.0 dB  |
| Peaking | 5811 Hz  | 8.02 | 2.7 dB  |
| Peaking | 7493 Hz  | 4.54 | -2.8 dB |
| Peaking | 13562 Hz | 3.65 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -5.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Campfire%20Audio%20Solaris%20sample%203/Campfire%20Audio%20Solaris%20sample%203.png)