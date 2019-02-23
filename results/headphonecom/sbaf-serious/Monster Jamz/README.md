# Monster Jamz
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.2; 23 -1.8; 25 -2.3; 28 -3.0; 31 -3.6; 34 -4.1; 37 -4.6; 41 -5.2; 45 -5.7; 49 -6.2; 54 -6.7; 60 -7.4; 66 -8.0; 72 -8.5; 79 -9.1; 87 -9.7; 96 -10.2; 106 -10.8; 116 -11.2; 128 -11.7; 141 -12.2; 155 -12.6; 170 -12.8; 187 -13.2; 206 -13.2; 227 -13.0; 249 -12.8; 274 -13.0; 302 -13.0; 332 -12.5; 365 -12.0; 402 -11.5; 442 -11.0; 486 -10.5; 535 -9.8; 588 -9.1; 647 -8.4; 712 -7.9; 783 -7.4; 861 -7.2; 947 -7.1; 1042 -7.0; 1146 -7.0; 1261 -7.1; 1387 -7.2; 1526 -7.5; 1678 -7.2; 1846 -6.9; 2031 -6.5; 2234 -5.7; 2457 -4.4; 2703 -2.9; 2973 -1.4; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -2.1; 4788 -1.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Jamz GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Jamz ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.63 | 6.1 dB  |
| Peaking | 135 Hz  | 0.66 | -3.9 dB |
| Peaking | 295 Hz  | 0.72 | -4.9 dB |
| Peaking | 3441 Hz | 2.15 | 6.2 dB  |
| Peaking | 5713 Hz | 2.85 | 5.8 dB  |
| Peaking | 840 Hz  | 2.59 | 0.8 dB  |
| Peaking | 1748 Hz | 1.88 | -1.1 dB |
| Peaking | 2734 Hz | 4.49 | 1.0 dB  |
| Peaking | 6587 Hz | 7.65 | 2.1 dB  |
| Peaking | 7782 Hz | 2.34 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -6.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Jamz/Monster%20Jamz.png)