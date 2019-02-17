# Grado iGrado White
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -1.1; 79 -2.1; 87 -2.9; 96 -3.6; 106 -4.0; 116 -4.5; 128 -5.0; 141 -5.5; 155 -5.9; 170 -6.1; 187 -6.4; 206 -6.5; 227 -6.6; 249 -6.4; 274 -6.4; 302 -6.3; 332 -6.1; 365 -6.1; 402 -6.2; 442 -6.2; 486 -6.1; 535 -6.2; 588 -6.0; 647 -6.0; 712 -5.9; 783 -5.9; 861 -6.2; 947 -6.4; 1042 -6.6; 1146 -6.8; 1261 -7.2; 1387 -8.0; 1526 -9.0; 1678 -9.7; 1846 -9.9; 2031 -9.6; 2234 -8.4; 2457 -6.8; 2703 -7.2; 2973 -6.3; 3270 -3.4; 3597 -2.4; 3957 -3.1; 4353 -2.9; 4788 -1.6; 5267 -0.8; 5793 -0.5; 6373 -2.7; 7010 -4.1; 7711 -6.2; 8482 -6.7; 9330 -8.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado iGrado White GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado iGrado White ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.54 | 6.8 dB  |
| Peaking | 1852 Hz | 2.2  | -4.0 dB |
| Peaking | 3558 Hz | 4.13 | 3.2 dB  |
| Peaking | 5485 Hz | 2.08 | 6.3 dB  |
| Peaking | 9052 Hz | 4.19 | -2.7 dB |
| Peaking | 40 Hz   | 2.82 | -0.9 dB |
| Peaking | 69 Hz   | 3.11 | 1.5 dB  |
| Peaking | 187 Hz  | 1.56 | -1.0 dB |
| Peaking | 718 Hz  | 1.16 | 0.6 dB  |
| Peaking | 1499 Hz | 5.52 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 5.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20iGrado%20White/Grado%20iGrado%20White.png)