# Polk Audio UltraFit 3000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.3; 23 -15.3; 25 -15.3; 28 -15.4; 31 -15.4; 34 -15.5; 37 -15.5; 41 -15.6; 45 -15.6; 49 -15.7; 54 -15.8; 60 -16.0; 66 -16.2; 72 -16.3; 79 -16.5; 87 -16.7; 96 -16.9; 106 -16.9; 116 -16.8; 128 -16.8; 141 -16.7; 155 -16.5; 170 -16.3; 187 -15.9; 206 -15.6; 227 -15.1; 249 -14.6; 274 -14.0; 302 -13.4; 332 -12.8; 365 -12.1; 402 -11.4; 442 -10.6; 486 -10.0; 535 -9.3; 588 -8.2; 647 -7.5; 712 -7.0; 783 -6.4; 861 -6.4; 947 -6.3; 1042 -5.7; 1146 -5.6; 1261 -5.6; 1387 -5.9; 1526 -6.3; 1678 -6.5; 1846 -6.1; 2031 -5.7; 2234 -5.0; 2457 -3.4; 2703 -2.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -3.1; 4788 -5.2; 5267 -2.3; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 3000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 3000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 28 Hz    |  0.22 | -8.4 dB |
| Peaking | 144 Hz   |  0.7  | -5.7 dB |
| Peaking | 301 Hz   |  1.24 | -3.2 dB |
| Peaking | 3305 Hz  |  1.83 | 6.6 dB  |
| Peaking | 6018 Hz  |  4.44 | 5.7 dB  |
| Peaking | 478 Hz   |  2.58 | -1.0 dB |
| Peaking | 1438 Hz  |  0.7  | 2.2 dB  |
| Peaking | 1761 Hz  |  1.53 | -2.8 dB |
| Peaking | 4751 Hz  | 11.96 | -2.2 dB |
| Peaking | 20874 Hz |  1.63 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.8 dB |
| Peaking | 62 Hz    | 1.41 | -6.8 dB |
| Peaking | 125 Hz   | 1.41 | -8.6 dB |
| Peaking | 250 Hz   | 1.41 | -6.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20UltraFit%203000/Polk%20Audio%20UltraFit%203000.png)