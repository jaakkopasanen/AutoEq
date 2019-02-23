# Koss Pro4AA
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.7; 25 -3.3; 28 -3.9; 31 -4.5; 34 -4.9; 37 -5.3; 41 -5.8; 45 -6.1; 49 -6.5; 54 -6.9; 60 -7.4; 66 -7.7; 72 -7.9; 79 -8.4; 87 -9.5; 96 -10.4; 106 -10.4; 116 -11.0; 128 -11.9; 141 -12.4; 155 -12.6; 170 -12.5; 187 -13.1; 206 -13.0; 227 -12.7; 249 -12.2; 274 -11.4; 302 -11.0; 332 -11.3; 365 -10.7; 402 -9.8; 442 -8.7; 486 -8.1; 535 -7.1; 588 -6.0; 647 -5.2; 712 -4.9; 783 -4.4; 861 -4.0; 947 -3.5; 1042 -3.2; 1146 -2.9; 1261 -2.6; 1387 -3.0; 1526 -3.6; 1678 -4.2; 1846 -4.9; 2031 -5.8; 2234 -7.2; 2457 -8.2; 2703 -8.5; 2973 -8.8; 3270 -6.5; 3597 -4.1; 3957 -2.3; 4353 -4.2; 4788 -0.9; 5267 -0.5; 5793 -1.4; 6373 -3.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Pro4AA GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Pro4AA ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 12 Hz   |  0.44 | 5.8 dB  |
| Peaking | 203 Hz  |  0.51 | -6.9 dB |
| Peaking | 1075 Hz |  0.64 | 4.6 dB  |
| Peaking | 2643 Hz |  2.4  | -4.6 dB |
| Peaking | 5156 Hz |  2.02 | 5.9 dB  |
| Peaking | 285 Hz  |  5.74 | 1.0 dB  |
| Peaking | 349 Hz  |  4.5  | -0.8 dB |
| Peaking | 3047 Hz | 11.35 | -1.3 dB |
| Peaking | 3787 Hz |  7.88 | 1.9 dB  |
| Peaking | 8508 Hz |  3.47 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -5.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20Pro4AA/Koss%20Pro4AA.png)