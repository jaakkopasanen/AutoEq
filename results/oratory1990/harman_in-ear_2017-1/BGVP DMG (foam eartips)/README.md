# BGVP DMG (foam eartips)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -6.9; 25 -7.3; 28 -7.7; 31 -8.1; 34 -8.4; 37 -8.7; 41 -8.9; 45 -9.2; 49 -9.4; 54 -9.7; 60 -10.0; 66 -10.3; 72 -10.6; 79 -10.9; 87 -11.1; 96 -11.4; 106 -11.6; 116 -11.8; 128 -11.8; 141 -11.8; 155 -11.7; 170 -11.6; 187 -11.3; 206 -11.0; 227 -10.6; 249 -10.2; 274 -9.7; 302 -9.2; 332 -8.5; 365 -7.9; 402 -7.3; 442 -6.7; 486 -6.1; 535 -5.5; 588 -4.9; 647 -4.4; 712 -3.8; 783 -3.3; 861 -3.0; 947 -2.8; 1042 -2.5; 1146 -2.2; 1261 -2.0; 1387 -1.9; 1526 -2.6; 1678 -3.5; 1846 -3.8; 2031 -3.4; 2234 -2.8; 2457 -2.3; 2703 -2.4; 2973 -2.4; 3270 -0.5; 3597 -2.0; 3957 -4.3; 4353 -5.2; 4788 -5.5; 5267 -6.7; 5793 -9.9; 6373 -9.1; 7010 -6.1; 7711 -6.0; 8482 -7.8; 9330 -10.8; 10263 -12.8; 11289 -11.4; 12418 -10.9; 13660 -17.7; 15026 -25.7; 16529 -25.6; 18182 -20.3; 20000 -16.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BGVP DMG (foam eartips) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BGVP DMG (foam eartips) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 136 Hz   | 0.39 | -5.7 dB  |
| Peaking | 1076 Hz  | 0.57 | 4.6 dB   |
| Peaking | 3269 Hz  | 3.2  | 4.7 dB   |
| Peaking | 15711 Hz | 1.6  | -15.2 dB |
| Peaking | 18915 Hz | 0.45 | -10.3 dB |
| Peaking | 2436 Hz  | 8.42 | 1.3 dB   |
| Peaking | 6063 Hz  | 4.96 | -5.4 dB  |
| Peaking | 7657 Hz  | 1.53 | 6.1 dB   |
| Peaking | 10295 Hz | 1.04 | -6.6 dB  |
| Peaking | 12195 Hz | 3.04 | 7.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -5.0 dB  |
| Peaking | 250 Hz   | 1.41 | -3.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 16000 Hz | 1.41 | -25.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/BGVP%20DMG%20(foam%20eartips)/BGVP%20DMG%20(foam%20eartips).png)