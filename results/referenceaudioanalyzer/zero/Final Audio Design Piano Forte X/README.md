# Final Audio Design Piano Forte X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -1.0; 31 -1.8; 34 -2.7; 37 -3.4; 41 -4.2; 45 -4.9; 49 -5.5; 54 -6.3; 60 -7.0; 66 -7.7; 72 -8.3; 79 -8.9; 87 -9.4; 96 -9.7; 106 -9.9; 116 -10.1; 128 -10.4; 141 -10.5; 155 -10.5; 170 -10.5; 187 -10.5; 206 -10.5; 227 -10.5; 249 -10.3; 274 -10.1; 302 -9.7; 332 -9.4; 365 -9.1; 402 -8.8; 442 -8.4; 486 -8.1; 535 -7.7; 588 -7.3; 647 -7.0; 712 -6.9; 783 -6.8; 861 -6.6; 947 -6.6; 1042 -6.6; 1146 -6.4; 1261 -5.9; 1387 -4.7; 1526 -2.5; 1678 -0.7; 1846 -3.1; 2031 -8.3; 2234 -13.5; 2457 -16.1; 2703 -15.8; 2973 -13.5; 3270 -11.6; 3597 -12.4; 3957 -15.1; 4353 -15.8; 4788 -12.0; 5267 -2.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Design Piano Forte X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Design Piano Forte X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 0.72 | 6.9 dB   |
| Peaking | 1831 Hz | 0.45 | 39.1 dB  |
| Peaking | 2254 Hz | 0.27 | -46.3 dB |
| Peaking | 4674 Hz | 0.7  | -32.0 dB |
| Peaking | 5475 Hz | 0.54 | 43.3 dB  |
| Peaking | 1196 Hz | 1.98 | -2.0 dB  |
| Peaking | 2620 Hz | 6.33 | -2.6 dB  |
| Peaking | 3332 Hz | 0.31 | 1.6 dB   |
| Peaking | 6452 Hz | 4.89 | 3.9 dB   |
| Peaking | 6644 Hz | 1.1  | -3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | -8.1 dB |
| Peaking | 8000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Final%20Audio%20Design%20Piano%20Forte%20X/Final%20Audio%20Design%20Piano%20Forte%20X.png)