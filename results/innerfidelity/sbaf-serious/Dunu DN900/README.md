# Dunu DN900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.1; 23 -8.9; 25 -8.7; 28 -8.4; 31 -8.2; 34 -8.0; 37 -7.8; 41 -7.6; 45 -7.4; 49 -7.3; 54 -7.2; 60 -7.1; 66 -7.1; 72 -7.2; 79 -7.3; 87 -7.5; 96 -7.7; 106 -7.8; 116 -7.8; 128 -8.0; 141 -8.2; 155 -8.3; 170 -8.3; 187 -8.3; 206 -8.4; 227 -8.2; 249 -8.2; 274 -8.1; 302 -8.1; 332 -7.9; 365 -7.8; 402 -7.6; 442 -7.4; 486 -7.4; 535 -7.2; 588 -6.7; 647 -6.7; 712 -6.6; 783 -6.5; 861 -6.7; 947 -6.6; 1042 -6.6; 1146 -6.9; 1261 -7.3; 1387 -7.8; 1526 -8.3; 1678 -8.4; 1846 -7.9; 2031 -6.8; 2234 -5.5; 2457 -3.3; 2703 -1.3; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DN900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.93 | -2.5 dB |
| Peaking | 152 Hz  | 0.85 | -1.4 dB |
| Peaking | 303 Hz  | 0.99 | -1.1 dB |
| Peaking | 1734 Hz | 1.84 | -4.3 dB |
| Peaking | 3741 Hz | 0.84 | 7.2 dB  |
| Peaking | 2237 Hz | 5.18 | -0.8 dB |
| Peaking | 2765 Hz | 3.63 | 1.5 dB  |
| Peaking | 3786 Hz | 2.84 | -1.1 dB |
| Peaking | 6331 Hz | 2.43 | 5.0 dB  |
| Peaking | 7354 Hz | 1.49 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20DN900/Dunu%20DN900.png)