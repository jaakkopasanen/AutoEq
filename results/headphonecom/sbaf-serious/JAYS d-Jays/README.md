# JAYS d-Jays
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.5; 25 -2.8; 28 -3.1; 31 -3.3; 34 -3.6; 37 -3.8; 41 -4.0; 45 -4.3; 49 -4.6; 54 -4.9; 60 -5.3; 66 -5.7; 72 -6.0; 79 -6.5; 87 -6.8; 96 -7.1; 106 -7.4; 116 -7.6; 128 -7.9; 141 -8.4; 155 -8.7; 170 -8.9; 187 -9.0; 206 -8.8; 227 -8.9; 249 -9.1; 274 -9.4; 302 -9.2; 332 -8.9; 365 -8.7; 402 -8.4; 442 -8.3; 486 -8.2; 535 -8.0; 588 -7.8; 647 -7.4; 712 -7.3; 783 -7.2; 861 -7.3; 947 -7.6; 1042 -8.1; 1146 -8.4; 1261 -8.9; 1387 -9.5; 1526 -10.2; 1678 -10.9; 1846 -11.9; 2031 -12.3; 2234 -12.0; 2457 -10.1; 2703 -6.4; 2973 -1.9; 3270 -0.5; 3597 -0.8; 3957 -2.4; 4353 -5.2; 4788 -6.5; 5267 -3.2; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JAYS d-Jays GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JAYS d-Jays ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.38 | 4.4 dB  |
| Peaking | 216 Hz  | 0.6  | -2.8 dB |
| Peaking | 2174 Hz | 1.31 | -7.9 dB |
| Peaking | 3222 Hz | 2.47 | 10.2 dB |
| Peaking | 6005 Hz | 4.33 | 6.6 dB  |
| Peaking | 793 Hz  | 4.26 | 0.6 dB  |
| Peaking | 3884 Hz | 9.01 | 1.4 dB  |
| Peaking | 4722 Hz | 8.73 | -2.3 dB |
| Peaking | 6792 Hz | 7.98 | 1.6 dB  |
| Peaking | 7764 Hz | 3.23 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -6.4 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/JAYS%20d-Jays/JAYS%20d-Jays.png)