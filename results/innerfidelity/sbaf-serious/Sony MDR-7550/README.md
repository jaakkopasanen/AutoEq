# Sony MDR-7550
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -1.8; 25 -2.0; 28 -2.4; 31 -2.6; 34 -2.9; 37 -3.1; 41 -3.3; 45 -3.6; 49 -3.8; 54 -4.1; 60 -4.5; 66 -4.9; 72 -5.2; 79 -5.6; 87 -6.0; 96 -6.5; 106 -6.8; 116 -7.0; 128 -7.4; 141 -7.7; 155 -7.9; 170 -8.0; 187 -8.2; 206 -8.2; 227 -8.2; 249 -8.2; 274 -8.0; 302 -8.0; 332 -7.8; 365 -7.6; 402 -7.4; 442 -7.0; 486 -6.9; 535 -6.7; 588 -6.2; 647 -6.0; 712 -5.9; 783 -5.7; 861 -6.0; 947 -6.3; 1042 -6.5; 1146 -6.6; 1261 -7.5; 1387 -8.6; 1526 -9.6; 1678 -10.0; 1846 -9.8; 2031 -8.9; 2234 -7.4; 2457 -5.0; 2703 -2.6; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -4.0; 4788 -8.3; 5267 -8.5; 5793 -3.1; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7550 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.41 | 4.9 dB  |
| Peaking | 46 Hz   | 2.07 | 2.3 dB  |
| Peaking | 1772 Hz | 2.31 | -4.6 dB |
| Peaking | 3243 Hz | 2.39 | 7.4 dB  |
| Peaking | 6351 Hz | 7.65 | 5.8 dB  |
| Peaking | 227 Hz  | 0.92 | -1.9 dB |
| Peaking | 758 Hz  | 2.02 | 1.2 dB  |
| Peaking | 4058 Hz | 6.86 | 3.7 dB  |
| Peaking | 5079 Hz | 4.02 | -5.4 dB |
| Peaking | 5824 Hz | 6.13 | 3.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-7550/Sony%20MDR-7550.png)