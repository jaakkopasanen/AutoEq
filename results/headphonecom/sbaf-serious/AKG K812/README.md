# AKG K812
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -5.2; 25 -5.5; 28 -5.8; 31 -6.0; 34 -6.2; 37 -6.4; 41 -6.6; 45 -6.7; 49 -6.9; 54 -7.0; 60 -7.3; 66 -7.6; 72 -7.6; 79 -7.7; 87 -8.0; 96 -8.2; 106 -8.5; 116 -8.8; 128 -9.0; 141 -9.3; 155 -9.4; 170 -9.3; 187 -9.4; 206 -9.4; 227 -9.4; 249 -9.1; 274 -9.1; 302 -8.7; 332 -8.5; 365 -8.1; 402 -7.9; 442 -7.7; 486 -7.4; 535 -7.0; 588 -6.6; 647 -6.1; 712 -5.6; 783 -5.0; 861 -4.7; 947 -4.4; 1042 -4.0; 1146 -3.2; 1261 -2.9; 1387 -3.4; 1526 -5.1; 1678 -4.7; 1846 -3.6; 2031 -3.8; 2234 -4.4; 2457 -2.4; 2703 -0.5; 2973 -4.4; 3270 -4.7; 3597 -5.7; 3957 -7.3; 4353 -1.9; 4788 -3.9; 5267 -7.7; 5793 -11.0; 6373 -10.7; 7010 -4.5; 7711 -6.1; 8482 -6.9; 9330 -10.1; 10263 -9.6; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -11.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K812 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K812 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 209 Hz  | 0.52 | -3.3 dB |
| Peaking | 1171 Hz | 3.44 | 1.6 dB  |
| Peaking | 2749 Hz | 0.26 | 2.8 dB  |
| Peaking | 5948 Hz | 5.77 | -8.5 dB |
| Peaking | 9720 Hz | 4.26 | -5.8 dB |
| Peaking | 20 Hz   | 1.42 | 1.6 dB  |
| Peaking | 1578 Hz | 9.81 | -1.5 dB |
| Peaking | 2623 Hz | 9.79 | 4.2 dB  |
| Peaking | 3928 Hz | 4.01 | -4.9 dB |
| Peaking | 4398 Hz | 6.75 | 5.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K812/AKG%20K812.png)