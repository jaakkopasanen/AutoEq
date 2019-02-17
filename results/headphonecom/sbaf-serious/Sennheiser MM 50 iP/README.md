# Sennheiser MM 50 iP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -4.5; 25 -5.0; 28 -5.7; 31 -6.3; 34 -6.9; 37 -7.3; 41 -7.9; 45 -8.4; 49 -8.8; 54 -9.3; 60 -9.9; 66 -10.4; 72 -10.8; 79 -11.3; 87 -11.6; 96 -11.9; 106 -12.2; 116 -12.4; 128 -12.5; 141 -12.6; 155 -12.7; 170 -12.6; 187 -12.4; 206 -12.0; 227 -11.7; 249 -11.1; 274 -11.0; 302 -10.9; 332 -10.3; 365 -9.5; 402 -8.8; 442 -8.2; 486 -7.5; 535 -6.8; 588 -6.1; 647 -5.3; 712 -4.7; 783 -4.1; 861 -3.8; 947 -3.6; 1042 -3.5; 1146 -3.2; 1261 -3.4; 1387 -3.4; 1526 -4.1; 1678 -4.6; 1846 -4.5; 2031 -4.1; 2234 -3.5; 2457 -2.8; 2703 -2.4; 2973 -1.7; 3270 -0.9; 3597 -0.5; 3957 -1.9; 4353 -4.4; 4788 -6.3; 5267 -7.9; 5793 -11.8; 6373 -10.9; 7010 -7.0; 7711 -5.5; 8482 -7.5; 9330 -10.3; 10263 -6.3; 11289 -3.6; 12418 -3.6; 13660 -3.6; 15026 -3.6; 16529 -3.6; 18182 -3.6; 20000 -3.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MM 50 iP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MM 50 iP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 113 Hz   | 0.46 | -8.5 dB |
| Peaking | 296 Hz   | 1.04 | -3.3 dB |
| Peaking | 3456 Hz  | 2.95 | 3.9 dB  |
| Peaking | 5953 Hz  | 3.42 | -9.1 dB |
| Peaking | 9337 Hz  | 5.48 | -6.8 dB |
| Peaking | 16 Hz    | 2.29 | 1.3 dB  |
| Peaking | 1053 Hz  | 1.64 | 1.1 dB  |
| Peaking | 1754 Hz  | 4.2  | -1.3 dB |
| Peaking | 9994 Hz  | 8.41 | -2.2 dB |
| Peaking | 10702 Hz | 3.72 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -7.6 dB |
| Peaking | 250 Hz   | 1.41 | -6.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20MM%2050%20iP/Sennheiser%20MM%2050%20iP.png)