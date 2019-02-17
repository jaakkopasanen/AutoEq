# Westone W10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -0.9; 28 -1.3; 31 -1.8; 34 -2.1; 37 -2.4; 41 -2.8; 45 -3.2; 49 -3.5; 54 -3.9; 60 -4.3; 66 -4.7; 72 -5.2; 79 -5.6; 87 -6.1; 96 -6.7; 106 -6.9; 116 -7.3; 128 -7.6; 141 -8.0; 155 -8.2; 170 -8.3; 187 -8.4; 206 -8.6; 227 -8.5; 249 -8.7; 274 -8.5; 302 -8.5; 332 -8.3; 365 -8.3; 402 -8.3; 442 -7.9; 486 -7.8; 535 -7.5; 588 -6.9; 647 -6.7; 712 -6.7; 783 -6.3; 861 -6.4; 947 -6.4; 1042 -6.6; 1146 -6.5; 1261 -6.5; 1387 -6.6; 1526 -6.5; 1678 -6.2; 1846 -5.4; 2031 -4.2; 2234 -3.2; 2457 -1.9; 2703 -1.1; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.63 | 5.8 dB  |
| Peaking | 56 Hz   | 0.75 | 1.5 dB  |
| Peaking | 205 Hz  | 0.44 | -2.4 dB |
| Peaking | 3954 Hz | 0.94 | 7.0 dB  |
| Peaking | 1610 Hz | 2.63 | -1.5 dB |
| Peaking | 2672 Hz | 2.14 | 1.7 dB  |
| Peaking | 3878 Hz | 2.53 | -1.4 dB |
| Peaking | 6325 Hz | 2.51 | 4.9 dB  |
| Peaking | 7355 Hz | 1.54 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W10/Westone%20W10.png)