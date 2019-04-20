# BGVP DMG
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -8.0; 25 -8.3; 28 -8.7; 31 -9.0; 34 -9.2; 37 -9.5; 41 -9.7; 45 -9.9; 49 -10.1; 54 -10.4; 60 -10.6; 66 -10.9; 72 -11.1; 79 -11.3; 87 -11.5; 96 -11.7; 106 -12.0; 116 -12.1; 128 -12.2; 141 -12.2; 155 -12.0; 170 -11.8; 187 -11.6; 206 -11.2; 227 -10.9; 249 -10.5; 274 -10.0; 302 -9.4; 332 -8.7; 365 -8.1; 402 -7.5; 442 -6.9; 486 -6.2; 535 -5.6; 588 -4.9; 647 -4.3; 712 -3.7; 783 -3.2; 861 -2.6; 947 -2.4; 1042 -2.2; 1146 -2.1; 1261 -1.8; 1387 -1.7; 1526 -2.2; 1678 -2.6; 1846 -2.6; 2031 -2.0; 2234 -1.3; 2457 -1.1; 2703 -1.5; 2973 -2.7; 3270 -0.9; 3597 -0.5; 3957 -3.3; 4353 -5.1; 4788 -6.1; 5267 -7.1; 5793 -9.0; 6373 -7.1; 7010 -4.8; 7711 -6.0; 8482 -9.0; 9330 -11.2; 10263 -11.3; 11289 -9.4; 12418 -8.1; 13660 -13.4; 15026 -20.6; 16529 -21.0; 18182 -18.1; 20000 -17.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BGVP DMG GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BGVP DMG ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 132 Hz   | 0.31 | -6.2 dB  |
| Peaking | 864 Hz   | 0.62 | 4.1 dB   |
| Peaking | 4037 Hz  | 0.57 | 5.9 dB   |
| Peaking | 5304 Hz  | 2.09 | -5.9 dB  |
| Peaking | 17212 Hz | 0.57 | -15.2 dB |
| Peaking | 6064 Hz  | 7.93 | -2.7 dB  |
| Peaking | 7172 Hz  | 2.55 | 3.2 dB   |
| Peaking | 9487 Hz  | 2.06 | -4.5 dB  |
| Peaking | 12419 Hz | 2.5  | 6.0 dB   |
| Peaking | 15051 Hz | 3.45 | -4.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -3.5 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -18.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/BGVP%20DMG/BGVP%20DMG.png)