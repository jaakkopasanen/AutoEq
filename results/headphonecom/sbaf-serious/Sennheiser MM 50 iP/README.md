# Sennheiser MM 50 iP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -3.9; 25 -4.4; 28 -5.1; 31 -5.7; 34 -6.3; 37 -6.7; 41 -7.3; 45 -7.8; 49 -8.2; 54 -8.7; 60 -9.3; 66 -9.8; 72 -10.2; 79 -10.7; 87 -11.0; 96 -11.3; 106 -11.6; 116 -11.8; 128 -11.9; 141 -12.0; 155 -12.1; 170 -12.0; 187 -11.8; 206 -11.4; 227 -11.1; 249 -10.5; 274 -10.5; 302 -10.3; 332 -9.7; 365 -8.9; 402 -8.2; 442 -7.6; 486 -7.0; 535 -6.2; 588 -5.5; 647 -4.7; 712 -4.1; 783 -3.5; 861 -3.2; 947 -3.0; 1042 -2.9; 1146 -2.6; 1261 -2.8; 1387 -2.8; 1526 -3.5; 1678 -4.0; 1846 -3.9; 2031 -3.5; 2234 -2.9; 2457 -2.2; 2703 -1.8; 2973 -1.1; 3270 -0.5; 3597 -0.5; 3957 -1.3; 4353 -3.8; 4788 -5.7; 5267 -7.4; 5793 -11.2; 6373 -10.4; 7010 -6.4; 7711 -6.2; 8482 -7.1; 9330 -9.7; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MM 50 iP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MM 50 iP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.61 | 4.6 dB  |
| Peaking | 153 Hz  | 0.37 | -5.9 dB |
| Peaking | 928 Hz  | 0.69 | 4.5 dB  |
| Peaking | 3369 Hz | 1.67 | 6.0 dB  |
| Peaking | 5890 Hz | 4.63 | -6.9 dB |
| Peaking | 2419 Hz | 8.52 | 0.6 dB  |
| Peaking | 6350 Hz | 9.09 | -2.0 dB |
| Peaking | 7016 Hz | 2.8  | 1.5 dB  |
| Peaking | 9320 Hz | 6.17 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20MM%2050%20iP/Sennheiser%20MM%2050%20iP.png)