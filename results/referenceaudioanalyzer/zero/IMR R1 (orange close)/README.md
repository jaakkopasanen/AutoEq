# IMR R1 (orange close)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.1; 25 -5.2; 28 -5.3; 31 -5.3; 34 -5.4; 37 -5.4; 41 -5.4; 45 -5.4; 49 -5.4; 54 -5.4; 60 -5.4; 66 -5.4; 72 -5.4; 79 -5.4; 87 -5.4; 96 -5.4; 106 -5.4; 116 -5.4; 128 -5.4; 141 -5.4; 155 -5.4; 170 -5.4; 187 -5.4; 206 -5.4; 227 -5.4; 249 -5.4; 274 -5.4; 302 -5.2; 332 -5.1; 365 -5.1; 402 -5.0; 442 -4.8; 486 -4.5; 535 -4.1; 588 -3.6; 647 -3.1; 712 -2.7; 783 -2.3; 861 -1.8; 947 -1.3; 1042 -1.0; 1146 -0.7; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.8; 1846 -1.2; 2031 -1.7; 2234 -2.3; 2457 -3.0; 2703 -3.7; 2973 -4.2; 3270 -4.4; 3597 -5.0; 3957 -6.8; 4353 -9.7; 4788 -11.9; 5267 -11.9; 5793 -9.4; 6373 -4.8; 7010 -1.4; 7711 -3.3; 8482 -3.6; 9330 -3.6; 10263 -3.6; 11289 -3.6; 12418 -3.6; 13660 -3.6; 15026 -3.6; 16529 -3.6; 18182 -3.6; 20000 -3.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`IMR R1 (orange close) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `IMR R1 (orange close) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 66 Hz   | 0.15 | -1.8 dB |
| Peaking | 398 Hz  | 0.87 | -1.0 dB |
| Peaking | 1305 Hz | 0.78 | 3.7 dB  |
| Peaking | 5077 Hz | 2.19 | -9.9 dB |
| Peaking | 6905 Hz | 4.32 | 5.0 dB  |
| Peaking | 3571 Hz | 2.11 | -1.1 dB |
| Peaking | 3577 Hz | 4.76 | 1.8 dB  |
| Peaking | 9955 Hz | 2.05 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -6.3 dB |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/IMR%20R1%20(orange%20close)/IMR%20R1%20(orange%20close).png)