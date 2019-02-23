# Monster Jamz
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.5; 23 -12.5; 25 -12.4; 28 -12.3; 31 -12.1; 34 -12.0; 37 -11.9; 41 -11.7; 45 -11.5; 49 -11.4; 54 -11.3; 60 -11.1; 66 -11.0; 72 -10.9; 79 -10.9; 87 -10.8; 96 -10.7; 106 -10.5; 116 -10.2; 128 -10.0; 141 -9.9; 155 -9.5; 170 -9.2; 187 -8.8; 206 -8.4; 227 -8.0; 249 -7.5; 274 -7.1; 302 -6.6; 332 -6.2; 365 -5.8; 402 -5.3; 442 -4.8; 486 -4.6; 535 -4.2; 588 -3.6; 647 -3.4; 712 -3.3; 783 -3.1; 861 -3.4; 947 -3.8; 1042 -4.4; 1146 -5.1; 1261 -5.3; 1387 -5.7; 1526 -7.0; 1678 -7.8; 1846 -8.5; 2031 -9.1; 2234 -9.4; 2457 -8.9; 2703 -8.3; 2973 -5.1; 3270 -2.1; 3597 -0.7; 3957 -1.4; 4353 -4.1; 4788 -5.8; 5267 -5.3; 5793 -3.1; 6373 -0.5; 7010 -2.9; 7711 -5.1; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -6.1; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Jamz GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Jamz ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.31 | -6.9 dB |
| Peaking | 132 Hz  | 1.06 | -2.8 dB |
| Peaking | 2264 Hz | 2.29 | -4.9 dB |
| Peaking | 3584 Hz | 3.92 | 6.1 dB  |
| Peaking | 6408 Hz | 6.38 | 5.3 dB  |
| Peaking | 81 Hz   | 3.89 | -0.4 dB |
| Peaking | 243 Hz  | 2.04 | -0.9 dB |
| Peaking | 722 Hz  | 1.15 | 2.6 dB  |
| Peaking | 1671 Hz | 3.95 | -1.5 dB |
| Peaking | 4911 Hz | 8.02 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.2 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Jamz/Monster%20Jamz.png)