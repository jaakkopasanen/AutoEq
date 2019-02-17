# Venture Electronics Duke
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -1.9; 25 -2.1; 28 -2.3; 31 -2.5; 34 -2.7; 37 -2.9; 41 -3.1; 45 -3.3; 49 -3.5; 54 -3.8; 60 -4.2; 66 -4.6; 72 -4.9; 79 -5.3; 87 -5.6; 96 -6.0; 106 -6.3; 116 -6.5; 128 -6.8; 141 -7.1; 155 -7.2; 170 -7.3; 187 -7.3; 206 -7.3; 227 -7.1; 249 -7.0; 274 -6.7; 302 -6.4; 332 -6.1; 365 -5.7; 402 -5.3; 442 -4.8; 486 -4.4; 535 -3.9; 588 -3.2; 647 -2.8; 712 -2.5; 783 -2.0; 861 -1.9; 947 -1.9; 1042 -2.1; 1146 -2.3; 1261 -2.6; 1387 -3.1; 1526 -3.5; 1678 -3.7; 1846 -3.7; 2031 -2.4; 2234 -2.6; 2457 -2.9; 2703 -4.9; 2973 -5.0; 3270 -2.5; 3597 -0.7; 3957 -0.5; 4353 -1.7; 4788 -1.7; 5267 -1.3; 5793 -2.0; 6373 -6.4; 7010 -10.5; 7711 -10.4; 8482 -7.0; 9330 -2.6; 10263 -2.1; 11289 -2.4; 12418 -4.5; 13660 -2.5; 15026 -2.1; 16529 -2.1; 18182 -3.1; 20000 -2.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Venture Electronics Duke GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Venture Electronics Duke ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 123 Hz  | 0.69 | -4.0 dB  |
| Peaking | 228 Hz  | 1.28 | -2.6 dB  |
| Peaking | 371 Hz  | 1.85 | -1.9 dB  |
| Peaking | 1746 Hz | 2.38 | -1.5 dB  |
| Peaking | 7414 Hz | 4.07 | -10.1 dB |
| Peaking | 18 Hz   | 1.56 | 0.8 dB   |
| Peaking | 2887 Hz | 4.27 | -4.8 dB  |
| Peaking | 3634 Hz | 5.34 | 1.1 dB   |
| Peaking | 3760 Hz | 0.91 | 2.1 dB   |
| Peaking | 9636 Hz | 0.31 | -0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Venture%20Electronics%20Duke/Venture%20Electronics%20Duke.png)