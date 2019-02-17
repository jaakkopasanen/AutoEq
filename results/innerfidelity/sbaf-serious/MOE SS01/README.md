# MOE SS01
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.4; 25 -6.5; 28 -6.5; 31 -6.6; 34 -6.6; 37 -6.6; 41 -6.7; 45 -6.7; 49 -6.8; 54 -6.9; 60 -6.9; 66 -7.1; 72 -7.2; 79 -7.4; 87 -7.6; 96 -7.8; 106 -7.8; 116 -7.8; 128 -7.8; 141 -7.7; 155 -7.6; 170 -7.4; 187 -7.1; 206 -6.9; 227 -6.4; 249 -6.0; 274 -5.6; 302 -5.1; 332 -4.6; 365 -4.0; 402 -3.5; 442 -2.9; 486 -2.5; 535 -2.0; 588 -1.3; 647 -1.0; 712 -0.9; 783 -0.5; 861 -0.7; 947 -0.9; 1042 -1.3; 1146 -1.6; 1261 -2.0; 1387 -2.6; 1526 -3.4; 1678 -3.4; 1846 -3.1; 2031 -3.4; 2234 -3.9; 2457 -4.0; 2703 -4.5; 2973 -4.4; 3270 -2.8; 3597 -1.6; 3957 -2.5; 4353 -5.3; 4788 -7.4; 5267 -7.6; 5793 -5.5; 6373 -3.0; 7010 -1.7; 7711 -1.9; 8482 -3.8; 9330 -4.3; 10263 -1.5; 11289 -1.1; 12418 -1.1; 13660 -1.1; 15026 -1.1; 16529 -1.1; 18182 -1.1; 20000 -1.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MOE SS01 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MOE SS01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.28 | -5.2 dB |
| Peaking | 132 Hz  | 0.81 | -4.1 dB |
| Peaking | 256 Hz  | 1.4  | -2.4 dB |
| Peaking | 2322 Hz | 1.53 | -2.9 dB |
| Peaking | 5117 Hz | 3.12 | -6.8 dB |
| Peaking | 785 Hz  | 2.74 | 1.2 dB  |
| Peaking | 1528 Hz | 4.3  | -1.5 dB |
| Peaking | 2892 Hz | 8.29 | -1.7 dB |
| Peaking | 4615 Hz | 0.28 | 0.5 dB  |
| Peaking | 8972 Hz | 4.93 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | -3.1 dB |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MOE%20SS01/MOE%20SS01.png)