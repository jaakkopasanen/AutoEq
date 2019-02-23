# JPS Labs Abyss AB-1266
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -4.3; 25 -5.1; 28 -5.7; 31 -5.9; 34 -5.7; 37 -5.4; 41 -5.5; 45 -6.2; 49 -6.5; 54 -6.1; 60 -5.7; 66 -5.6; 72 -5.5; 79 -5.6; 87 -5.7; 96 -5.9; 106 -6.0; 116 -6.1; 128 -6.4; 141 -6.5; 155 -6.7; 170 -6.8; 187 -6.9; 206 -7.1; 227 -7.1; 249 -7.4; 274 -7.5; 302 -7.9; 332 -8.3; 365 -8.2; 402 -8.7; 442 -9.3; 486 -5.6; 535 -6.0; 588 -6.3; 647 -7.7; 712 -8.9; 783 -9.6; 861 -11.1; 947 -11.5; 1042 -10.5; 1146 -10.4; 1261 -9.4; 1387 -8.9; 1526 -8.2; 1678 -7.0; 1846 -5.0; 2031 -4.9; 2234 -5.7; 2457 -5.3; 2703 -3.6; 2973 -2.9; 3270 -3.1; 3597 -2.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.3; 6373 -7.6; 7010 -8.1; 7711 -7.8; 8482 -10.6; 9330 -12.3; 10263 -9.4; 11289 -7.3; 12418 -8.7; 13660 -10.1; 15026 -10.1; 16529 -11.1; 18182 -13.2; 20000 -13.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JPS Labs Abyss AB-1266 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JPS Labs Abyss AB-1266 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 348 Hz   | 2.41 | -1.9 dB |
| Peaking | 985 Hz   | 2.01 | -5.2 dB |
| Peaking | 4451 Hz  | 1.23 | 9.1 dB  |
| Peaking | 20009 Hz | 0.05 | -5.1 dB |
| Peaking | 533 Hz   | 6.69 | 2.0 dB  |
| Peaking | 5609 Hz  | 9.81 | 3.5 dB  |
| Peaking | 9655 Hz  | 1.96 | -6.1 dB |
| Peaking | 10918 Hz | 2.03 | 6.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.1 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | -6.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JPS%20Labs%20Abyss%20AB-1266/JPS%20Labs%20Abyss%20AB-1266.png)