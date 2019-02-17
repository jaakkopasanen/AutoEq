# HZSOUND HZ3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.3; 25 -2.6; 28 -2.9; 31 -3.2; 34 -3.4; 37 -3.6; 41 -3.8; 45 -4.0; 49 -4.2; 54 -4.5; 60 -4.8; 66 -5.2; 72 -5.5; 79 -5.8; 87 -6.3; 96 -6.7; 106 -6.8; 116 -7.0; 128 -7.3; 141 -7.5; 155 -7.6; 170 -7.7; 187 -7.6; 206 -7.7; 227 -7.5; 249 -7.4; 274 -7.2; 302 -7.0; 332 -6.7; 365 -6.4; 402 -6.1; 442 -5.6; 486 -5.4; 535 -5.1; 588 -4.4; 647 -4.1; 712 -3.9; 783 -3.5; 861 -3.6; 947 -2.3; 1042 -3.1; 1146 -3.4; 1261 -2.9; 1387 -2.6; 1526 -3.4; 1678 -3.6; 1846 -3.5; 2031 -3.2; 2234 -3.0; 2457 -2.6; 2703 -2.1; 2973 -1.5; 3270 -0.5; 3597 -0.9; 3957 -1.4; 4353 -3.1; 4788 -7.6; 5267 -11.1; 5793 -8.1; 6373 -3.0; 7010 -0.7; 7711 -2.4; 8482 -3.0; 9330 -4.2; 10263 -2.8; 11289 -2.7; 12418 -2.7; 13660 -2.7; 15026 -2.7; 16529 -2.7; 18182 -2.7; 20000 -2.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HZSOUND HZ3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HZSOUND HZ3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 113 Hz  | 0.68 | -3.0 dB  |
| Peaking | 264 Hz  | 0.64 | -3.6 dB  |
| Peaking | 3930 Hz | 1.98 | 4.3 dB   |
| Peaking | 5296 Hz | 2.84 | -10.9 dB |
| Peaking | 6712 Hz | 4.44 | 4.7 dB   |
| Peaking | 20 Hz   | 1.91 | 1.1 dB   |
| Peaking | 1487 Hz | 0.83 | 1.0 dB   |
| Peaking | 1774 Hz | 2    | -1.5 dB  |
| Peaking | 2096 Hz | 0.14 | -0.2 dB  |
| Peaking | 3226 Hz | 8.82 | 0.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HZSOUND%20HZ3/HZSOUND%20HZ3.png)