# ADV Sound M4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -10.1; 25 -10.4; 28 -10.6; 31 -10.8; 34 -11.0; 37 -11.1; 41 -11.3; 45 -11.5; 49 -11.7; 54 -11.9; 60 -12.1; 66 -12.4; 72 -12.7; 79 -12.9; 87 -13.2; 96 -13.5; 106 -13.6; 116 -13.6; 128 -13.7; 141 -13.8; 155 -13.6; 170 -13.5; 187 -13.2; 206 -12.9; 227 -12.5; 249 -12.1; 274 -11.6; 302 -11.0; 332 -10.4; 365 -9.8; 402 -9.1; 442 -8.3; 486 -7.8; 535 -7.1; 588 -6.1; 647 -5.6; 712 -5.2; 783 -4.5; 861 -4.3; 947 -4.2; 1042 -3.8; 1146 -3.6; 1261 -3.8; 1387 -4.2; 1526 -4.5; 1678 -4.4; 1846 -4.0; 2031 -3.4; 2234 -3.1; 2457 -3.5; 2703 -3.5; 2973 -1.1; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.9; 5267 -0.7; 5793 -1.9; 6373 -5.6; 7010 -10.0; 7711 -9.2; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`ADV Sound M4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ADV Sound M4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.82 | -1.9 dB |
| Peaking | 79 Hz   | 0.38 | -2.9 dB |
| Peaking | 196 Hz  | 0.36 | -5.5 dB |
| Peaking | 862 Hz  | 0.53 | 3.9 dB  |
| Peaking | 3927 Hz | 1.55 | 6.4 dB  |
| Peaking | 1597 Hz | 4.46 | -0.6 dB |
| Peaking | 2123 Hz | 5.27 | 0.8 dB  |
| Peaking | 5343 Hz | 6.03 | 2.3 dB  |
| Peaking | 5951 Hz | 4.86 | 2.3 dB  |
| Peaking | 7151 Hz | 3.89 | -5.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/ADV%20Sound%20M4/ADV%20Sound%20M4.png)