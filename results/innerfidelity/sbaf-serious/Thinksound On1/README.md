# Thinksound On1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -7.1; 25 -7.6; 28 -8.2; 31 -8.7; 34 -9.1; 37 -9.4; 41 -9.7; 45 -9.9; 49 -10.0; 54 -10.0; 60 -9.9; 66 -10.3; 72 -10.8; 79 -10.9; 87 -11.0; 96 -10.7; 106 -10.1; 116 -9.4; 128 -8.9; 141 -8.2; 155 -7.8; 170 -6.3; 187 -6.2; 206 -5.1; 227 -3.9; 249 -3.1; 274 -3.0; 302 -3.3; 332 -4.0; 365 -4.3; 402 -4.6; 442 -4.9; 486 -5.4; 535 -5.6; 588 -5.5; 647 -5.8; 712 -6.0; 783 -6.1; 861 -6.4; 947 -6.4; 1042 -6.5; 1146 -6.3; 1261 -6.2; 1387 -6.3; 1526 -6.3; 1678 -6.2; 1846 -5.1; 2031 -3.2; 2234 -3.0; 2457 -2.2; 2703 -0.5; 2973 -0.9; 3270 -2.4; 3597 -2.7; 3957 -2.0; 4353 -2.5; 4788 -1.5; 5267 -0.5; 5793 -3.0; 6373 -3.8; 7010 -6.1; 7711 -6.7; 8482 -8.1; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.6; 13660 -7.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Thinksound On1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thinksound On1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 1.58 | -1.8 dB |
| Peaking | 87 Hz    | 0.82 | -4.5 dB |
| Peaking | 269 Hz   | 1.31 | 4.3 dB  |
| Peaking | 2791 Hz  | 1.98 | 5.6 dB  |
| Peaking | 5092 Hz  | 3.05 | 5.4 dB  |
| Peaking | 1749 Hz  | 2.07 | -1.1 dB |
| Peaking | 2059 Hz  | 5.96 | 1.9 dB  |
| Peaking | 6300 Hz  | 2.95 | 0.6 dB  |
| Peaking | 8408 Hz  | 3.69 | -2.1 dB |
| Peaking | 12274 Hz | 2.14 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | 4.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Thinksound%20On1/Thinksound%20On1.png)