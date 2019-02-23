# T-Peos Rich 200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.0; 25 -8.0; 28 -8.0; 31 -8.1; 34 -8.1; 37 -8.1; 41 -8.2; 45 -8.3; 49 -8.4; 54 -8.6; 60 -8.7; 66 -9.0; 72 -9.1; 79 -9.4; 87 -9.7; 96 -9.9; 106 -10.0; 116 -10.0; 128 -10.1; 141 -10.0; 155 -10.0; 170 -9.8; 187 -9.6; 206 -9.3; 227 -8.9; 249 -8.5; 274 -8.1; 302 -7.6; 332 -7.2; 365 -6.6; 402 -6.1; 442 -5.4; 486 -5.1; 535 -4.5; 588 -3.9; 647 -3.5; 712 -3.4; 783 -3.1; 861 -3.3; 947 -3.7; 1042 -4.1; 1146 -4.6; 1261 -5.2; 1387 -6.1; 1526 -7.2; 1678 -8.0; 1846 -8.7; 2031 -9.0; 2234 -8.8; 2457 -6.9; 2703 -4.7; 2973 -1.8; 3270 -0.5; 3597 -0.5; 3957 -1.3; 4353 -5.7; 4788 -10.5; 5267 -11.7; 5793 -7.4; 6373 -3.9; 7010 -4.0; 7711 -7.4; 8482 -10.0; 9330 -8.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`T-Peos Rich 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Rich 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 117 Hz  | 0.47 | -3.6 dB |
| Peaking | 695 Hz  | 1.4  | 4.0 dB  |
| Peaking | 3542 Hz | 3.35 | 7.3 dB  |
| Peaking | 5030 Hz | 6.95 | -7.7 dB |
| Peaking | 8714 Hz | 7.16 | -4.2 dB |
| Peaking | 23 Hz   | 1.65 | -0.9 dB |
| Peaking | 1157 Hz | 1.8  | 1.8 dB  |
| Peaking | 2095 Hz | 1.26 | -4.0 dB |
| Peaking | 2917 Hz | 3.6  | 3.7 dB  |
| Peaking | 6649 Hz | 6.85 | 4.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Rich%20200/T-Peos%20Rich%20200.png)