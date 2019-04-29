# IMR Acoustics R1 Orange
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.5; 25 -2.8; 28 -3.1; 31 -3.2; 34 -3.3; 37 -3.4; 41 -3.6; 45 -3.9; 49 -4.0; 54 -4.1; 60 -4.3; 66 -4.6; 72 -5.0; 79 -5.2; 87 -5.7; 96 -6.4; 106 -6.7; 116 -7.1; 128 -7.3; 141 -7.7; 155 -7.8; 170 -8.1; 187 -8.2; 206 -8.5; 227 -8.4; 249 -8.3; 274 -8.2; 302 -8.1; 332 -7.7; 365 -7.4; 402 -7.0; 442 -6.5; 486 -6.0; 535 -5.4; 588 -4.8; 647 -4.0; 712 -3.1; 783 -2.4; 861 -1.7; 947 -1.2; 1042 -1.1; 1146 -1.4; 1261 -1.8; 1387 -1.9; 1526 -1.7; 1678 -1.3; 1846 -0.8; 2031 -0.5; 2234 -0.5; 2457 -0.6; 2703 -1.0; 2973 -1.6; 3270 -2.1; 3597 -3.4; 3957 -5.5; 4353 -8.0; 4788 -9.4; 5267 -6.8; 5793 -3.2; 6373 -1.5; 7010 -2.1; 7711 -4.2; 8482 -4.5; 9330 -4.5; 10263 -4.5; 11289 -4.5; 12418 -4.5; 13660 -4.5; 15026 -5.0; 16529 -9.7; 18182 -11.5; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`IMR Acoustics R1 Orange GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `IMR Acoustics R1 Orange ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 238 Hz   | 0.63 | -4.3 dB |
| Peaking | 908 Hz   | 1.99 | 2.4 dB  |
| Peaking | 3035 Hz  | 0.43 | 4.3 dB  |
| Peaking | 4588 Hz  | 3.05 | -8.9 dB |
| Peaking | 17928 Hz | 1.4  | -8.0 dB |
| Peaking | 18 Hz    | 1.31 | 2.4 dB  |
| Peaking | 44 Hz    | 1.64 | 0.9 dB  |
| Peaking | 6548 Hz  | 3.82 | 4.6 dB  |
| Peaking | 7122 Hz  | 1.65 | -2.6 dB |
| Peaking | 22010 Hz | 3.31 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.2 dB |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -4.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/IMR%20Acoustics%20R1%20Orange/IMR%20Acoustics%20R1%20Orange.png)