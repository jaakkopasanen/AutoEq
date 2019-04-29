# Campfire Audio Solaris sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.0; 25 -6.1; 28 -6.3; 31 -6.4; 34 -6.5; 37 -6.6; 41 -6.8; 45 -6.9; 49 -7.0; 54 -7.2; 60 -7.4; 66 -7.6; 72 -7.9; 79 -8.2; 87 -8.5; 96 -8.8; 106 -9.1; 116 -9.4; 128 -9.6; 141 -9.8; 155 -9.9; 170 -10.0; 187 -10.0; 206 -10.1; 227 -10.0; 249 -9.8; 274 -9.7; 302 -9.5; 332 -9.3; 365 -9.1; 402 -8.8; 442 -8.6; 486 -8.3; 535 -7.9; 588 -7.6; 647 -7.2; 712 -6.8; 783 -6.6; 861 -6.5; 947 -6.2; 1042 -5.9; 1146 -5.9; 1261 -6.3; 1387 -6.6; 1526 -6.7; 1678 -6.9; 1846 -7.8; 2031 -8.9; 2234 -8.4; 2457 -5.8; 2703 -3.5; 2973 -2.7; 3270 -4.3; 3597 -4.8; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.4; 7010 -4.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.1; 15026 -9.1; 16529 -9.9; 18182 -10.1; 20000 -10.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Solaris sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Solaris sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 158 Hz   | 0.74 | -3.3 dB |
| Peaking | 338 Hz   | 1.3  | -1.6 dB |
| Peaking | 2109 Hz  | 4.21 | -3.5 dB |
| Peaking | 2809 Hz  | 4.88 | 3.1 dB  |
| Peaking | 4911 Hz  | 1.82 | 6.9 dB  |
| Peaking | 18 Hz    | 1.36 | 0.9 dB  |
| Peaking | 1055 Hz  | 3.42 | 0.9 dB  |
| Peaking | 6064 Hz  | 8.9  | 2.2 dB  |
| Peaking | 7901 Hz  | 4.33 | -1.0 dB |
| Peaking | 18870 Hz | 0.58 | -4.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -3.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Campfire%20Audio%20Solaris%20sample%202/Campfire%20Audio%20Solaris%20sample%202.png)