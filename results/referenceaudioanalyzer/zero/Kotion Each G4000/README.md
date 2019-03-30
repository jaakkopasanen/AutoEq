# Kotion Each G4000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.5; 45 -3.2; 49 -4.9; 54 -6.6; 60 -8.2; 66 -9.2; 72 -9.9; 79 -10.3; 87 -10.6; 96 -10.9; 106 -11.1; 116 -10.9; 128 -10.6; 141 -10.4; 155 -10.2; 170 -10.0; 187 -9.7; 206 -9.5; 227 -9.2; 249 -8.9; 274 -8.7; 302 -8.4; 332 -8.2; 365 -8.1; 402 -8.2; 442 -8.8; 486 -9.8; 535 -11.0; 588 -11.9; 647 -12.8; 712 -13.7; 783 -14.4; 861 -14.9; 947 -14.8; 1042 -14.6; 1146 -14.3; 1261 -13.6; 1387 -11.9; 1526 -9.5; 1678 -6.6; 1846 -3.8; 2031 -1.0; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.0; 4788 -4.1; 5267 -3.6; 5793 -3.6; 6373 -3.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kotion Each G4000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kotion Each G4000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 33 Hz   |  0.67 | 9.5 dB  |
| Peaking | 79 Hz   |  0.61 | -7.5 dB |
| Peaking | 1021 Hz |  0.88 | -9.9 dB |
| Peaking | 2077 Hz |  2.33 | 6.2 dB  |
| Peaking | 3355 Hz |  1.02 | 6.7 dB  |
| Peaking | 396 Hz  |  3.11 | 1.3 dB  |
| Peaking | 625 Hz  |  3.12 | -0.9 dB |
| Peaking | 4771 Hz | 10.26 | -1.6 dB |
| Peaking | 6671 Hz |  3.99 | 3.1 dB  |
| Peaking | 7717 Hz |  2.22 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 8.7 dB   |
| Peaking | 62 Hz    | 1.41 | -3.3 dB  |
| Peaking | 125 Hz   | 1.41 | -4.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -11.4 dB |
| Peaking | 2000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Kotion%20Each%20G4000/Kotion%20Each%20G4000.png)