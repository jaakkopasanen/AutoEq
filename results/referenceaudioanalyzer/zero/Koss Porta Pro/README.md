# Koss Porta Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.7; 37 -1.4; 41 -2.7; 45 -3.9; 49 -5.0; 54 -6.2; 60 -7.3; 66 -8.2; 72 -8.9; 79 -9.6; 87 -10.2; 96 -10.4; 106 -10.4; 116 -10.4; 128 -10.4; 141 -10.3; 155 -10.1; 170 -9.9; 187 -9.6; 206 -9.4; 227 -9.0; 249 -8.6; 274 -8.1; 302 -7.7; 332 -7.4; 365 -7.1; 402 -6.7; 442 -6.3; 486 -5.9; 535 -5.7; 588 -5.4; 647 -5.2; 712 -5.1; 783 -4.9; 861 -4.9; 947 -4.9; 1042 -4.9; 1146 -5.0; 1261 -5.3; 1387 -5.7; 1526 -6.1; 1678 -6.7; 1846 -7.5; 2031 -8.4; 2234 -9.6; 2457 -10.6; 2703 -10.7; 2973 -9.6; 3270 -7.7; 3597 -5.5; 3957 -2.7; 4353 -1.2; 4788 -6.8; 5267 -10.7; 5793 -10.2; 6373 -5.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Porta Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 28 Hz   | 0.84 | 7.3 dB   |
| Peaking | 103 Hz  | 0.71 | -5.1 dB  |
| Peaking | 2798 Hz | 2.04 | -7.9 dB  |
| Peaking | 4443 Hz | 1.26 | 10.1 dB  |
| Peaking | 5307 Hz | 3.31 | -12.1 dB |
| Peaking | 11 Hz   | 1.59 | 0.9 dB   |
| Peaking | 883 Hz  | 1.01 | 1.9 dB   |
| Peaking | 2114 Hz | 3.89 | -1.3 dB  |
| Peaking | 6752 Hz | 8.98 | 3.8 dB   |
| Peaking | 7954 Hz | 1.2  | -1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Koss%20Porta%20Pro/Koss%20Porta%20Pro.png)