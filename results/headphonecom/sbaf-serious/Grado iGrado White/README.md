# Grado iGrado White
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.8; 72 -1.9; 79 -2.8; 87 -3.7; 96 -4.4; 106 -4.7; 116 -5.2; 128 -5.8; 141 -6.2; 155 -6.7; 170 -6.9; 187 -7.2; 206 -7.3; 227 -7.4; 249 -7.2; 274 -7.1; 302 -7.0; 332 -6.9; 365 -6.9; 402 -7.0; 442 -7.0; 486 -6.9; 535 -7.0; 588 -6.7; 647 -6.8; 712 -6.7; 783 -6.7; 861 -6.9; 947 -7.2; 1042 -7.4; 1146 -7.6; 1261 -8.0; 1387 -8.8; 1526 -9.7; 1678 -10.5; 1846 -10.7; 2031 -10.4; 2234 -9.2; 2457 -7.6; 2703 -8.0; 2973 -7.1; 3270 -4.2; 3597 -3.2; 3957 -3.9; 4353 -3.7; 4788 -2.4; 5267 -1.6; 5793 -0.5; 6373 -3.5; 7010 -4.2; 7711 -6.2; 8482 -7.2; 9330 -9.3; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado iGrado White GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado iGrado White ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.68 | 7.0 dB  |
| Peaking | 1844 Hz | 1.51 | -4.4 dB |
| Peaking | 3570 Hz | 3.68 | 3.2 dB  |
| Peaking | 5548 Hz | 2.46 | 6.0 dB  |
| Peaking | 9132 Hz | 5.78 | -3.6 dB |
| Peaking | 38 Hz   | 3.03 | -1.2 dB |
| Peaking | 64 Hz   | 2.7  | 1.8 dB  |
| Peaking | 154 Hz  | 2.37 | -0.4 dB |
| Peaking | 216 Hz  | 1.15 | -1.2 dB |
| Peaking | 4819 Hz | 5.16 | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20iGrado%20White/Grado%20iGrado%20White.png)