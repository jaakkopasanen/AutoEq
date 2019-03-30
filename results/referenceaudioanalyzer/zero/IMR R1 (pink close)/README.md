# IMR R1 (pink close)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -9.0; 25 -9.1; 28 -9.2; 31 -9.3; 34 -9.3; 37 -9.3; 41 -9.2; 45 -9.0; 49 -8.9; 54 -8.9; 60 -8.9; 66 -9.0; 72 -8.9; 79 -8.7; 87 -8.6; 96 -8.4; 106 -8.3; 116 -8.2; 128 -8.0; 141 -7.8; 155 -7.5; 170 -7.2; 187 -7.0; 206 -6.7; 227 -6.6; 249 -6.4; 274 -6.1; 302 -5.7; 332 -5.4; 365 -4.9; 402 -4.4; 442 -4.0; 486 -3.5; 535 -3.0; 588 -2.4; 647 -1.9; 712 -1.6; 783 -1.2; 861 -0.9; 947 -0.6; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.7; 1526 -1.2; 1678 -1.9; 1846 -2.9; 2031 -4.3; 2234 -6.3; 2457 -8.8; 2703 -11.0; 2973 -11.7; 3270 -10.7; 3597 -9.0; 3957 -9.3; 4353 -11.8; 4788 -13.9; 5267 -13.5; 5793 -10.2; 6373 -4.4; 7010 -2.4; 7711 -4.6; 8482 -4.9; 9330 -4.9; 10263 -4.9; 11289 -4.9; 12418 -4.9; 13660 -4.9; 15026 -4.9; 16529 -4.9; 18182 -4.9; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`IMR R1 (pink close) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `IMR R1 (pink close) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 25 Hz   | 0.1  | -4.2 dB  |
| Peaking | 1230 Hz | 0.52 | 5.3 dB   |
| Peaking | 2806 Hz | 2.1  | -8.5 dB  |
| Peaking | 5082 Hz | 2.36 | -10.2 dB |
| Peaking | 6737 Hz | 4.42 | 6.1 dB   |
| Peaking | 179 Hz  | 2.35 | 0.3 dB   |
| Peaking | 288 Hz  | 2.25 | -0.3 dB  |
| Peaking | 9959 Hz | 2.58 | 0.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -8.9 dB |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/IMR%20R1%20(pink%20close)/IMR%20R1%20(pink%20close).png)