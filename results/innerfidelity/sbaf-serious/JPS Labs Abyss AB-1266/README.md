# JPS Labs Abyss AB-1266
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.0; 34 -0.8; 37 -0.6; 41 -0.7; 45 -1.3; 49 -1.6; 54 -1.2; 60 -0.8; 66 -0.6; 72 -0.6; 79 -0.6; 87 -0.8; 96 -1.0; 106 -1.1; 116 -1.2; 128 -1.5; 141 -1.5; 155 -1.7; 170 -1.9; 187 -2.0; 206 -2.2; 227 -2.1; 249 -2.4; 274 -2.6; 302 -2.9; 332 -3.4; 365 -3.2; 402 -3.7; 442 -4.4; 486 -0.7; 535 -1.1; 588 -1.4; 647 -2.8; 712 -3.9; 783 -4.7; 861 -6.1; 947 -6.6; 1042 -5.6; 1146 -5.4; 1261 -4.4; 1387 -3.9; 1526 -3.3; 1678 -2.0; 1846 -0.5; 2031 -0.5; 2234 -0.8; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.7; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -7.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -8.2; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JPS Labs Abyss AB-1266 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JPS Labs Abyss AB-1266 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.38 | 5.3 dB  |
| Peaking | 119 Hz  | 0.4  | 4.7 dB  |
| Peaking | 539 Hz  | 3.86 | 4.4 dB  |
| Peaking | 3820 Hz | 0.53 | 7.0 dB  |
| Peaking | 8925 Hz | 1.55 | -3.6 dB |
| Peaking | 967 Hz  | 3.89 | -2.3 dB |
| Peaking | 1903 Hz | 4.17 | 2.1 dB  |
| Peaking | 3689 Hz | 2.55 | -0.9 dB |
| Peaking | 6028 Hz | 4.37 | 2.7 dB  |
| Peaking | 6596 Hz | 3.67 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 4.2 dB  |
| Peaking | 125 Hz   | 1.41 | 4.2 dB  |
| Peaking | 250 Hz   | 1.41 | 2.3 dB  |
| Peaking | 500 Hz   | 1.41 | 4.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JPS%20Labs%20Abyss%20AB-1266/JPS%20Labs%20Abyss%20AB-1266.png)