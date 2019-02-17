# Havi B3 Pro1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.8; 54 -1.2; 60 -1.8; 66 -2.2; 72 -2.6; 79 -3.1; 87 -3.5; 96 -4.0; 106 -4.4; 116 -4.6; 128 -5.0; 141 -5.3; 155 -5.6; 170 -5.8; 187 -5.9; 206 -6.2; 227 -6.1; 249 -6.4; 274 -6.4; 302 -6.5; 332 -6.6; 365 -6.7; 402 -6.8; 442 -6.8; 486 -7.0; 535 -7.1; 588 -6.9; 647 -6.8; 712 -7.0; 783 -6.7; 861 -6.6; 947 -6.5; 1042 -6.3; 1146 -5.8; 1261 -6.1; 1387 -5.7; 1526 -5.4; 1678 -5.5; 1846 -5.0; 2031 -4.7; 2234 -4.1; 2457 -3.0; 2703 -2.0; 2973 -0.8; 3270 -0.5; 3597 -1.4; 3957 -3.0; 4353 -2.3; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Havi B3 Pro1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Havi B3 Pro1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.52 | 6.5 dB  |
| Peaking | 3045 Hz  | 1.94 | 5.0 dB  |
| Peaking | 5835 Hz  | 1.64 | 6.9 dB  |
| Peaking | 7901 Hz  | 1.89 | -2.9 dB |
| Peaking | 20961 Hz | 1.31 | -0.3 dB |
| Peaking | 14 Hz    | 1.95 | 1.1 dB  |
| Peaking | 480 Hz   | 1.06 | -0.7 dB |
| Peaking | 12740 Hz | 2.36 | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Havi%20B3%20Pro1/Havi%20B3%20Pro1.png)