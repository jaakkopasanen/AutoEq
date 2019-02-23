# RHA T20 Treble Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.8; 23 -9.1; 25 -9.3; 28 -9.6; 31 -9.8; 34 -9.9; 37 -9.9; 41 -10.0; 45 -10.0; 49 -10.1; 54 -10.1; 60 -10.1; 66 -10.1; 72 -10.2; 79 -10.2; 87 -10.2; 96 -10.2; 106 -10.0; 116 -9.8; 128 -9.7; 141 -9.4; 155 -9.2; 170 -8.9; 187 -8.5; 206 -8.1; 227 -7.6; 249 -7.1; 274 -6.7; 302 -6.2; 332 -5.7; 365 -5.3; 402 -4.8; 442 -4.2; 486 -4.0; 535 -3.7; 588 -3.0; 647 -2.8; 712 -2.9; 783 -2.7; 861 -3.0; 947 -3.4; 1042 -4.0; 1146 -4.6; 1261 -5.5; 1387 -7.1; 1526 -8.1; 1678 -7.1; 1846 -4.0; 2031 -6.3; 2234 -7.5; 2457 -8.9; 2703 -10.1; 2973 -9.6; 3270 -8.0; 3597 -7.1; 3957 -8.7; 4353 -13.1; 4788 -14.8; 5267 -8.6; 5793 -2.7; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA T20 Treble Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T20 Treble Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 63 Hz   | 0.3  | -4.5 dB  |
| Peaking | 635 Hz  | 1.05 | 3.8 dB   |
| Peaking | 2717 Hz | 3.48 | -4.3 dB  |
| Peaking | 4692 Hz | 4.45 | -10.6 dB |
| Peaking | 6185 Hz | 4.12 | 7.3 dB   |
| Peaking | 896 Hz  | 4.27 | 0.7 dB   |
| Peaking | 1131 Hz | 3.59 | 0.6 dB   |
| Peaking | 1558 Hz | 3.33 | -3.2 dB  |
| Peaking | 1855 Hz | 8.06 | 3.6 dB   |
| Peaking | 7964 Hz | 6.78 | -0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | -4.9 dB |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T20%20Treble%20Filter/RHA%20T20%20Treble%20Filter.png)