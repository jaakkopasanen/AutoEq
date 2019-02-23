# Sony MDR-Z7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -3.9; 25 -5.0; 28 -6.3; 31 -7.2; 34 -7.9; 37 -8.2; 41 -8.5; 45 -8.6; 49 -8.5; 54 -8.4; 60 -8.4; 66 -8.3; 72 -8.1; 79 -7.9; 87 -7.7; 96 -8.1; 106 -8.8; 116 -9.0; 128 -8.5; 141 -9.4; 155 -10.5; 170 -9.5; 187 -9.6; 206 -9.2; 227 -8.8; 249 -8.3; 274 -7.7; 302 -6.9; 332 -6.3; 365 -5.7; 402 -5.2; 442 -4.6; 486 -4.6; 535 -4.5; 588 -4.2; 647 -4.5; 712 -5.1; 783 -5.6; 861 -6.0; 947 -5.5; 1042 -4.3; 1146 -1.9; 1261 -0.5; 1387 -0.5; 1526 -1.9; 1678 -4.0; 1846 -6.1; 2031 -7.8; 2234 -9.0; 2457 -9.5; 2703 -8.3; 2973 -6.8; 3270 -4.2; 3597 -2.0; 3957 -2.7; 4353 -4.7; 4788 -4.6; 5267 -2.0; 5793 -1.8; 6373 -3.7; 7010 -4.0; 7711 -5.4; 8482 -5.8; 9330 -6.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-Z7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Z7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 3.4  | 3.5 dB  |
| Peaking | 114 Hz  | 0.51 | -3.6 dB |
| Peaking | 1350 Hz | 2.56 | 6.0 dB  |
| Peaking | 2466 Hz | 1.64 | -9.4 dB |
| Peaking | 3245 Hz | 0.85 | 6.1 dB  |
| Peaking | 26 Hz   | 0.53 | 2.7 dB  |
| Peaking | 37 Hz   | 1.35 | -4.0 dB |
| Peaking | 484 Hz  | 2.57 | 2.0 dB  |
| Peaking | 5798 Hz | 5.2  | 3.4 dB  |
| Peaking | 7093 Hz | 0.74 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-Z7/Sony%20MDR-Z7.png)