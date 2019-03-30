# Maxell Ear Bud
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.9; 116 -2.0; 128 -3.3; 141 -4.6; 155 -5.8; 170 -7.2; 187 -8.6; 206 -10.0; 227 -11.7; 249 -13.2; 274 -14.9; 302 -16.3; 332 -17.8; 365 -19.4; 402 -20.9; 442 -22.0; 486 -22.6; 535 -22.8; 588 -22.6; 647 -21.4; 712 -19.3; 783 -16.3; 861 -12.7; 947 -9.1; 1042 -5.5; 1146 -1.7; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -2.0; 2703 -4.0; 2973 -4.0; 3270 -2.2; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.9; 6373 -4.4; 7010 -5.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Maxell Ear Bud GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Maxell Ear Bud ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 111 Hz   | 0.27 | 17.3 dB  |
| Peaking | 547 Hz   | 0.25 | -29.0 dB |
| Peaking | 1168 Hz  | 1.27 | 15.8 dB  |
| Peaking | 1886 Hz  | 0.88 | 13.0 dB  |
| Peaking | 4579 Hz  | 1.1  | 10.6 dB  |
| Peaking | 21 Hz    | 2.21 | 1.6 dB   |
| Peaking | 2850 Hz  | 4.87 | -3.8 dB  |
| Peaking | 2921 Hz  | 2.31 | 2.3 dB   |
| Peaking | 7452 Hz  | 3.33 | -0.9 dB  |
| Peaking | 12007 Hz | 0.65 | 0.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB   |
| Peaking | 62 Hz    | 1.41 | 5.3 dB   |
| Peaking | 125 Hz   | 1.41 | 5.1 dB   |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | -20.7 dB |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Maxell%20Ear%20Bud/Maxell%20Ear%20Bud.png)