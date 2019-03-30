# IMR R1 (blue close)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.5; 25 -4.7; 28 -4.8; 31 -4.9; 34 -5.0; 37 -5.0; 41 -5.0; 45 -5.0; 49 -5.0; 54 -5.0; 60 -5.0; 66 -5.0; 72 -5.0; 79 -5.0; 87 -5.0; 96 -5.0; 106 -5.0; 116 -5.0; 128 -5.0; 141 -5.0; 155 -5.0; 170 -5.0; 187 -5.0; 206 -5.0; 227 -5.0; 249 -5.0; 274 -5.0; 302 -5.0; 332 -4.7; 365 -4.7; 402 -4.6; 442 -4.3; 486 -4.1; 535 -3.7; 588 -3.2; 647 -2.7; 712 -2.3; 783 -1.9; 861 -1.5; 947 -1.1; 1042 -0.8; 1146 -0.6; 1261 -0.5; 1387 -0.8; 1526 -1.1; 1678 -1.7; 1846 -2.7; 2031 -4.0; 2234 -5.9; 2457 -8.5; 2703 -11.5; 2973 -13.3; 3270 -12.8; 3597 -10.8; 3957 -10.5; 4353 -12.8; 4788 -15.1; 5267 -15.1; 5793 -12.0; 6373 -5.6; 7010 -2.3; 7711 -4.4; 8482 -4.7; 9330 -4.7; 10263 -4.7; 11289 -4.8; 12418 -5.4; 13660 -4.7; 15026 -4.7; 16529 -4.7; 18182 -4.7; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`IMR R1 (blue close) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `IMR R1 (blue close) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 448 Hz  | 0.43 | -1.3 dB  |
| Peaking | 1323 Hz | 0.54 | 5.6 dB   |
| Peaking | 2920 Hz | 2.09 | -9.9 dB  |
| Peaking | 5157 Hz | 2.2  | -11.8 dB |
| Peaking | 6807 Hz | 4.03 | 6.7 dB   |
| Peaking | 14 Hz   | 0.82 | 0.8 dB   |
| Peaking | 35 Hz   | 0.86 | -0.4 dB  |
| Peaking | 6511 Hz | 2.31 | 0.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 4000 Hz  | 1.41 | -11.3 dB |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 16000 Hz | 1.41 | -0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/IMR%20R1%20(blue%20close)/IMR%20R1%20(blue%20close).png)