# Final Audio Design Piano Forte IX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -1.0; 54 -1.9; 60 -2.9; 66 -3.7; 72 -4.4; 79 -5.3; 87 -6.1; 96 -6.8; 106 -7.5; 116 -8.1; 128 -8.6; 141 -8.9; 155 -9.2; 170 -9.2; 187 -9.2; 206 -9.2; 227 -9.0; 249 -8.7; 274 -8.2; 302 -7.7; 332 -7.2; 365 -6.7; 402 -6.2; 442 -5.7; 486 -5.4; 535 -5.0; 588 -5.0; 647 -5.0; 712 -5.0; 783 -5.0; 861 -5.0; 947 -5.0; 1042 -5.0; 1146 -5.0; 1261 -5.0; 1387 -4.7; 1526 -4.7; 1678 -6.2; 1846 -9.0; 2031 -12.3; 2234 -15.8; 2457 -17.9; 2703 -18.0; 2973 -16.4; 3270 -14.6; 3597 -15.0; 3957 -17.2; 4353 -17.6; 4788 -13.8; 5267 -4.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Design Piano Forte IX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Design Piano Forte IX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 34 Hz   | 0.47 | 6.9 dB   |
| Peaking | 149 Hz  | 0.67 | -4.4 dB  |
| Peaking | 2571 Hz | 1.58 | -19.3 dB |
| Peaking | 2662 Hz | 0.33 | 7.6 dB   |
| Peaking | 4176 Hz | 3.79 | -13.4 dB |
| Peaking | 3610 Hz | 3.15 | -1.9 dB  |
| Peaking | 4167 Hz | 7.86 | 3.2 dB   |
| Peaking | 4734 Hz | 4.63 | -7.4 dB  |
| Peaking | 5764 Hz | 2    | 10.4 dB  |
| Peaking | 7626 Hz | 1.02 | -4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | -9.7 dB |
| Peaking | 8000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Final%20Audio%20Design%20Piano%20Forte%20IX/Final%20Audio%20Design%20Piano%20Forte%20IX.png)