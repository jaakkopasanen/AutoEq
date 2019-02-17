# Polk Audio UltraFit 2000 sample B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.7; 54 -1.9; 60 -3.5; 66 -4.8; 72 -5.9; 79 -7.0; 87 -8.0; 96 -8.8; 106 -9.2; 116 -9.2; 128 -9.3; 141 -9.2; 155 -9.0; 170 -8.7; 187 -8.3; 206 -7.8; 227 -7.3; 249 -6.9; 274 -6.3; 302 -5.5; 332 -5.5; 365 -4.9; 402 -4.2; 442 -3.5; 486 -3.2; 535 -2.5; 588 -1.6; 647 -1.3; 712 -1.5; 783 -2.4; 861 -4.6; 947 -6.2; 1042 -6.3; 1146 -6.6; 1261 -7.4; 1387 -7.5; 1526 -8.6; 1678 -8.8; 1846 -7.7; 2031 -5.9; 2234 -3.7; 2457 -1.4; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.1; 3957 -1.3; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 2000 sample B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 2000 sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.41 | 7.8 dB  |
| Peaking | 103 Hz  | 0.82 | -7.1 dB |
| Peaking | 597 Hz  | 1.88 | 5.6 dB  |
| Peaking | 2939 Hz | 2.9  | 5.7 dB  |
| Peaking | 5119 Hz | 1.8  | 6.4 dB  |
| Peaking | 373 Hz  | 2.59 | 0.9 dB  |
| Peaking | 1633 Hz | 2.24 | -3.5 dB |
| Peaking | 2401 Hz | 4.5  | 2.4 dB  |
| Peaking | 6475 Hz | 5.39 | 3.0 dB  |
| Peaking | 7685 Hz | 1.98 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 5.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20UltraFit%202000%20sample%20B/Polk%20Audio%20UltraFit%202000%20sample%20B.png)