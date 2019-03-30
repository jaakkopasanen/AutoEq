# Ferrari Cavallino T350
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.4; 25 -2.6; 28 -2.8; 31 -3.2; 34 -3.6; 37 -4.0; 41 -4.5; 45 -4.9; 49 -5.2; 54 -5.4; 60 -5.5; 66 -5.4; 72 -5.4; 79 -5.4; 87 -5.7; 96 -5.8; 106 -5.8; 116 -6.1; 128 -6.1; 141 -6.1; 155 -6.1; 170 -6.2; 187 -6.4; 206 -6.4; 227 -6.3; 249 -6.1; 274 -6.1; 302 -5.9; 332 -5.8; 365 -5.7; 402 -5.4; 442 -4.8; 486 -4.2; 535 -3.7; 588 -3.2; 647 -2.5; 712 -1.8; 783 -1.6; 861 -2.0; 947 -2.8; 1042 -3.9; 1146 -5.2; 1261 -6.6; 1387 -7.2; 1526 -6.6; 1678 -5.1; 1846 -3.7; 2031 -1.8; 2234 -0.5; 2457 -0.6; 2703 -0.7; 2973 -0.6; 3270 -0.8; 3597 -1.8; 3957 -4.5; 4353 -10.0; 4788 -14.8; 5267 -15.2; 5793 -11.1; 6373 -4.3; 7010 -3.1; 7711 -4.8; 8482 -5.1; 9330 -4.9; 10263 -4.9; 11289 -4.9; 12418 -4.9; 13660 -4.9; 15026 -4.9; 16529 -4.9; 18182 -4.9; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ferrari Cavallino T350 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ferrari Cavallino T350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 2.18 | 2.9 dB   |
| Peaking | 781 Hz  | 2.55 | 3.4 dB   |
| Peaking | 1435 Hz | 2.1  | -5.4 dB  |
| Peaking | 3281 Hz | 0.62 | 7.3 dB   |
| Peaking | 4954 Hz | 2.89 | -17.2 dB |
| Peaking | 128 Hz  | 0.88 | -1.0 dB  |
| Peaking | 253 Hz  | 1.46 | -1.1 dB  |
| Peaking | 5658 Hz | 8.03 | -3.9 dB  |
| Peaking | 6637 Hz | 3.32 | 4.5 dB   |
| Peaking | 7964 Hz | 1.59 | -1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.7 dB |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ferrari%20Cavallino%20T350/Ferrari%20Cavallino%20T350.png)