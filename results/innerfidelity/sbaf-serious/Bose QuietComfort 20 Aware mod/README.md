# Bose QuietComfort 20 Aware mod
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -4.0; 25 -5.2; 28 -6.3; 31 -6.9; 34 -7.0; 37 -7.0; 41 -6.8; 45 -6.6; 49 -6.4; 54 -6.3; 60 -6.3; 66 -6.5; 72 -6.9; 79 -7.4; 87 -8.0; 96 -8.6; 106 -8.8; 116 -8.9; 128 -8.9; 141 -8.9; 155 -8.8; 170 -8.9; 187 -8.9; 206 -8.9; 227 -8.7; 249 -8.6; 274 -8.4; 302 -8.2; 332 -8.2; 365 -8.1; 402 -8.2; 442 -8.1; 486 -8.1; 535 -7.8; 588 -7.2; 647 -7.2; 712 -7.3; 783 -6.6; 861 -6.2; 947 -6.1; 1042 -6.8; 1146 -7.6; 1261 -8.8; 1387 -10.4; 1526 -11.9; 1678 -12.6; 1846 -11.5; 2031 -10.0; 2234 -9.0; 2457 -8.0; 2703 -7.4; 2973 -5.5; 3270 -4.1; 3597 -4.5; 3957 -6.7; 4353 -8.4; 4788 -5.0; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -5.1; 7711 -10.1; 8482 -8.4; 9330 -7.3; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 20 Aware mod GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 Aware mod ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 181 Hz  |  0.61 | -2.6 dB |
| Peaking | 1691 Hz |  2.35 | -6.4 dB |
| Peaking | 3305 Hz |  7.41 | 3.1 dB  |
| Peaking | 5989 Hz |  3.17 | 7.7 dB  |
| Peaking | 7793 Hz |  4.49 | -5.5 dB |
| Peaking | 20 Hz   |  2.8  | 4.5 dB  |
| Peaking | 478 Hz  |  3.45 | -0.7 dB |
| Peaking | 925 Hz  |  4.18 | 1.5 dB  |
| Peaking | 4369 Hz |  7.65 | -3.6 dB |
| Peaking | 5188 Hz | 10.03 | 2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2020%20Aware%20mod/Bose%20QuietComfort%2020%20Aware%20mod.png)