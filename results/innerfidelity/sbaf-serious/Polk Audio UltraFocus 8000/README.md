# Polk Audio UltraFocus 8000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.6; 23 -9.5; 25 -9.4; 28 -9.1; 31 -8.8; 34 -8.3; 37 -7.9; 41 -7.5; 45 -7.1; 49 -6.8; 54 -6.4; 60 -5.9; 66 -5.6; 72 -5.4; 79 -5.3; 87 -5.4; 96 -5.3; 106 -5.2; 116 -5.0; 128 -5.0; 141 -4.9; 155 -4.7; 170 -4.4; 187 -4.6; 206 -4.6; 227 -4.5; 249 -4.6; 274 -4.7; 302 -4.8; 332 -4.9; 365 -4.7; 402 -5.0; 442 -5.0; 486 -5.3; 535 -5.0; 588 -4.6; 647 -4.7; 712 -4.9; 783 -4.8; 861 -5.3; 947 -6.0; 1042 -6.5; 1146 -6.1; 1261 -5.6; 1387 -5.3; 1526 -4.8; 1678 -4.3; 1846 -3.5; 2031 -3.1; 2234 -2.4; 2457 -0.9; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.4; 4788 -4.1; 5267 -1.9; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFocus 8000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFocus 8000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.04 | -3.3 dB |
| Peaking | 177 Hz  | 0.42 | 2.0 dB  |
| Peaking | 639 Hz  | 2.82 | 1.0 dB  |
| Peaking | 3104 Hz | 1.18 | 6.5 dB  |
| Peaking | 5998 Hz | 4.49 | 5.0 dB  |
| Peaking | 1071 Hz | 5.28 | -1.2 dB |
| Peaking | 3184 Hz | 3.68 | -2.7 dB |
| Peaking | 3335 Hz | 1.73 | 2.1 dB  |
| Peaking | 6674 Hz | 7.27 | 2.2 dB  |
| Peaking | 7356 Hz | 1.42 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | 1.3 dB  |
| Peaking | 250 Hz   | 1.41 | 1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20UltraFocus%208000/Polk%20Audio%20UltraFocus%208000.png)