# Audeze LCD-3 Fazor sn2715432
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -0.8; 37 -1.1; 41 -1.4; 45 -2.0; 49 -2.6; 54 -3.2; 60 -3.9; 66 -4.2; 72 -4.4; 79 -4.6; 87 -4.9; 96 -5.3; 106 -5.4; 116 -5.7; 128 -5.9; 141 -6.2; 155 -6.4; 170 -6.5; 187 -6.6; 206 -6.7; 227 -6.7; 249 -6.9; 274 -6.8; 302 -6.8; 332 -6.9; 365 -6.9; 402 -7.0; 442 -6.8; 486 -6.9; 535 -6.8; 588 -6.4; 647 -6.6; 712 -6.4; 783 -6.3; 861 -6.7; 947 -6.7; 1042 -6.3; 1146 -6.3; 1261 -6.5; 1387 -7.5; 1526 -8.2; 1678 -8.2; 1846 -7.3; 2031 -7.2; 2234 -6.3; 2457 -4.8; 2703 -4.1; 2973 -3.3; 3270 -2.6; 3597 -1.7; 3957 -0.6; 4353 -1.0; 4788 -2.8; 5267 -4.1; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -10.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 Fazor sn2715432 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 Fazor sn2715432 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.59 | 6.3 dB  |
| Peaking | 264 Hz  | 0.8  | -0.6 dB |
| Peaking | 1652 Hz | 3.18 | -2.3 dB |
| Peaking | 3836 Hz | 1.85 | 5.7 dB  |
| Peaking | 6088 Hz | 4.9  | 5.3 dB  |
| Peaking | 1177 Hz | 7.38 | 0.5 dB  |
| Peaking | 2124 Hz | 9.38 | -1.0 dB |
| Peaking | 2567 Hz | 5.05 | 0.8 dB  |
| Peaking | 6735 Hz | 8.49 | 1.8 dB  |
| Peaking | 7678 Hz | 1.92 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20Fazor%20sn2715432/Audeze%20LCD-3%20Fazor%20sn2715432.png)