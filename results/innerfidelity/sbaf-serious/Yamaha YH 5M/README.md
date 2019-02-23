# Yamaha YH 5M
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.1; 31 -1.5; 34 -1.9; 37 -2.2; 41 -2.5; 45 -2.9; 49 -3.2; 54 -3.7; 60 -4.1; 66 -4.5; 72 -5.0; 79 -5.4; 87 -5.9; 96 -6.4; 106 -6.8; 116 -7.1; 128 -7.4; 141 -8.1; 155 -8.2; 170 -8.5; 187 -8.8; 206 -9.0; 227 -9.1; 249 -9.3; 274 -9.4; 302 -9.5; 332 -9.7; 365 -9.9; 402 -10.0; 442 -10.1; 486 -10.6; 535 -10.9; 588 -11.0; 647 -11.4; 712 -12.1; 783 -12.3; 861 -12.2; 947 -11.1; 1042 -10.4; 1146 -8.2; 1261 -6.1; 1387 -4.5; 1526 -2.7; 1678 -2.3; 1846 -4.4; 2031 -4.4; 2234 -3.7; 2457 -1.1; 2703 -0.9; 2973 -1.0; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -3.8; 4788 -5.8; 5267 -7.0; 5793 -6.0; 6373 -8.9; 7010 -4.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha YH 5M GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha YH 5M ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 24 Hz   |  0.98 | 5.9 dB  |
| Peaking | 50 Hz   |  1.5  | 2.0 dB  |
| Peaking | 1292 Hz |  0.24 | -7.1 dB |
| Peaking | 1529 Hz |  2.15 | 7.9 dB  |
| Peaking | 3078 Hz |  1.11 | 11.6 dB |
| Peaking | 2492 Hz |  9.59 | 1.7 dB  |
| Peaking | 3061 Hz |  5.61 | -1.2 dB |
| Peaking | 4099 Hz |  4.72 | 5.5 dB  |
| Peaking | 4460 Hz |  2.48 | -3.6 dB |
| Peaking | 7141 Hz | 10.77 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -3.9 dB |
| Peaking | 1000 Hz  | 1.41 | -4.4 dB |
| Peaking | 2000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20YH%205M/Yamaha%20YH%205M.png)