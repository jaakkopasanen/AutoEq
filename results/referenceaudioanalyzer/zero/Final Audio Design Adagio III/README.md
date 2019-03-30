# Final Audio Design Adagio III
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -19.8; 23 -19.9; 25 -19.9; 28 -19.9; 31 -19.8; 34 -19.6; 37 -19.5; 41 -19.3; 45 -19.0; 49 -18.8; 54 -18.5; 60 -18.1; 66 -17.8; 72 -17.4; 79 -17.0; 87 -16.5; 96 -15.9; 106 -15.4; 116 -14.7; 128 -14.1; 141 -13.4; 155 -12.7; 170 -12.1; 187 -11.3; 206 -10.6; 227 -9.8; 249 -9.0; 274 -8.2; 302 -7.5; 332 -6.8; 365 -6.1; 402 -5.3; 442 -4.5; 486 -3.6; 535 -2.8; 588 -2.0; 647 -1.4; 712 -0.8; 783 -0.5; 861 -0.5; 947 -0.7; 1042 -1.2; 1146 -1.5; 1261 -1.8; 1387 -2.0; 1526 -2.5; 1678 -3.2; 1846 -4.5; 2031 -6.2; 2234 -8.3; 2457 -9.8; 2703 -10.4; 2973 -10.0; 3270 -8.6; 3597 -7.0; 3957 -6.5; 4353 -7.9; 4788 -10.0; 5267 -9.9; 5793 -6.0; 6373 -0.5; 7010 -3.1; 7711 -5.3; 8482 -5.6; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Design Adagio III GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Design Adagio III ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 0.14 | -14.3 dB |
| Peaking | 853 Hz  | 0.56 | 6.0 dB   |
| Peaking | 2630 Hz | 2.17 | -6.7 dB  |
| Peaking | 5158 Hz | 3.68 | -5.7 dB  |
| Peaking | 6482 Hz | 5.42 | 6.7 dB   |
| Peaking | 1116 Hz | 5.15 | -0.5 dB  |
| Peaking | 1592 Hz | 5.03 | 0.5 dB   |
| Peaking | 5505 Hz | 2.82 | 0.1 dB   |
| Peaking | 6124 Hz | 6.9  | 1.2 dB   |
| Peaking | 6697 Hz | 2.25 | -0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -15.3 dB |
| Peaking | 62 Hz    | 1.41 | -8.8 dB  |
| Peaking | 125 Hz   | 1.41 | -6.7 dB  |
| Peaking | 250 Hz   | 1.41 | -2.6 dB  |
| Peaking | 500 Hz   | 1.41 | 2.4 dB   |
| Peaking | 1000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Final%20Audio%20Design%20Adagio%20III/Final%20Audio%20Design%20Adagio%20III.png)