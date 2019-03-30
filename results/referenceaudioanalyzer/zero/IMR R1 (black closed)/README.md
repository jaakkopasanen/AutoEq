# IMR R1 (black closed)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -18.9; 23 -18.8; 25 -18.7; 28 -18.5; 31 -18.4; 34 -18.2; 37 -18.1; 41 -17.8; 45 -17.6; 49 -17.4; 54 -17.1; 60 -16.8; 66 -16.4; 72 -16.0; 79 -15.6; 87 -15.2; 96 -14.7; 106 -14.2; 116 -13.7; 128 -13.1; 141 -12.5; 155 -11.8; 170 -11.2; 187 -10.4; 206 -9.8; 227 -9.1; 249 -8.5; 274 -8.0; 302 -7.5; 332 -6.9; 365 -6.2; 402 -5.5; 442 -4.8; 486 -4.1; 535 -3.5; 588 -2.8; 647 -2.2; 712 -1.7; 783 -1.2; 861 -1.0; 947 -0.8; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.7; 1526 -1.2; 1678 -1.8; 1846 -2.7; 2031 -4.0; 2234 -5.7; 2457 -8.2; 2703 -11.4; 2973 -13.7; 3270 -13.9; 3597 -12.1; 3957 -11.3; 4353 -13.5; 4788 -16.0; 5267 -16.3; 5793 -13.5; 6373 -7.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`IMR R1 (black closed) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `IMR R1 (black closed) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 48 Hz   | 0.26 | -9.5 dB  |
| Peaking | 1798 Hz | 0.31 | 8.6 dB   |
| Peaking | 3036 Hz | 1.51 | -13.9 dB |
| Peaking | 5084 Hz | 3.03 | -12.2 dB |
| Peaking | 18 Hz   | 0.86 | -5.2 dB  |
| Peaking | 35 Hz   | 0.76 | -0.7 dB  |
| Peaking | 5858 Hz | 8.94 | -2.4 dB  |
| Peaking | 6829 Hz | 6.79 | 4.4 dB   |
| Peaking | 9873 Hz | 1.06 | -0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -12.9 dB |
| Peaking | 62 Hz    | 1.41 | -7.3 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -10.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 16000 Hz | 1.41 | -0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/IMR%20R1%20(black%20closed)/IMR%20R1%20(black%20closed).png)