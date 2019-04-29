# Grado iGE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.6; 23 -10.7; 25 -10.7; 28 -10.7; 31 -10.7; 34 -10.6; 37 -10.6; 41 -10.6; 45 -10.6; 49 -10.6; 54 -10.5; 60 -10.4; 66 -10.4; 72 -10.5; 79 -10.6; 87 -10.6; 96 -10.7; 106 -10.7; 116 -10.7; 128 -10.6; 141 -10.5; 155 -10.4; 170 -10.2; 187 -10.0; 206 -9.6; 227 -9.4; 249 -9.0; 274 -8.8; 302 -8.7; 332 -8.4; 365 -8.2; 402 -8.0; 442 -7.8; 486 -7.6; 535 -7.5; 588 -7.4; 647 -7.3; 712 -7.2; 783 -7.2; 861 -7.2; 947 -7.5; 1042 -7.8; 1146 -8.4; 1261 -9.3; 1387 -9.9; 1526 -9.9; 1678 -9.1; 1846 -7.6; 2031 -5.6; 2234 -3.8; 2457 -2.3; 2703 -1.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.6; 6373 -3.0; 7010 -6.9; 7711 -10.3; 8482 -7.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado iGE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado iGE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.5  | -3.6 dB |
| Peaking | 125 Hz   | 0.42 | -3.7 dB |
| Peaking | 1518 Hz  | 1.61 | -6.3 dB |
| Peaking | 3751 Hz  | 0.61 | 7.5 dB  |
| Peaking | 7779 Hz  | 3.83 | -7.4 dB |
| Peaking | 1889 Hz  | 5.63 | -0.4 dB |
| Peaking | 2789 Hz  | 2.47 | 1.1 dB  |
| Peaking | 3655 Hz  | 2.06 | -1.2 dB |
| Peaking | 5779 Hz  | 5.08 | 1.9 dB  |
| Peaking | 11765 Hz | 1.47 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Grado%20iGE/Grado%20iGE.png)