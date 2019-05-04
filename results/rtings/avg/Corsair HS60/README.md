# Corsair HS60
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.0; 25 -6.3; 28 -6.6; 31 -6.9; 34 -7.1; 37 -7.3; 41 -7.5; 45 -7.7; 49 -7.8; 54 -8.0; 60 -8.3; 66 -8.6; 72 -8.9; 79 -9.3; 87 -9.7; 96 -10.0; 106 -10.3; 116 -10.4; 128 -10.4; 141 -10.3; 155 -10.0; 170 -9.4; 187 -8.5; 206 -7.6; 227 -6.6; 249 -5.7; 274 -4.7; 302 -3.9; 332 -3.3; 365 -2.9; 402 -2.7; 442 -3.1; 486 -3.9; 535 -4.8; 588 -5.7; 647 -6.2; 712 -6.0; 783 -5.6; 861 -4.2; 947 -3.0; 1042 -3.8; 1146 -3.4; 1261 -3.2; 1387 -3.2; 1526 -3.1; 1678 -3.2; 1846 -3.8; 2031 -4.4; 2234 -4.8; 2457 -5.1; 2703 -5.2; 2973 -5.0; 3270 -3.7; 3597 -1.5; 3957 -1.4; 4353 -5.5; 4788 -8.3; 5267 -6.6; 5793 -4.9; 6373 -0.5; 7010 -2.9; 7711 -7.1; 8482 -12.4; 9330 -10.7; 10263 -8.3; 11289 -9.9; 12418 -10.2; 13660 -7.5; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Corsair HS60 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Corsair HS60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 114 Hz   | 0.78 | -6.3 dB |
| Peaking | 2376 Hz  | 0.05 | 2.0 dB  |
| Peaking | 6644 Hz  | 5.04 | 7.5 dB  |
| Peaking | 8561 Hz  | 6.74 | -4.5 dB |
| Peaking | 10033 Hz | 0.65 | -6.1 dB |
| Peaking | 375 Hz   | 2.4  | 2.3 dB  |
| Peaking | 656 Hz   | 3.21 | -2.9 dB |
| Peaking | 2777 Hz  | 2.96 | -1.8 dB |
| Peaking | 3846 Hz  | 3.49 | 5.0 dB  |
| Peaking | 4715 Hz  | 4.95 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | 1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Corsair%20HS60/Corsair%20HS60.png)