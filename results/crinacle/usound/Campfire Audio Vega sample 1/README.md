# Campfire Audio Vega sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.3; 23 -12.4; 25 -12.5; 28 -12.5; 31 -12.4; 34 -12.4; 37 -12.4; 41 -12.5; 45 -12.5; 49 -12.5; 54 -12.5; 60 -12.5; 66 -12.6; 72 -12.7; 79 -12.9; 87 -13.0; 96 -13.1; 106 -13.2; 116 -13.2; 128 -13.1; 141 -13.0; 155 -12.9; 170 -12.7; 187 -12.4; 206 -12.0; 227 -11.6; 249 -11.2; 274 -10.8; 302 -10.3; 332 -9.8; 365 -9.3; 402 -8.8; 442 -8.3; 486 -7.9; 535 -7.5; 588 -7.0; 647 -6.6; 712 -6.2; 783 -5.8; 861 -5.6; 947 -5.7; 1042 -5.8; 1146 -6.3; 1261 -7.3; 1387 -7.0; 1526 -6.5; 1678 -6.0; 1846 -5.0; 2031 -3.3; 2234 -1.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.6; 5267 -2.4; 5793 -3.7; 6373 -5.7; 7010 -6.8; 7711 -9.2; 8482 -11.2; 9330 -8.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Vega sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Vega sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.18 | -5.7 dB |
| Peaking | 172 Hz   | 0.69 | -3.8 dB |
| Peaking | 2524 Hz  | 2.67 | 4.5 dB  |
| Peaking | 4164 Hz  | 1.31 | 6.1 dB  |
| Peaking | 8299 Hz  | 3.32 | -5.9 dB |
| Peaking | 832 Hz   | 2.18 | 1.7 dB  |
| Peaking | 1085 Hz  | 4.2  | 1.4 dB  |
| Peaking | 1237 Hz  | 1.57 | -2.0 dB |
| Peaking | 2156 Hz  | 6.04 | 1.0 dB  |
| Peaking | 22049 Hz | 1.65 | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Campfire%20Audio%20Vega%20sample%201/Campfire%20Audio%20Vega%20sample%201.png)