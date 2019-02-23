# Master Dynamic ME05
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.1; 25 -7.4; 28 -7.9; 31 -8.2; 34 -8.5; 37 -8.8; 41 -9.0; 45 -9.2; 49 -9.3; 54 -9.4; 60 -9.6; 66 -9.7; 72 -9.8; 79 -9.9; 87 -10.0; 96 -10.1; 106 -9.9; 116 -9.7; 128 -9.6; 141 -9.4; 155 -9.1; 170 -8.8; 187 -8.3; 206 -7.9; 227 -7.3; 249 -6.8; 274 -6.3; 302 -5.7; 332 -5.1; 365 -4.6; 402 -4.0; 442 -3.3; 486 -2.8; 535 -2.3; 588 -1.6; 647 -1.2; 712 -1.0; 783 -0.5; 861 -0.7; 947 -0.9; 1042 -1.3; 1146 -1.6; 1261 -1.8; 1387 -2.4; 1526 -3.1; 1678 -3.8; 1846 -4.0; 2031 -4.1; 2234 -4.5; 2457 -4.4; 2703 -4.6; 2973 -3.7; 3270 -1.9; 3597 -1.0; 3957 -2.0; 4353 -4.9; 4788 -6.8; 5267 -5.8; 5793 -2.9; 6373 -0.7; 7010 -1.6; 7711 -3.8; 8482 -4.1; 9330 -4.1; 10263 -4.1; 11289 -4.1; 12418 -4.1; 13660 -4.1; 15026 -4.1; 16529 -4.1; 18182 -4.1; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Master Dynamic ME05 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Master Dynamic ME05 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 41 Hz    | 0.49 | -3.4 dB |
| Peaking | 128 Hz   | 0.52 | -4.5 dB |
| Peaking | 518 Hz   | 1.3  | 1.4 dB  |
| Peaking | 850 Hz   | 1.19 | 3.5 dB  |
| Peaking | 21272 Hz | 2.12 | 1.4 dB  |
| Peaking | 1271 Hz  | 4.32 | 0.9 dB  |
| Peaking | 3162 Hz  | 0.97 | -2.2 dB |
| Peaking | 3666 Hz  | 2.72 | 5.8 dB  |
| Peaking | 4827 Hz  | 3.62 | -3.7 dB |
| Peaking | 6406 Hz  | 4.56 | 4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Master%20Dynamic%20ME05/Master%20Dynamic%20ME05.png)