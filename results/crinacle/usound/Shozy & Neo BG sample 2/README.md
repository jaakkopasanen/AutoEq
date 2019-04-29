# Shozy & Neo BG sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -3.9; 25 -4.3; 28 -4.7; 31 -5.0; 34 -5.2; 37 -5.4; 41 -5.6; 45 -5.9; 49 -6.2; 54 -6.4; 60 -6.6; 66 -6.9; 72 -7.2; 79 -7.5; 87 -7.9; 96 -8.3; 106 -8.7; 116 -9.0; 128 -9.2; 141 -9.4; 155 -9.5; 170 -9.6; 187 -9.7; 206 -9.7; 227 -9.6; 249 -9.4; 274 -9.2; 302 -9.0; 332 -8.7; 365 -8.4; 402 -8.0; 442 -7.7; 486 -7.3; 535 -6.9; 588 -6.4; 647 -6.0; 712 -5.5; 783 -5.0; 861 -4.6; 947 -4.6; 1042 -5.0; 1146 -5.9; 1261 -6.9; 1387 -7.8; 1526 -8.5; 1678 -9.0; 1846 -9.3; 2031 -7.8; 2234 -5.0; 2457 -2.4; 2703 -1.4; 2973 -2.3; 3270 -4.1; 3597 -3.5; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -2.0; 5793 -5.6; 6373 -9.0; 7010 -8.2; 7711 -10.1; 8482 -8.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.4; 18182 -8.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shozy & Neo BG sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shozy & Neo BG sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.68 | 3.5 dB  |
| Peaking | 174 Hz   | 0.75 | -3.5 dB |
| Peaking | 2690 Hz  | 5.59 | 4.9 dB  |
| Peaking | 4610 Hz  | 2.19 | 7.7 dB  |
| Peaking | 6990 Hz  | 1.96 | -4.5 dB |
| Peaking | 905 Hz   | 2.1  | 2.7 dB  |
| Peaking | 1807 Hz  | 1.98 | -4.1 dB |
| Peaking | 2341 Hz  | 3.58 | 2.7 dB  |
| Peaking | 9747 Hz  | 5.21 | 1.0 dB  |
| Peaking | 17981 Hz | 2.38 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Shozy%20&%20Neo%20BG%20sample%202/Shozy%20&%20Neo%20BG%20sample%202.png)