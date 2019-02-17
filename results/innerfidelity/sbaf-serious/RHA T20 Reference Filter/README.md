# RHA T20 Reference Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.6; 23 -10.9; 25 -11.1; 28 -11.3; 31 -11.5; 34 -11.6; 37 -11.6; 41 -11.7; 45 -11.7; 49 -11.7; 54 -11.8; 60 -11.8; 66 -11.8; 72 -11.8; 79 -11.8; 87 -11.9; 96 -11.9; 106 -11.7; 116 -11.5; 128 -11.3; 141 -11.1; 155 -10.8; 170 -10.5; 187 -10.1; 206 -9.7; 227 -9.2; 249 -8.8; 274 -8.3; 302 -7.8; 332 -7.3; 365 -6.9; 402 -6.4; 442 -5.9; 486 -5.7; 535 -5.3; 588 -4.7; 647 -4.5; 712 -4.5; 783 -4.4; 861 -4.7; 947 -5.1; 1042 -5.8; 1146 -6.4; 1261 -7.2; 1387 -8.8; 1526 -9.8; 1678 -8.8; 1846 -5.7; 2031 -8.0; 2234 -9.0; 2457 -10.0; 2703 -10.3; 2973 -9.1; 3270 -7.7; 3597 -7.5; 3957 -9.5; 4353 -13.8; 4788 -14.3; 5267 -8.3; 5793 -3.1; 6373 -0.5; 7010 -3.0; 7711 -5.2; 8482 -5.5; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA T20 Reference Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T20 Reference Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 41 Hz   | 0.36 | -6.0 dB  |
| Peaking | 147 Hz  | 0.9  | -3.2 dB  |
| Peaking | 2411 Hz | 1.34 | -3.8 dB  |
| Peaking | 4641 Hz | 4.52 | -10.3 dB |
| Peaking | 6267 Hz | 3.95 | 6.6 dB   |
| Peaking | 745 Hz  | 1.67 | 2.0 dB   |
| Peaking | 1562 Hz | 3.12 | -3.9 dB  |
| Peaking | 1867 Hz | 5.02 | 4.1 dB   |
| Peaking | 3186 Hz | 1.84 | -1.7 dB  |
| Peaking | 3387 Hz | 4.21 | 2.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | -5.1 dB |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T20%20Reference%20Filter/RHA%20T20%20Reference%20Filter.png)