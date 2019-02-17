# Westone UM1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -1.0; 54 -1.5; 60 -2.0; 66 -2.5; 72 -3.0; 79 -3.5; 87 -4.1; 96 -4.5; 106 -5.0; 116 -5.3; 128 -5.7; 141 -6.0; 155 -6.3; 170 -6.5; 187 -6.6; 206 -6.8; 227 -6.8; 249 -6.9; 274 -6.9; 302 -6.9; 332 -6.8; 365 -6.7; 402 -6.6; 442 -6.3; 486 -6.4; 535 -6.3; 588 -5.9; 647 -5.8; 712 -5.8; 783 -5.7; 861 -6.0; 947 -6.3; 1042 -6.6; 1146 -6.9; 1261 -7.2; 1387 -7.7; 1526 -8.1; 1678 -8.1; 1846 -7.6; 2031 -6.7; 2234 -5.7; 2457 -4.0; 2703 -2.5; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -0.9; 4353 -1.1; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone UM1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.63 | 6.7 dB  |
| Peaking | 774 Hz  | 2.58 | 1.0 dB  |
| Peaking | 1748 Hz | 1.39 | -3.0 dB |
| Peaking | 3281 Hz | 1.42 | 6.5 dB  |
| Peaking | 5598 Hz | 2.59 | 5.1 dB  |
| Peaking | 18 Hz   | 0.29 | 1.9 dB  |
| Peaking | 32 Hz   | 1.5  | -2.4 dB |
| Peaking | 192 Hz  | 0.97 | -0.9 dB |
| Peaking | 6521 Hz | 7.06 | 2.2 dB  |
| Peaking | 7820 Hz | 2.2  | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 3.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20UM1/Westone%20UM1.png)