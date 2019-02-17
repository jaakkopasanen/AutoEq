# Fischer Audio FA-003
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -2.4; 25 -2.8; 28 -3.5; 31 -4.0; 34 -4.5; 37 -4.8; 41 -5.2; 45 -5.5; 49 -5.7; 54 -5.9; 60 -6.0; 66 -6.0; 72 -6.1; 79 -6.3; 87 -7.0; 96 -8.3; 106 -9.2; 116 -9.3; 128 -9.9; 141 -10.2; 155 -10.1; 170 -9.5; 187 -9.6; 206 -8.8; 227 -7.3; 249 -5.3; 274 -2.4; 302 -0.5; 332 -1.7; 365 -3.6; 402 -4.3; 442 -5.6; 486 -6.2; 535 -6.5; 588 -6.3; 647 -6.4; 712 -6.2; 783 -5.5; 861 -5.5; 947 -5.4; 1042 -4.8; 1146 -4.4; 1261 -4.1; 1387 -4.4; 1526 -4.7; 1678 -5.1; 1846 -5.2; 2031 -5.3; 2234 -5.2; 2457 -5.4; 2703 -5.9; 2973 -6.7; 3270 -5.0; 3597 -5.0; 3957 -6.8; 4353 -8.6; 4788 -8.6; 5267 -7.4; 5793 -8.9; 6373 -5.4; 7010 -2.5; 7711 -4.7; 8482 -5.0; 9330 -5.0; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -5.0; 16529 -5.0; 18182 -5.9; 20000 -9.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio FA-003 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio FA-003 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.43 | 3.4 dB  |
| Peaking | 157 Hz  | 0.88 | -5.7 dB |
| Peaking | 302 Hz  | 2.88 | 7.0 dB  |
| Peaking | 563 Hz  | 2.46 | -1.5 dB |
| Peaking | 4761 Hz | 2.99 | -4.0 dB |
| Peaking | 1262 Hz | 4.03 | 1.1 dB  |
| Peaking | 3013 Hz | 5.06 | -1.7 dB |
| Peaking | 3419 Hz | 6.26 | 1.9 dB  |
| Peaking | 5978 Hz | 7.68 | -3.8 dB |
| Peaking | 6762 Hz | 6.96 | 4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | 1.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.7 dB |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fischer%20Audio%20FA-003/Fischer%20Audio%20FA-003.png)