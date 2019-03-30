# Fostex T50RP mod
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -1.2; 31 -2.7; 34 -4.3; 37 -5.4; 41 -6.4; 45 -6.9; 49 -7.1; 54 -7.3; 60 -8.0; 66 -8.7; 72 -9.2; 79 -9.4; 87 -9.4; 96 -9.4; 106 -9.4; 116 -9.4; 128 -9.4; 141 -9.3; 155 -8.8; 170 -8.2; 187 -7.8; 206 -7.9; 227 -8.4; 249 -8.9; 274 -9.3; 302 -9.4; 332 -9.4; 365 -9.4; 402 -9.7; 442 -9.6; 486 -9.4; 535 -9.4; 588 -8.9; 647 -7.8; 712 -6.1; 783 -4.8; 861 -3.8; 947 -2.9; 1042 -2.1; 1146 -1.6; 1261 -0.7; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -2.3; 2703 -4.2; 2973 -6.4; 3270 -9.6; 3597 -13.1; 3957 -15.0; 4353 -14.7; 4788 -12.6; 5267 -9.7; 5793 -6.1; 6373 -3.8; 7010 -4.8; 7711 -6.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.6; 12418 -7.0; 13660 -6.5; 15026 -6.7; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T50RP mod GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T50RP mod ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 1.51 | 7.0 dB   |
| Peaking | 88 Hz   | 0.77 | -3.2 dB  |
| Peaking | 510 Hz  | 0.75 | -7.2 dB  |
| Peaking | 1730 Hz | 0.33 | 9.2 dB   |
| Peaking | 3983 Hz | 1.85 | -15.7 dB |
| Peaking | 194 Hz  | 7.3  | 0.8 dB   |
| Peaking | 2259 Hz | 8.31 | 1.1 dB   |
| Peaking | 4884 Hz | 6.55 | -1.7 dB  |
| Peaking | 6295 Hz | 4.08 | 3.9 dB   |
| Peaking | 8979 Hz | 0.64 | -1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | -4.2 dB |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -9.3 dB |
| Peaking | 8000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fostex%20T50RP%20mod/Fostex%20T50RP%20mod.png)