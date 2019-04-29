# Campfire Audio Dorado
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -10.8; 25 -10.8; 28 -10.9; 31 -11.0; 34 -11.0; 37 -11.1; 41 -11.2; 45 -11.3; 49 -11.4; 54 -11.5; 60 -11.6; 66 -11.8; 72 -12.1; 79 -12.3; 87 -12.6; 96 -12.9; 106 -13.1; 116 -13.3; 128 -13.3; 141 -13.4; 155 -13.4; 170 -13.3; 187 -13.2; 206 -12.9; 227 -12.6; 249 -12.2; 274 -11.8; 302 -11.3; 332 -10.9; 365 -10.4; 402 -9.9; 442 -9.4; 486 -9.0; 535 -8.4; 588 -7.9; 647 -7.4; 712 -6.8; 783 -6.3; 861 -5.9; 947 -5.8; 1042 -6.0; 1146 -6.6; 1261 -7.3; 1387 -7.1; 1526 -6.7; 1678 -6.0; 1846 -4.7; 2031 -3.0; 2234 -1.2; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.9; 7010 -6.7; 7711 -10.6; 8482 -7.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Dorado GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Dorado ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.29 | -3.2 dB |
| Peaking | 178 Hz  | 0.5  | -5.6 dB |
| Peaking | 4038 Hz | 0.72 | 7.1 dB  |
| Peaking | 7769 Hz | 4.74 | -7.6 dB |
| Peaking | 18 Hz   | 0.83 | -1.1 dB |
| Peaking | 1518 Hz | 3.16 | -2.2 dB |
| Peaking | 2390 Hz | 3.01 | 2.7 dB  |
| Peaking | 5793 Hz | 0.53 | -1.3 dB |
| Peaking | 6034 Hz | 3.45 | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Campfire%20Audio%20Dorado/Campfire%20Audio%20Dorado.png)