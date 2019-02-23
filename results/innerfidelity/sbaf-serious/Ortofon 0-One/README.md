# Ortofon 0-One
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.2; 31 -2.2; 34 -3.0; 37 -3.6; 41 -4.2; 45 -4.6; 49 -4.9; 54 -4.8; 60 -4.2; 66 -4.5; 72 -6.0; 79 -7.0; 87 -7.6; 96 -7.7; 106 -7.7; 116 -7.8; 128 -7.9; 141 -7.7; 155 -7.3; 170 -7.0; 187 -6.4; 206 -5.8; 227 -4.8; 249 -3.9; 274 -3.4; 302 -3.5; 332 -5.6; 365 -8.1; 402 -9.8; 442 -10.6; 486 -11.0; 535 -10.7; 588 -10.3; 647 -8.1; 712 -7.3; 783 -8.8; 861 -9.5; 947 -9.8; 1042 -10.1; 1146 -8.2; 1261 -8.5; 1387 -9.4; 1526 -10.5; 1678 -9.9; 1846 -7.2; 2031 -4.0; 2234 -0.6; 2457 -1.2; 2703 -1.2; 2973 -0.5; 3270 -0.5; 3597 -3.5; 3957 -7.1; 4353 -3.7; 4788 -5.9; 5267 -7.7; 5793 -3.7; 6373 -1.3; 7010 -4.0; 7711 -6.7; 8482 -9.8; 9330 -10.3; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.8; 16529 -10.3; 18182 -11.5; 20000 -16.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ortofon 0-One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ortofon 0-One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.19 | 6.3 dB  |
| Peaking | 494 Hz   | 3.3  | -4.7 dB |
| Peaking | 1615 Hz  | 0.98 | -4.8 dB |
| Peaking | 2216 Hz  | 3.74 | 7.3 dB  |
| Peaking | 3030 Hz  | 2.38 | 7.0 dB  |
| Peaking | 122 Hz   | 1.62 | -1.9 dB |
| Peaking | 284 Hz   | 2.31 | 4.4 dB  |
| Peaking | 389 Hz   | 3.95 | -2.7 dB |
| Peaking | 6246 Hz  | 7.73 | 6.4 dB  |
| Peaking | 20251 Hz | 0.51 | -9.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | 3.8 dB  |
| Peaking | 500 Hz   | 1.41 | -4.0 dB |
| Peaking | 1000 Hz  | 1.41 | -3.4 dB |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -4.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ortofon%200-One/Ortofon%200-One.png)