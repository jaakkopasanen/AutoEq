# Dunu DN900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.3; 23 -11.1; 25 -10.9; 28 -10.6; 31 -10.4; 34 -10.2; 37 -10.0; 41 -9.8; 45 -9.6; 49 -9.5; 54 -9.4; 60 -9.3; 66 -9.3; 72 -9.4; 79 -9.5; 87 -9.7; 96 -9.9; 106 -10.0; 116 -10.0; 128 -10.2; 141 -10.3; 155 -10.5; 170 -10.5; 187 -10.4; 206 -10.6; 227 -10.4; 249 -10.4; 274 -10.3; 302 -10.3; 332 -10.1; 365 -10.0; 402 -9.8; 442 -9.6; 486 -9.6; 535 -9.4; 588 -8.9; 647 -8.9; 712 -8.8; 783 -8.7; 861 -8.9; 947 -8.8; 1042 -8.8; 1146 -9.1; 1261 -9.5; 1387 -10.0; 1526 -10.4; 1678 -10.6; 1846 -10.1; 2031 -9.0; 2234 -7.7; 2457 -5.4; 2703 -3.5; 2973 -1.0; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DN900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.54 | -4.6 dB |
| Peaking | 162 Hz  | 0.47 | -1.4 dB |
| Peaking | 276 Hz  | 0.31 | -2.6 dB |
| Peaking | 1765 Hz | 1.39 | -5.8 dB |
| Peaking | 3818 Hz | 0.91 | 7.9 dB  |
| Peaking | 2270 Hz | 5.29 | -0.4 dB |
| Peaking | 3042 Hz | 5.48 | 1.5 dB  |
| Peaking | 3936 Hz | 3.19 | -1.1 dB |
| Peaking | 6290 Hz | 2.51 | 4.9 dB  |
| Peaking | 7426 Hz | 1.52 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 9.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20DN900/Dunu%20DN900.png)