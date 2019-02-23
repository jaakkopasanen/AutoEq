# Toshiba HR-810 Low Gain
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -1.4; 96 -2.8; 106 -4.0; 116 -4.8; 128 -6.0; 141 -6.9; 155 -7.6; 170 -8.1; 187 -8.5; 206 -8.8; 227 -8.8; 249 -8.8; 274 -8.8; 302 -8.7; 332 -8.6; 365 -8.4; 402 -8.3; 442 -7.9; 486 -7.9; 535 -7.8; 588 -7.5; 647 -7.5; 712 -7.6; 783 -7.5; 861 -7.8; 947 -8.3; 1042 -8.2; 1146 -7.4; 1261 -9.5; 1387 -11.2; 1526 -11.6; 1678 -12.2; 1846 -11.9; 2031 -11.8; 2234 -12.5; 2457 -11.3; 2703 -11.1; 2973 -9.4; 3270 -8.2; 3597 -7.3; 3957 -6.2; 4353 -5.6; 4788 -3.6; 5267 -1.7; 5793 -0.8; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Toshiba HR-810 Low Gain GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Toshiba HR-810 Low Gain ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 63 Hz   | 0.3  | 8.3 dB  |
| Peaking | 186 Hz  | 0.59 | -7.1 dB |
| Peaking | 1548 Hz | 2.46 | -3.7 dB |
| Peaking | 2314 Hz | 1.65 | -5.1 dB |
| Peaking | 5741 Hz | 2.55 | 6.6 dB  |
| Peaking | 18 Hz   | 1.23 | 2.0 dB  |
| Peaking | 44 Hz   | 0.57 | -1.0 dB |
| Peaking | 79 Hz   | 3.56 | 1.6 dB  |
| Peaking | 6588 Hz | 7.77 | 2.0 dB  |
| Peaking | 7727 Hz | 2.57 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 6.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -7.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Toshiba%20HR-810%20Low%20Gain/Toshiba%20HR-810%20Low%20Gain.png)