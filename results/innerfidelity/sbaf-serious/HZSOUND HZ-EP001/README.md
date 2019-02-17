# HZSOUND HZ-EP001
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.0; 23 -9.1; 25 -9.1; 28 -9.1; 31 -9.1; 34 -9.1; 37 -9.0; 41 -8.9; 45 -9.0; 49 -9.0; 54 -9.0; 60 -9.1; 66 -9.3; 72 -9.4; 79 -9.5; 87 -9.8; 96 -10.0; 106 -10.1; 116 -10.1; 128 -10.3; 141 -10.4; 155 -10.5; 170 -10.6; 187 -10.6; 206 -10.5; 227 -10.4; 249 -10.4; 274 -10.3; 302 -10.1; 332 -10.1; 365 -10.2; 402 -9.8; 442 -7.3; 486 -8.2; 535 -8.1; 588 -7.5; 647 -7.3; 712 -6.8; 783 -6.6; 861 -6.5; 947 -6.5; 1042 -6.5; 1146 -6.3; 1261 -6.2; 1387 -6.4; 1526 -6.5; 1678 -6.4; 1846 -5.7; 2031 -5.1; 2234 -4.7; 2457 -3.6; 2703 -3.4; 2973 -3.2; 3270 -3.0; 3597 -4.8; 3957 -5.8; 4353 -5.6; 4788 -3.4; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HZSOUND HZ-EP001 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HZSOUND HZ-EP001 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.13 | -2.4 dB |
| Peaking | 195 Hz  | 0.71 | -3.1 dB |
| Peaking | 359 Hz  | 3.82 | -1.9 dB |
| Peaking | 2774 Hz | 2.3  | 3.3 dB  |
| Peaking | 5764 Hz | 3.18 | 6.6 dB  |
| Peaking | 273 Hz  | 6.71 | -0.3 dB |
| Peaking | 1609 Hz | 7.8  | -0.4 dB |
| Peaking | 4156 Hz | 5.85 | -3.2 dB |
| Peaking | 4285 Hz | 1.89 | 1.4 dB  |
| Peaking | 8215 Hz | 3.62 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HZSOUND%20HZ-EP001/HZSOUND%20HZ-EP001.png)