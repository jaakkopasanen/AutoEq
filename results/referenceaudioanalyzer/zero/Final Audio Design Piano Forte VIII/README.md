# Final Audio Design Piano Forte VIII
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.8; 54 -1.6; 60 -2.6; 66 -3.5; 72 -4.3; 79 -5.1; 87 -5.9; 96 -6.7; 106 -7.4; 116 -8.0; 128 -8.6; 141 -9.0; 155 -9.3; 170 -9.4; 187 -9.4; 206 -9.4; 227 -9.4; 249 -9.4; 274 -9.0; 302 -8.7; 332 -8.3; 365 -7.8; 402 -7.3; 442 -6.9; 486 -6.5; 535 -6.2; 588 -5.8; 647 -5.5; 712 -5.5; 783 -5.2; 861 -5.2; 947 -5.2; 1042 -5.2; 1146 -5.1; 1261 -4.6; 1387 -4.2; 1526 -4.6; 1678 -5.8; 1846 -7.7; 2031 -11.3; 2234 -15.7; 2457 -18.0; 2703 -17.7; 2973 -15.6; 3270 -14.0; 3597 -15.0; 3957 -17.1; 4353 -17.0; 4788 -11.8; 5267 -3.1; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Design Piano Forte VIII GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Design Piano Forte VIII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 39 Hz   | 0.39 | 7.8 dB   |
| Peaking | 141 Hz  | 0.47 | -5.6 dB  |
| Peaking | 2565 Hz | 1.81 | -19.4 dB |
| Peaking | 2744 Hz | 0.37 | 7.9 dB   |
| Peaking | 4072 Hz | 3.65 | -13.9 dB |
| Peaking | 1555 Hz | 3.45 | 2.0 dB   |
| Peaking | 4696 Hz | 6.35 | -7.3 dB  |
| Peaking | 5349 Hz | 0.31 | -2.1 dB  |
| Peaking | 5742 Hz | 1.53 | 9.7 dB   |
| Peaking | 7652 Hz | 1.8  | -4.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | -9.0 dB |
| Peaking | 8000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Final%20Audio%20Design%20Piano%20Forte%20VIII/Final%20Audio%20Design%20Piano%20Forte%20VIII.png)