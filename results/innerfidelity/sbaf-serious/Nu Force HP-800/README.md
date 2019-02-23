# Nu Force HP-800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.6; 25 -7.3; 28 -8.1; 31 -8.7; 34 -9.1; 37 -9.4; 41 -9.7; 45 -10.0; 49 -10.2; 54 -10.2; 60 -10.2; 66 -10.3; 72 -10.5; 79 -10.9; 87 -11.2; 96 -11.3; 106 -11.5; 116 -11.6; 128 -11.7; 141 -11.7; 155 -11.6; 170 -11.3; 187 -11.3; 206 -11.0; 227 -10.7; 249 -10.5; 274 -9.7; 302 -8.7; 332 -7.7; 365 -5.6; 402 -4.0; 442 -4.4; 486 -4.2; 535 -4.2; 588 -5.3; 647 -5.6; 712 -5.4; 783 -4.7; 861 -4.2; 947 -3.9; 1042 -3.6; 1146 -3.3; 1261 -3.4; 1387 -4.0; 1526 -5.0; 1678 -6.2; 1846 -7.2; 2031 -8.1; 2234 -9.0; 2457 -10.2; 2703 -10.6; 2973 -9.7; 3270 -8.2; 3597 -6.7; 3957 -5.2; 4353 -4.0; 4788 -1.1; 5267 -0.5; 5793 -0.5; 6373 -1.3; 7010 -4.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nu Force HP-800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nu Force HP-800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 111 Hz  | 0.46 | -6.0 dB |
| Peaking | 229 Hz  | 1.45 | -3.5 dB |
| Peaking | 607 Hz  | 0.23 | 3.6 dB  |
| Peaking | 2576 Hz | 1.63 | -6.5 dB |
| Peaking | 5377 Hz | 2.38 | 6.9 dB  |
| Peaking | 40 Hz   | 3.38 | -0.8 dB |
| Peaking | 405 Hz  | 6.08 | 2.0 dB  |
| Peaking | 677 Hz  | 3.85 | -1.8 dB |
| Peaking | 1220 Hz | 4.28 | 1.3 dB  |
| Peaking | 8279 Hz | 4    | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nu%20Force%20HP-800/Nu%20Force%20HP-800.png)