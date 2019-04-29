# Shozy x AAW Hibiki SE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.1; 23 -10.3; 25 -10.4; 28 -10.5; 31 -10.6; 34 -10.7; 37 -10.7; 41 -10.7; 45 -10.6; 49 -10.5; 54 -10.5; 60 -10.5; 66 -10.4; 72 -10.5; 79 -10.5; 87 -10.5; 96 -10.6; 106 -10.7; 116 -10.7; 128 -10.7; 141 -10.7; 155 -10.5; 170 -10.4; 187 -10.1; 206 -9.9; 227 -9.6; 249 -9.2; 274 -8.8; 302 -8.4; 332 -8.0; 365 -7.5; 402 -7.1; 442 -6.6; 486 -6.2; 535 -5.7; 588 -5.3; 647 -4.8; 712 -4.4; 783 -3.7; 861 -3.0; 947 -2.9; 1042 -3.2; 1146 -4.0; 1261 -4.9; 1387 -5.6; 1526 -6.0; 1678 -6.4; 1846 -7.1; 2031 -8.1; 2234 -8.9; 2457 -8.8; 2703 -7.8; 2973 -6.8; 3270 -6.8; 3597 -8.5; 3957 -9.9; 4353 -7.1; 4788 -2.5; 5267 -0.5; 5793 -0.5; 6373 -1.1; 7010 -6.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shozy x AAW Hibiki SE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shozy x AAW Hibiki SE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 65 Hz   | 0.19 | -4.4 dB |
| Peaking | 867 Hz  | 1.04 | 4.0 dB  |
| Peaking | 2247 Hz | 2.42 | -3.1 dB |
| Peaking | 3983 Hz | 5.12 | -5.2 dB |
| Peaking | 5451 Hz | 2.77 | 7.3 dB  |
| Peaking | 66 Hz   | 2.97 | 0.4 dB  |
| Peaking | 419 Hz  | 3.83 | 0.4 dB  |
| Peaking | 1406 Hz | 7.25 | -0.5 dB |
| Peaking | 6399 Hz | 7.69 | 3.8 dB  |
| Peaking | 6943 Hz | 3.18 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Shozy%20x%20AAW%20Hibiki%20SE/Shozy%20x%20AAW%20Hibiki%20SE.png)