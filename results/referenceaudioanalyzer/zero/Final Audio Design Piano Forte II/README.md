# Final Audio Design Piano Forte II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -1.8; 170 -4.2; 187 -5.9; 206 -6.8; 227 -7.4; 249 -7.7; 274 -7.9; 302 -8.2; 332 -8.6; 365 -8.5; 402 -8.1; 442 -7.5; 486 -6.9; 535 -6.4; 588 -6.0; 647 -5.9; 712 -5.7; 783 -5.5; 861 -5.6; 947 -5.9; 1042 -6.5; 1146 -7.5; 1261 -9.2; 1387 -11.7; 1526 -13.7; 1678 -13.4; 1846 -10.0; 2031 -4.3; 2234 -3.0; 2457 -6.8; 2703 -10.6; 2973 -13.3; 3270 -13.8; 3597 -11.8; 3957 -9.1; 4353 -8.2; 4788 -9.3; 5267 -11.5; 5793 -12.6; 6373 -11.4; 7010 -8.9; 7711 -6.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Design Piano Forte II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Design Piano Forte II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 51 Hz   | 0.45 | 7.1 dB  |
| Peaking | 1608 Hz | 3.13 | -8.7 dB |
| Peaking | 2162 Hz | 4.03 | 7.5 dB  |
| Peaking | 3112 Hz | 2.93 | -8.0 dB |
| Peaking | 5833 Hz | 3.69 | -6.2 dB |
| Peaking | 17 Hz   | 1.3  | 2.6 dB  |
| Peaking | 46 Hz   | 1.53 | -1.3 dB |
| Peaking | 136 Hz  | 1.58 | 5.5 dB  |
| Peaking | 231 Hz  | 0.63 | -4.1 dB |
| Peaking | 740 Hz  | 1.45 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.2 dB  |
| Peaking | 125 Hz   | 1.41 | 6.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | -4.8 dB |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Final%20Audio%20Design%20Piano%20Forte%20II/Final%20Audio%20Design%20Piano%20Forte%20II.png)