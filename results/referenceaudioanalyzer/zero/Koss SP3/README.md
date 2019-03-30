# Koss SP3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -1.9; 227 -5.5; 249 -7.1; 274 -10.0; 302 -13.5; 332 -16.5; 365 -18.6; 402 -18.5; 442 -17.6; 486 -17.2; 535 -16.4; 588 -15.6; 647 -15.0; 712 -14.5; 783 -15.2; 861 -16.5; 947 -17.7; 1042 -17.3; 1146 -14.6; 1261 -14.3; 1387 -16.2; 1526 -15.2; 1678 -11.9; 1846 -12.4; 2031 -12.7; 2234 -9.9; 2457 -7.1; 2703 -7.6; 2973 -12.4; 3270 -15.4; 3597 -14.1; 3957 -6.1; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss SP3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss SP3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 398 Hz  | 2.84 | -11.7 dB |
| Peaking | 839 Hz  | 1.22 | -8.5 dB  |
| Peaking | 1473 Hz | 1.51 | -5.8 dB  |
| Peaking | 3427 Hz | 3.97 | -13.4 dB |
| Peaking | 4698 Hz | 1.56 | 9.4 dB   |
| Peaking | 47 Hz   | 0.18 | 6.2 dB   |
| Peaking | 178 Hz  | 2.1  | 3.2 dB   |
| Peaking | 308 Hz  | 3    | -6.0 dB  |
| Peaking | 534 Hz  | 3.86 | -3.7 dB  |
| Peaking | 750 Hz  | 8.85 | 1.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB   |
| Peaking | 62 Hz    | 1.41 | 3.7 dB   |
| Peaking | 125 Hz   | 1.41 | 7.6 dB   |
| Peaking | 250 Hz   | 1.41 | -0.7 dB  |
| Peaking | 500 Hz   | 1.41 | -11.3 dB |
| Peaking | 1000 Hz  | 1.41 | -7.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 16000 Hz | 1.41 | -0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Koss%20SP3/Koss%20SP3.png)