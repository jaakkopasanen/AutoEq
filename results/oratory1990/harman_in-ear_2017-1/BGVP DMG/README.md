# BGVP DMG
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.1; 25 -7.4; 28 -7.9; 31 -8.2; 34 -8.5; 37 -8.8; 41 -9.1; 45 -9.3; 49 -9.6; 54 -9.8; 60 -10.1; 66 -10.4; 72 -10.7; 79 -11.0; 87 -11.3; 96 -11.5; 106 -11.8; 116 -11.9; 128 -12.0; 141 -12.0; 155 -11.9; 170 -11.7; 187 -11.5; 206 -11.1; 227 -10.7; 249 -10.3; 274 -9.9; 302 -9.3; 332 -8.6; 365 -8.0; 402 -7.4; 442 -6.9; 486 -6.3; 535 -5.7; 588 -5.1; 647 -4.5; 712 -4.0; 783 -3.5; 861 -3.1; 947 -3.0; 1042 -2.6; 1146 -2.4; 1261 -2.2; 1387 -2.0; 1526 -2.7; 1678 -3.7; 1846 -3.9; 2031 -3.5; 2234 -2.9; 2457 -2.4; 2703 -2.5; 2973 -2.6; 3270 -0.5; 3597 -2.3; 3957 -4.5; 4353 -5.3; 4788 -5.7; 5267 -6.8; 5793 -10.1; 6373 -9.2; 7010 -6.2; 7711 -6.2; 8482 -8.0; 9330 -10.9; 10263 -12.9; 11289 -11.6; 12418 -11.0; 13660 -17.8; 15026 -25.8; 16529 -25.8; 18182 -20.4; 20000 -17.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BGVP DMG GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BGVP DMG ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 136 Hz   | 0.39 | -5.7 dB  |
| Peaking | 1078 Hz  | 0.56 | 4.6 dB   |
| Peaking | 3272 Hz  | 3.32 | 4.8 dB   |
| Peaking | 15702 Hz | 1.53 | -15.7 dB |
| Peaking | 18908 Hz | 0.46 | -9.9 dB  |
| Peaking | 2450 Hz  | 8.1  | 1.3 dB   |
| Peaking | 6010 Hz  | 5.63 | -5.0 dB  |
| Peaking | 7578 Hz  | 2.17 | 3.5 dB   |
| Peaking | 10027 Hz | 2.32 | -3.7 dB  |
| Peaking | 12272 Hz | 4.48 | 4.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -5.0 dB  |
| Peaking | 250 Hz   | 1.41 | -3.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 16000 Hz | 1.41 | -25.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/BGVP%20DMG/BGVP%20DMG.png)