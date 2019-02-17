# Polk Audio UltraFit 2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.3; 66 -2.6; 72 -3.8; 79 -4.9; 87 -6.0; 96 -6.9; 106 -7.4; 116 -7.6; 128 -7.7; 141 -7.7; 155 -7.5; 170 -7.2; 187 -6.8; 206 -6.4; 227 -6.0; 249 -5.5; 274 -5.0; 302 -4.4; 332 -3.9; 365 -3.4; 402 -2.8; 442 -2.0; 486 -1.6; 535 -0.9; 588 -0.5; 647 -0.5; 712 -0.5; 783 -0.5; 861 -2.7; 947 -5.4; 1042 -7.0; 1146 -7.6; 1261 -8.3; 1387 -8.6; 1526 -9.2; 1678 -9.4; 1846 -9.1; 2031 -8.0; 2234 -6.3; 2457 -4.1; 2703 -2.3; 2973 -0.8; 3270 -1.0; 3597 -2.6; 3957 -2.9; 4353 -1.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.3; 9330 -8.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 37 Hz   | 0.68 | 7.6 dB   |
| Peaking | 582 Hz  | 0.5  | 18.9 dB  |
| Peaking | 921 Hz  | 0.14 | -13.0 dB |
| Peaking | 2958 Hz | 1.96 | 9.9 dB   |
| Peaking | 5341 Hz | 1.33 | 11.3 dB  |
| Peaking | 59 Hz   | 3.91 | 1.9 dB   |
| Peaking | 106 Hz  | 1.64 | -1.1 dB  |
| Peaking | 245 Hz  | 2.3  | 1.1 dB   |
| Peaking | 793 Hz  | 8.42 | 2.3 dB   |
| Peaking | 8864 Hz | 8.36 | -1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 6.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20UltraFit%202000/Polk%20Audio%20UltraFit%202000.png)