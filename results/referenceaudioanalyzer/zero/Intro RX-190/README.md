# Intro RX-190
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.6; 23 -12.6; 25 -12.5; 28 -12.6; 31 -12.6; 34 -12.7; 37 -12.8; 41 -12.9; 45 -12.9; 49 -12.9; 54 -12.9; 60 -12.9; 66 -12.9; 72 -12.9; 79 -12.9; 87 -12.9; 96 -12.9; 106 -12.9; 116 -12.9; 128 -13.1; 141 -13.2; 155 -13.2; 170 -13.2; 187 -13.3; 206 -13.5; 227 -13.8; 249 -14.3; 274 -14.8; 302 -15.2; 332 -15.6; 365 -16.1; 402 -16.8; 442 -17.6; 486 -18.4; 535 -19.2; 588 -19.5; 647 -19.2; 712 -17.8; 783 -15.5; 861 -12.8; 947 -10.5; 1042 -8.6; 1146 -6.7; 1261 -4.9; 1387 -3.6; 1526 -2.7; 1678 -1.9; 1846 -1.0; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.3; 6373 -7.6; 7010 -7.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Intro RX-190 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Intro RX-190 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.16 | -6.2 dB  |
| Peaking | 424 Hz   | 0.6  | -5.0 dB  |
| Peaking | 649 Hz   | 0.96 | -13.6 dB |
| Peaking | 2012 Hz  | 0.27 | 8.7 dB   |
| Peaking | 7617 Hz  | 1.41 | -4.6 dB  |
| Peaking | 2951 Hz  | 2.97 | -0.8 dB  |
| Peaking | 5548 Hz  | 3.46 | 4.0 dB   |
| Peaking | 6395 Hz  | 4.16 | -5.5 dB  |
| Peaking | 7514 Hz  | 3.08 | 2.3 dB   |
| Peaking | 12238 Hz | 0.92 | -0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB  |
| Peaking | 62 Hz    | 1.41 | -4.6 dB  |
| Peaking | 125 Hz   | 1.41 | -4.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | -13.5 dB |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 16000 Hz | 1.41 | 0.0 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Intro%20RX-190/Intro%20RX-190.png)