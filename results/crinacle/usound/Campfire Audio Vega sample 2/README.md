# Campfire Audio Vega sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.5; 23 -11.6; 25 -11.8; 28 -11.9; 31 -12.1; 34 -12.2; 37 -12.2; 41 -12.3; 45 -12.3; 49 -12.4; 54 -12.5; 60 -12.6; 66 -12.7; 72 -12.8; 79 -12.9; 87 -13.1; 96 -13.2; 106 -13.3; 116 -13.3; 128 -13.3; 141 -13.3; 155 -13.1; 170 -12.9; 187 -12.6; 206 -12.2; 227 -11.8; 249 -11.4; 274 -10.9; 302 -10.5; 332 -10.0; 365 -9.5; 402 -9.0; 442 -8.5; 486 -8.1; 535 -7.6; 588 -7.2; 647 -6.7; 712 -6.3; 783 -5.9; 861 -5.7; 947 -5.8; 1042 -6.0; 1146 -6.4; 1261 -7.5; 1387 -7.2; 1526 -6.1; 1678 -5.5; 1846 -4.7; 2031 -3.2; 2234 -1.4; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.1; 5793 -3.9; 6373 -7.5; 7010 -9.6; 7711 -11.4; 8482 -11.0; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Vega sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Vega sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.29 | -5.0 dB |
| Peaking | 171 Hz  | 0.58 | -4.5 dB |
| Peaking | 3924 Hz | 0.77 | 7.4 dB  |
| Peaking | 7598 Hz | 2.39 | -8.3 dB |
| Peaking | 938 Hz  | 1.63 | 1.9 dB  |
| Peaking | 1321 Hz | 1.74 | -2.8 dB |
| Peaking | 2404 Hz | 3.41 | 2.5 dB  |
| Peaking | 4415 Hz | 1.32 | -1.2 dB |
| Peaking | 5062 Hz | 4.81 | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Campfire%20Audio%20Vega%20sample%202/Campfire%20Audio%20Vega%20sample%202.png)