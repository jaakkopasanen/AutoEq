# Bose AE2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.4; 23 -10.4; 25 -10.5; 28 -10.4; 31 -10.4; 34 -10.3; 37 -10.1; 41 -9.9; 45 -9.6; 49 -9.3; 54 -8.9; 60 -8.5; 66 -8.1; 72 -7.7; 79 -7.3; 87 -7.0; 96 -6.8; 106 -6.4; 116 -6.2; 128 -6.6; 141 -7.5; 155 -8.2; 170 -6.1; 187 -7.3; 206 -7.0; 227 -6.5; 249 -5.0; 274 -4.0; 302 -4.1; 332 -3.5; 365 -2.8; 402 -2.5; 442 -2.3; 486 -2.6; 535 -2.9; 588 -3.1; 647 -3.8; 712 -4.7; 783 -5.5; 861 -6.2; 947 -6.5; 1042 -6.1; 1146 -5.5; 1261 -4.7; 1387 -4.2; 1526 -3.9; 1678 -3.5; 1846 -3.2; 2031 -2.9; 2234 -2.1; 2457 -2.7; 2703 -3.7; 2973 -5.2; 3270 -5.5; 3597 -5.3; 3957 -5.6; 4353 -5.5; 4788 -2.5; 5267 -0.5; 5793 -1.9; 6373 -4.4; 7010 -6.9; 7711 -6.4; 8482 -7.1; 9330 -7.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose AE2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose AE2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.73 | -4.2 dB |
| Peaking | 194 Hz  | 2.51 | -1.4 dB |
| Peaking | 420 Hz  | 1.17 | 4.4 dB  |
| Peaking | 2111 Hz | 1.79 | 4.1 dB  |
| Peaking | 5338 Hz | 4.76 | 6.5 dB  |
| Peaking | 137 Hz  | 1.71 | 1.1 dB  |
| Peaking | 147 Hz  | 6.72 | -2.5 dB |
| Peaking | 934 Hz  | 4.51 | -1.4 dB |
| Peaking | 1386 Hz | 4.28 | 0.9 dB  |
| Peaking | 9022 Hz | 5.38 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 4.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20AE2/Bose%20AE2.png)