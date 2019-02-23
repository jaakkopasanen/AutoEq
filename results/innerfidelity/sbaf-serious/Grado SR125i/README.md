# Grado SR125i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.5; 45 -2.4; 49 -3.1; 54 -3.9; 60 -4.6; 66 -5.2; 72 -5.7; 79 -6.2; 87 -6.6; 96 -7.0; 106 -7.0; 116 -7.1; 128 -7.2; 141 -7.1; 155 -7.0; 170 -6.9; 187 -6.6; 206 -6.4; 227 -6.0; 249 -5.7; 274 -5.3; 302 -4.9; 332 -5.5; 365 -5.4; 402 -5.5; 442 -5.2; 486 -5.1; 535 -5.0; 588 -4.5; 647 -4.5; 712 -4.5; 783 -4.4; 861 -4.6; 947 -4.6; 1042 -4.8; 1146 -4.8; 1261 -5.4; 1387 -6.2; 1526 -7.6; 1678 -8.4; 1846 -10.7; 2031 -14.9; 2234 -13.6; 2457 -10.7; 2703 -8.6; 2973 -6.7; 3270 -5.0; 3597 -6.7; 3957 -6.4; 4353 -4.6; 4788 -4.9; 5267 -5.6; 5793 -3.7; 6373 -3.4; 7010 -7.0; 7711 -8.4; 8482 -9.0; 9330 -8.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR125i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR125i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 1.15 | 6.9 dB  |
| Peaking | 831 Hz  | 0.66 | 2.3 dB  |
| Peaking | 2091 Hz | 3.26 | -9.7 dB |
| Peaking | 6590 Hz | 1.33 | 5.3 dB  |
| Peaking | 7892 Hz | 2.12 | -6.5 dB |
| Peaking | 50 Hz   | 2.1  | 0.9 dB  |
| Peaking | 115 Hz  | 0.92 | -1.3 dB |
| Peaking | 288 Hz  | 3.35 | 1.1 dB  |
| Peaking | 3280 Hz | 6.8  | 3.0 dB  |
| Peaking | 3321 Hz | 3.18 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR125i/Grado%20SR125i.png)