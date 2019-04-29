# InEar PhoPhile-8 Treble
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.1; 28 -1.5; 31 -1.8; 34 -2.0; 37 -2.2; 41 -2.5; 45 -2.7; 49 -2.9; 54 -3.1; 60 -3.4; 66 -3.8; 72 -4.1; 79 -4.4; 87 -4.8; 96 -5.2; 106 -5.6; 116 -5.8; 128 -6.1; 141 -6.4; 155 -6.6; 170 -6.8; 187 -6.9; 206 -6.9; 227 -6.9; 249 -6.9; 274 -6.9; 302 -6.9; 332 -6.8; 365 -6.8; 402 -6.7; 442 -6.7; 486 -6.6; 535 -6.5; 588 -6.4; 647 -6.2; 712 -5.9; 783 -5.7; 861 -5.5; 947 -5.5; 1042 -5.9; 1146 -6.6; 1261 -7.4; 1387 -7.8; 1526 -7.7; 1678 -7.1; 1846 -6.3; 2031 -5.6; 2234 -4.8; 2457 -4.1; 2703 -3.6; 2973 -3.7; 3270 -4.1; 3597 -4.0; 3957 -3.5; 4353 -2.9; 4788 -3.3; 5267 -5.1; 5793 -6.6; 6373 -5.6; 7010 -6.7; 7711 -9.1; 8482 -7.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -7.4; 18182 -13.4; 20000 -16.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`InEar PhoPhile-8 Treble GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `InEar PhoPhile-8 Treble ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 24 Hz   |  1.05 | 5.2 dB  |
| Peaking | 53 Hz   |  1.75 | 2.1 dB  |
| Peaking | 2785 Hz |  3.81 | 2.4 dB  |
| Peaking | 4344 Hz |  3.33 | 3.2 dB  |
| Peaking | 7862 Hz |  5.44 | -3.7 dB |
| Peaking | 261 Hz  |  0.78 | -1.1 dB |
| Peaking | 953 Hz  |  2.29 | 1.4 dB  |
| Peaking | 1470 Hz |  1.52 | -2.9 dB |
| Peaking | 2007 Hz |  1.35 | 1.4 dB  |
| Peaking | 5714 Hz | 11.89 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/InEar%20PhoPhile-8%20Treble/InEar%20PhoPhile-8%20Treble.png)