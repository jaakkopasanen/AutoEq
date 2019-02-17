# Toshiba HR-810 Low Gain
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.9; 106 -2.1; 116 -2.9; 128 -4.1; 141 -5.0; 155 -5.7; 170 -6.2; 187 -6.6; 206 -6.9; 227 -6.9; 249 -6.9; 274 -6.9; 302 -6.8; 332 -6.7; 365 -6.5; 402 -6.4; 442 -6.1; 486 -6.0; 535 -5.9; 588 -5.6; 647 -5.6; 712 -5.7; 783 -5.6; 861 -5.9; 947 -6.4; 1042 -6.3; 1146 -5.5; 1261 -7.6; 1387 -9.3; 1526 -9.7; 1678 -10.3; 1846 -10.0; 2031 -9.9; 2234 -10.6; 2457 -9.4; 2703 -9.2; 2973 -7.5; 3270 -6.3; 3597 -5.4; 3957 -4.3; 4353 -3.7; 4788 -1.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Toshiba HR-810 Low Gain GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Toshiba HR-810 Low Gain ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 57 Hz   | 0.33 | 7.8 dB  |
| Peaking | 635 Hz  | 0.64 | 7.7 dB  |
| Peaking | 1093 Hz | 0.12 | -7.6 dB |
| Peaking | 1133 Hz | 4.7  | 3.2 dB  |
| Peaking | 5201 Hz | 1.05 | 11.5 dB |
| Peaking | 20 Hz   | 2.47 | 1.3 dB  |
| Peaking | 93 Hz   | 6.02 | 1.3 dB  |
| Peaking | 6420 Hz | 4.15 | 3.7 dB  |
| Peaking | 7020 Hz | 1.41 | -3.7 dB |
| Peaking | 8481 Hz | 0.52 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.8 dB  |
| Peaking | 125 Hz   | 1.41 | 2.0 dB  |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Toshiba%20HR-810%20Low%20Gain/Toshiba%20HR-810%20Low%20Gain.png)