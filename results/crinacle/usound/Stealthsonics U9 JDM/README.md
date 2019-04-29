# Stealthsonics U9 JDM
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.4; 23 -8.6; 25 -8.7; 28 -8.8; 31 -8.8; 34 -8.8; 37 -8.8; 41 -8.8; 45 -8.8; 49 -8.7; 54 -8.7; 60 -8.6; 66 -8.6; 72 -8.7; 79 -8.7; 87 -8.7; 96 -8.8; 106 -8.9; 116 -8.8; 128 -8.8; 141 -8.8; 155 -8.7; 170 -8.6; 187 -8.5; 206 -8.3; 227 -8.1; 249 -7.9; 274 -7.7; 302 -7.4; 332 -7.3; 365 -7.1; 402 -7.0; 442 -6.9; 486 -6.8; 535 -6.6; 588 -6.5; 647 -6.3; 712 -6.1; 783 -5.9; 861 -5.8; 947 -5.9; 1042 -6.4; 1146 -7.4; 1261 -8.5; 1387 -9.5; 1526 -10.1; 1678 -10.5; 1846 -10.4; 2031 -9.5; 2234 -7.9; 2457 -6.4; 2703 -5.5; 2973 -5.3; 3270 -4.2; 3597 -0.7; 3957 -0.5; 4353 -0.5; 4788 -1.3; 5267 -5.2; 5793 -5.6; 6373 -5.1; 7010 -6.5; 7711 -7.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.6; 13660 -12.4; 15026 -17.3; 16529 -19.3; 18182 -20.5; 20000 -20.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stealthsonics U9 JDM GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stealthsonics U9 JDM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 62 Hz    |  0.21 | -2.4 dB  |
| Peaking | 911 Hz   |  1.15 | 1.9 dB   |
| Peaking | 1662 Hz  |  1.49 | -5.2 dB  |
| Peaking | 4067 Hz  |  1.76 | 7.2 dB   |
| Peaking | 18589 Hz |  0.67 | -16.2 dB |
| Peaking | 3157 Hz  | 12.82 | -1.3 dB  |
| Peaking | 4762 Hz  |  9.42 | 1.3 dB   |
| Peaking | 5392 Hz  |  7.28 | -2.2 dB  |
| Peaking | 12259 Hz |  1.72 | 5.4 dB   |
| Peaking | 14861 Hz |  1.83 | -5.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 16000 Hz | 1.41 | -15.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Stealthsonics%20U9%20JDM/Stealthsonics%20U9%20JDM.png)