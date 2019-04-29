# Campfire Audio Andromeda
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.8; 25 -6.0; 28 -6.3; 31 -6.5; 34 -6.7; 37 -6.9; 41 -7.0; 45 -7.2; 49 -7.4; 54 -7.7; 60 -7.9; 66 -8.2; 72 -8.6; 79 -8.9; 87 -9.3; 96 -9.7; 106 -10.1; 116 -10.4; 128 -10.7; 141 -10.9; 155 -11.1; 170 -11.2; 187 -11.3; 206 -11.3; 227 -11.3; 249 -11.1; 274 -11.0; 302 -10.8; 332 -10.5; 365 -10.2; 402 -9.9; 442 -9.6; 486 -9.1; 535 -8.7; 588 -8.2; 647 -7.5; 712 -6.9; 783 -6.2; 861 -5.5; 947 -5.1; 1042 -5.1; 1146 -5.5; 1261 -6.0; 1387 -6.3; 1526 -6.1; 1678 -5.6; 1846 -4.9; 2031 -3.9; 2234 -2.6; 2457 -1.2; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.8; 5267 -1.0; 5793 -0.6; 6373 -4.3; 7010 -7.5; 7711 -8.1; 8482 -8.8; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.4; 16529 -9.1; 18182 -7.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Andromeda GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Andromeda ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 197 Hz   | 0.53 | -5.1 dB |
| Peaking | 3291 Hz  | 1.01 | 6.4 dB  |
| Peaking | 5828 Hz  | 3.08 | 6.0 dB  |
| Peaking | 6679 Hz  | 2.58 | -3.2 dB |
| Peaking | 8061 Hz  | 2.2  | -2.6 dB |
| Peaking | 19 Hz    | 1.5  | 1.2 dB  |
| Peaking | 951 Hz   | 1.51 | 4.6 dB  |
| Peaking | 1078 Hz  | 0.76 | -3.1 dB |
| Peaking | 2472 Hz  | 3.81 | 1.5 dB  |
| Peaking | 16566 Hz | 1.96 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Campfire%20Audio%20Andromeda/Campfire%20Audio%20Andromeda.png)