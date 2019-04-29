# Kumitate KL-Corona sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.1; 28 -1.6; 31 -2.1; 34 -2.7; 37 -3.2; 41 -3.7; 45 -4.0; 49 -4.3; 54 -4.7; 60 -5.2; 66 -5.7; 72 -6.1; 79 -6.5; 87 -6.8; 96 -7.3; 106 -7.7; 116 -7.9; 128 -8.1; 141 -8.3; 155 -8.4; 170 -8.5; 187 -8.4; 206 -8.3; 227 -8.2; 249 -8.1; 274 -7.9; 302 -7.7; 332 -7.5; 365 -7.3; 402 -7.2; 442 -7.0; 486 -6.8; 535 -6.5; 588 -6.3; 647 -6.1; 712 -5.7; 783 -5.4; 861 -5.1; 947 -5.1; 1042 -5.4; 1146 -6.1; 1261 -6.9; 1387 -7.4; 1526 -7.5; 1678 -7.3; 1846 -7.1; 2031 -7.1; 2234 -7.0; 2457 -6.6; 2703 -6.1; 2973 -5.4; 3270 -4.8; 3597 -4.2; 3957 -3.5; 4353 -2.9; 4788 -2.8; 5267 -3.4; 5793 -4.9; 6373 -7.4; 7010 -8.3; 7711 -9.5; 8482 -6.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Corona sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Corona sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 0.42 | 6.5 dB  |
| Peaking | 155 Hz   | 0.61 | -2.4 dB |
| Peaking | 850 Hz   | 3.15 | 1.8 dB  |
| Peaking | 4607 Hz  | 2.12 | 4.3 dB  |
| Peaking | 7369 Hz  | 3.73 | -3.7 dB |
| Peaking | 1044 Hz  | 3.49 | 1.1 dB  |
| Peaking | 1574 Hz  | 1.34 | -1.4 dB |
| Peaking | 3344 Hz  | 4.15 | 0.8 dB  |
| Peaking | 21072 Hz | 1.61 | 0.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kumitate%20KL-Corona%20sample%201/Kumitate%20KL-Corona%20sample%201.png)