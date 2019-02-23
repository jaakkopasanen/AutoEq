# AKG K 550
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.8; 25 -5.2; 28 -5.6; 31 -5.9; 34 -6.1; 37 -6.3; 41 -6.5; 45 -6.5; 49 -6.6; 54 -6.6; 60 -6.6; 66 -6.8; 72 -6.6; 79 -6.0; 87 -4.8; 96 -4.5; 106 -5.9; 116 -7.1; 128 -8.0; 141 -8.2; 155 -7.9; 170 -6.4; 187 -8.1; 206 -8.3; 227 -8.3; 249 -8.4; 274 -8.1; 302 -8.0; 332 -7.8; 365 -7.4; 402 -7.1; 442 -6.9; 486 -6.6; 535 -6.3; 588 -5.8; 647 -5.3; 712 -5.1; 783 -5.0; 861 -6.0; 947 -6.2; 1042 -6.5; 1146 -6.9; 1261 -7.3; 1387 -7.7; 1526 -8.4; 1678 -8.1; 1846 -7.2; 2031 -6.5; 2234 -5.9; 2457 -5.5; 2703 -5.2; 2973 -4.0; 3270 -2.6; 3597 -1.0; 3957 -0.5; 4353 -2.2; 4788 -3.2; 5267 -6.6; 5793 -7.1; 6373 -2.8; 7010 -3.8; 7711 -6.2; 8482 -11.6; 9330 -13.1; 10263 -7.5; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K 550 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K 550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 1.75 | 2.2 dB  |
| Peaking | 236 Hz  | 1.39 | -2.2 dB |
| Peaking | 3803 Hz | 3.01 | 6.4 dB  |
| Peaking | 6730 Hz | 8.2  | 4.8 dB  |
| Peaking | 9068 Hz | 5.03 | -8.2 dB |
| Peaking | 94 Hz   | 5.32 | 2.5 dB  |
| Peaking | 135 Hz  | 4.91 | -1.6 dB |
| Peaking | 719 Hz  | 3    | 1.7 dB  |
| Peaking | 1550 Hz | 2.45 | -2.3 dB |
| Peaking | 2667 Hz | 1.92 | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K550/AKG%20K%20550.png)