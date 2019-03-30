# ASTRO Gaming A40
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.3; 23 -11.6; 25 -11.8; 28 -11.9; 31 -11.8; 34 -11.4; 37 -11.1; 41 -10.9; 45 -11.1; 49 -11.5; 54 -11.9; 60 -12.3; 66 -12.6; 72 -12.8; 79 -12.7; 87 -12.7; 96 -12.7; 106 -12.8; 116 -12.6; 128 -12.4; 141 -12.3; 155 -12.1; 170 -11.8; 187 -11.6; 206 -11.4; 227 -11.2; 249 -11.0; 274 -10.8; 302 -10.6; 332 -10.4; 365 -10.1; 402 -9.7; 442 -9.2; 486 -8.6; 535 -8.1; 588 -7.6; 647 -7.3; 712 -7.2; 783 -6.9; 861 -6.3; 947 -5.4; 1042 -5.0; 1146 -4.7; 1261 -4.6; 1387 -4.7; 1526 -4.8; 1678 -4.6; 1846 -4.2; 2031 -4.0; 2234 -3.6; 2457 -2.3; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -1.7; 3957 -1.8; 4353 -2.0; 4788 -4.2; 5267 -7.0; 5793 -8.7; 6373 -8.2; 7010 -5.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`ASTRO Gaming A40 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ASTRO Gaming A40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.59 | -3.1 dB |
| Peaking | 105 Hz   | 0.3  | -6.1 dB |
| Peaking | 3219 Hz  | 0.77 | 5.8 dB  |
| Peaking | 4548 Hz  | 2.99 | 1.3 dB  |
| Peaking | 5688 Hz  | 2.67 | -5.5 dB |
| Peaking | 368 Hz   | 3.12 | -0.7 dB |
| Peaking | 1093 Hz  | 2.41 | 1.4 dB  |
| Peaking | 2319 Hz  | 2.07 | -1.9 dB |
| Peaking | 2715 Hz  | 3.59 | 2.1 dB  |
| Peaking | 10152 Hz | 2.61 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/ASTRO%20Gaming%20A40/ASTRO%20Gaming%20A40.png)