# Polk Audio UltraFit 3000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.8; 23 -15.8; 25 -15.8; 28 -15.9; 31 -15.9; 34 -16.0; 37 -16.0; 41 -16.1; 45 -16.1; 49 -16.2; 54 -16.3; 60 -16.5; 66 -16.7; 72 -16.8; 79 -17.0; 87 -17.2; 96 -17.4; 106 -17.4; 116 -17.3; 128 -17.3; 141 -17.2; 155 -17.1; 170 -16.8; 187 -16.4; 206 -16.1; 227 -15.6; 249 -15.1; 274 -14.5; 302 -13.9; 332 -13.3; 365 -12.6; 402 -11.9; 442 -11.1; 486 -10.5; 535 -9.8; 588 -8.7; 647 -8.0; 712 -7.5; 783 -7.0; 861 -6.9; 947 -6.8; 1042 -6.2; 1146 -6.1; 1261 -6.1; 1387 -6.4; 1526 -6.8; 1678 -7.0; 1846 -6.7; 2031 -6.2; 2234 -5.5; 2457 -3.9; 2703 -2.5; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -3.6; 4788 -5.7; 5267 -2.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 3000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 3000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 25 Hz   |  0.2  | -8.8 dB |
| Peaking | 144 Hz  |  0.63 | -6.2 dB |
| Peaking | 309 Hz  |  1.09 | -3.3 dB |
| Peaking | 3332 Hz |  2.18 | 6.7 dB  |
| Peaking | 6038 Hz |  4.51 | 6.0 dB  |
| Peaking | 1152 Hz |  1.52 | 1.1 dB  |
| Peaking | 1760 Hz |  2.05 | -1.4 dB |
| Peaking | 2720 Hz |  4.61 | 0.8 dB  |
| Peaking | 4751 Hz | 13.06 | -2.1 dB |
| Peaking | 8253 Hz |  5.43 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.4 dB |
| Peaking | 62 Hz    | 1.41 | -7.2 dB |
| Peaking | 125 Hz   | 1.41 | -8.9 dB |
| Peaking | 250 Hz   | 1.41 | -7.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20UltraFit%203000/Polk%20Audio%20UltraFit%203000.png)