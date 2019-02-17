# RHA T20 Treble Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -10.0; 25 -10.2; 28 -10.5; 31 -10.7; 34 -10.8; 37 -10.8; 41 -10.9; 45 -10.9; 49 -11.0; 54 -11.0; 60 -11.0; 66 -11.0; 72 -11.0; 79 -11.0; 87 -11.1; 96 -11.1; 106 -10.9; 116 -10.7; 128 -10.6; 141 -10.3; 155 -10.1; 170 -9.7; 187 -9.3; 206 -9.0; 227 -8.5; 249 -8.0; 274 -7.5; 302 -7.1; 332 -6.6; 365 -6.1; 402 -5.6; 442 -5.1; 486 -4.9; 535 -4.5; 588 -3.9; 647 -3.7; 712 -3.7; 783 -3.5; 861 -3.9; 947 -4.3; 1042 -4.9; 1146 -5.5; 1261 -6.4; 1387 -7.9; 1526 -9.0; 1678 -8.0; 1846 -4.9; 2031 -7.2; 2234 -8.3; 2457 -9.7; 2703 -11.0; 2973 -10.5; 3270 -8.9; 3597 -8.0; 3957 -9.6; 4353 -14.0; 4788 -15.6; 5267 -9.5; 5793 -3.6; 6373 -0.5; 7010 -2.2; 7711 -4.4; 8482 -4.7; 9330 -4.7; 10263 -4.7; 11289 -4.7; 12418 -4.7; 13660 -5.1; 15026 -5.3; 16529 -4.7; 18182 -4.7; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA T20 Treble Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T20 Treble Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 36 Hz   | 0.42 | -5.8 dB  |
| Peaking | 112 Hz  | 0.95 | -3.5 dB  |
| Peaking | 209 Hz  | 1.61 | -2.1 dB  |
| Peaking | 2688 Hz | 1.88 | -5.8 dB  |
| Peaking | 4624 Hz | 6.08 | -11.4 dB |
| Peaking | 747 Hz  | 1.78 | 1.8 dB   |
| Peaking | 1561 Hz | 3.06 | -4.2 dB  |
| Peaking | 1862 Hz | 6.15 | 3.6 dB   |
| Peaking | 5071 Hz | 7.47 | -3.1 dB  |
| Peaking | 6384 Hz | 4.36 | 5.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | -7.1 dB |
| Peaking | 8000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T20%20Treble%20Filter/RHA%20T20%20Treble%20Filter.png)