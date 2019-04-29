# Campfire Audio Solaris sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -5.8; 25 -6.0; 28 -6.1; 31 -6.3; 34 -6.4; 37 -6.5; 41 -6.6; 45 -6.8; 49 -6.9; 54 -7.1; 60 -7.3; 66 -7.5; 72 -7.8; 79 -8.1; 87 -8.3; 96 -8.7; 106 -9.0; 116 -9.3; 128 -9.6; 141 -9.7; 155 -9.9; 170 -10.0; 187 -10.0; 206 -10.0; 227 -9.9; 249 -9.8; 274 -9.6; 302 -9.5; 332 -9.3; 365 -9.0; 402 -8.8; 442 -8.5; 486 -8.2; 535 -7.9; 588 -7.5; 647 -7.1; 712 -6.8; 783 -6.7; 861 -6.8; 947 -6.7; 1042 -6.5; 1146 -6.6; 1261 -7.0; 1387 -7.3; 1526 -7.7; 1678 -8.2; 1846 -9.2; 2031 -9.7; 2234 -8.3; 2457 -5.6; 2703 -3.7; 2973 -3.6; 3270 -3.6; 3597 -2.0; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.7; 7010 -4.4; 7711 -6.3; 8482 -6.6; 9330 -6.5; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -7.7; 15026 -8.4; 16529 -7.2; 18182 -7.2; 20000 -9.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Solaris sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Solaris sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.47 | 1.1 dB  |
| Peaking | 191 Hz   | 0.53 | -3.7 dB |
| Peaking | 1975 Hz  | 3.21 | -4.5 dB |
| Peaking | 4657 Hz  | 1.06 | 7.5 dB  |
| Peaking | 18560 Hz | 0.07 | -1.5 dB |
| Peaking | 4922 Hz  | 4.85 | -1.0 dB |
| Peaking | 6152 Hz  | 3.04 | 2.2 dB  |
| Peaking | 7665 Hz  | 2.88 | -2.0 dB |
| Peaking | 12021 Hz | 4.11 | 0.9 dB  |
| Peaking | 17529 Hz | 3.73 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Campfire%20Audio%20Solaris%20sample%201/Campfire%20Audio%20Solaris%20sample%201.png)