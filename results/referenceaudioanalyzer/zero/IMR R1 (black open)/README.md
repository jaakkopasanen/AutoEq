# IMR R1 (black open)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -18.7; 23 -18.6; 25 -18.5; 28 -18.4; 31 -18.2; 34 -18.0; 37 -17.9; 41 -17.6; 45 -17.4; 49 -17.1; 54 -16.8; 60 -16.5; 66 -16.2; 72 -15.9; 79 -15.5; 87 -15.0; 96 -14.5; 106 -14.0; 116 -13.5; 128 -12.9; 141 -12.3; 155 -11.7; 170 -11.0; 187 -10.3; 206 -9.6; 227 -8.9; 249 -8.3; 274 -7.9; 302 -7.4; 332 -6.8; 365 -6.0; 402 -5.4; 442 -4.7; 486 -4.0; 535 -3.3; 588 -2.7; 647 -2.2; 712 -1.8; 783 -1.4; 861 -1.0; 947 -0.8; 1042 -0.6; 1146 -0.5; 1261 -0.5; 1387 -0.8; 1526 -1.1; 1678 -1.7; 1846 -2.5; 2031 -3.8; 2234 -5.6; 2457 -8.4; 2703 -11.7; 2973 -13.9; 3270 -13.9; 3597 -12.0; 3957 -11.4; 4353 -13.6; 4788 -16.0; 5267 -15.9; 5793 -12.7; 6373 -6.3; 7010 -3.8; 7711 -6.0; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`IMR R1 (black open) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `IMR R1 (black open) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 50 Hz   | 0.27 | -9.3 dB  |
| Peaking | 1816 Hz | 0.31 | 8.4 dB   |
| Peaking | 3028 Hz | 1.58 | -14.2 dB |
| Peaking | 5022 Hz | 3.09 | -12.2 dB |
| Peaking | 17 Hz   | 0.76 | -5.1 dB  |
| Peaking | 28 Hz   | 0.45 | -0.6 dB  |
| Peaking | 5779 Hz | 8.83 | -2.5 dB  |
| Peaking | 6751 Hz | 6.77 | 4.7 dB   |
| Peaking | 9639 Hz | 1.08 | -0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -12.9 dB |
| Peaking | 62 Hz    | 1.41 | -7.2 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 6.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -10.8 dB |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 16000 Hz | 1.41 | -0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/IMR%20R1%20(black%20open)/IMR%20R1%20(black%20open).png)