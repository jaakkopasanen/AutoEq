# NCM Bella
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.6; 23 -10.6; 25 -10.6; 28 -10.6; 31 -10.6; 34 -10.5; 37 -10.4; 41 -10.4; 45 -10.3; 49 -10.3; 54 -10.2; 60 -10.1; 66 -10.1; 72 -10.1; 79 -10.1; 87 -10.1; 96 -10.2; 106 -10.1; 116 -10.0; 128 -9.9; 141 -9.8; 155 -9.6; 170 -9.3; 187 -9.1; 206 -8.7; 227 -8.4; 249 -8.0; 274 -7.6; 302 -7.3; 332 -6.9; 365 -6.6; 402 -6.2; 442 -6.0; 486 -5.7; 535 -5.4; 588 -5.1; 647 -4.8; 712 -4.5; 783 -4.2; 861 -4.1; 947 -4.2; 1042 -4.8; 1146 -5.8; 1261 -6.8; 1387 -7.2; 1526 -6.5; 1678 -5.5; 1846 -5.7; 2031 -7.4; 2234 -7.4; 2457 -5.6; 2703 -3.8; 2973 -2.7; 3270 -2.5; 3597 -1.0; 3957 -0.5; 4353 -1.5; 4788 -7.1; 5267 -11.0; 5793 -9.3; 6373 -6.5; 7010 -6.9; 7711 -10.1; 8482 -10.1; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.5; 16529 -8.9; 18182 -9.4; 20000 -8.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NCM Bella GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NCM Bella ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.37 | -4.1 dB |
| Peaking | 134 Hz   | 1.15 | -2.4 dB |
| Peaking | 4061 Hz  | 1.82 | 7.8 dB  |
| Peaking | 5211 Hz  | 4.06 | -8.7 dB |
| Peaking | 8102 Hz  | 5.37 | -5.0 dB |
| Peaking | 845 Hz   | 1.17 | 2.6 dB  |
| Peaking | 1318 Hz  | 4.14 | -2.2 dB |
| Peaking | 2167 Hz  | 5.87 | -2.7 dB |
| Peaking | 2836 Hz  | 6.55 | 1.1 dB  |
| Peaking | 18500 Hz | 0.97 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/NCM%20Bella/NCM%20Bella.png)