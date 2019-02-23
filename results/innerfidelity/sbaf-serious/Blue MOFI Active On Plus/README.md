# Blue MOFI Active On Plus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.5; 25 -7.8; 28 -8.3; 31 -8.7; 34 -9.2; 37 -9.6; 41 -10.2; 45 -10.8; 49 -11.3; 54 -11.9; 60 -12.5; 66 -12.9; 72 -13.1; 79 -13.1; 87 -12.9; 96 -12.8; 106 -12.5; 116 -11.9; 128 -11.7; 141 -11.9; 155 -11.9; 170 -10.9; 187 -11.3; 206 -11.0; 227 -10.4; 249 -9.6; 274 -8.4; 302 -7.5; 332 -7.2; 365 -7.2; 402 -7.2; 442 -5.6; 486 -4.9; 535 -5.5; 588 -5.7; 647 -6.0; 712 -6.6; 783 -6.9; 861 -7.5; 947 -8.2; 1042 -8.3; 1146 -8.2; 1261 -8.2; 1387 -8.4; 1526 -8.7; 1678 -8.6; 1846 -8.1; 2031 -7.0; 2234 -6.1; 2457 -5.9; 2703 -4.8; 2973 -4.3; 3270 -4.1; 3597 -3.2; 3957 -4.9; 4353 -8.3; 4788 -3.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Blue MOFI Active On Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Blue MOFI Active On Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 75 Hz   | 0.74 | -6.7 dB |
| Peaking | 184 Hz  | 1.82 | -3.0 dB |
| Peaking | 1461 Hz | 1.71 | -2.4 dB |
| Peaking | 3169 Hz | 2.78 | 2.7 dB  |
| Peaking | 5787 Hz | 3.53 | 6.9 dB  |
| Peaking | 236 Hz  | 6.04 | -0.8 dB |
| Peaking | 509 Hz  | 2.52 | 2.0 dB  |
| Peaking | 967 Hz  | 4.93 | -1.2 dB |
| Peaking | 6598 Hz | 6.67 | 1.4 dB  |
| Peaking | 8805 Hz | 3.13 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -5.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Blue%20MOFI%20Active%20On%20Plus/Blue%20MOFI%20Active%20On%20Plus.png)