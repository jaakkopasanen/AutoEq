# E-Mu Teak 2016
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.4; 25 -6.8; 28 -7.3; 31 -7.6; 34 -7.7; 37 -7.8; 41 -7.9; 45 -8.0; 49 -8.0; 54 -8.0; 60 -8.0; 66 -7.8; 72 -7.7; 79 -7.9; 87 -8.3; 96 -8.4; 106 -8.5; 116 -8.5; 128 -8.6; 141 -8.6; 155 -8.5; 170 -8.1; 187 -8.1; 206 -7.9; 227 -7.3; 249 -6.9; 274 -6.3; 302 -6.1; 332 -5.9; 365 -5.5; 402 -5.1; 442 -4.6; 486 -4.5; 535 -4.2; 588 -3.9; 647 -4.1; 712 -4.4; 783 -4.4; 861 -4.1; 947 -4.0; 1042 -4.2; 1146 -3.9; 1261 -3.7; 1387 -3.8; 1526 -4.0; 1678 -3.8; 1846 -3.4; 2031 -2.7; 2234 -2.1; 2457 -1.4; 2703 -1.0; 2973 -0.6; 3270 -0.5; 3597 -1.5; 3957 -1.7; 4353 -2.0; 4788 -3.2; 5267 -3.4; 5793 -3.0; 6373 -2.2; 7010 -1.8; 7711 -3.9; 8482 -4.2; 9330 -4.5; 10263 -5.0; 11289 -4.2; 12418 -4.2; 13660 -4.2; 15026 -4.2; 16529 -4.2; 18182 -4.2; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`E-Mu Teak 2016 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `E-Mu Teak 2016 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.48 | -3.3 dB |
| Peaking | 156 Hz  | 0.82 | -3.5 dB |
| Peaking | 3050 Hz | 1.5  | 3.8 dB  |
| Peaking | 6741 Hz | 6.89 | 2.4 dB  |
| Peaking | 318 Hz  | 2.37 | -0.2 dB |
| Peaking | 557 Hz  | 3.03 | 0.6 dB  |
| Peaking | 9839 Hz | 6.27 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/E-Mu%20Teak%202016/E-Mu%20Teak%202016.png)