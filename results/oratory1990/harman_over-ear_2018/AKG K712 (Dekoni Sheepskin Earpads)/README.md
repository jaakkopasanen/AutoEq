# AKG K712 (Dekoni Sheepskin Earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -5.1; 25 -5.5; 28 -5.9; 31 -6.2; 34 -6.5; 37 -6.7; 41 -6.9; 45 -7.1; 49 -7.3; 54 -7.5; 60 -7.7; 66 -7.9; 72 -8.1; 79 -8.3; 87 -8.6; 96 -8.9; 106 -9.2; 116 -9.6; 128 -10.1; 141 -10.6; 155 -10.9; 170 -11.2; 187 -11.3; 206 -11.5; 227 -11.5; 249 -11.5; 274 -11.3; 302 -10.9; 332 -10.4; 365 -9.8; 402 -9.3; 442 -8.8; 486 -8.3; 535 -7.5; 588 -6.7; 647 -5.9; 712 -6.0; 783 -6.4; 861 -6.6; 947 -6.6; 1042 -6.3; 1146 -5.6; 1261 -4.9; 1387 -5.1; 1526 -6.2; 1678 -7.7; 1846 -8.9; 2031 -10.4; 2234 -11.4; 2457 -11.1; 2703 -8.9; 2973 -4.7; 3270 -0.7; 3597 -0.5; 3957 -0.5; 4353 -1.1; 4788 -4.2; 5267 -8.6; 5793 -9.8; 6373 -7.0; 7010 -8.3; 7711 -8.8; 8482 -6.7; 9330 -6.5; 10263 -6.5; 11289 -7.5; 12418 -9.1; 13660 -7.4; 15026 -7.8; 16529 -11.5; 18182 -14.8; 20000 -15.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K712 (Dekoni Sheepskin Earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 (Dekoni Sheepskin Earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 215 Hz   | 0.63 | -5.3 dB  |
| Peaking | 2352 Hz  | 1.55 | -13.4 dB |
| Peaking | 3917 Hz  | 0.71 | 20.6 dB  |
| Peaking | 5440 Hz  | 0.93 | -14.9 dB |
| Peaking | 19136 Hz | 0.65 | -9.5 dB  |
| Peaking | 22 Hz    | 1.94 | 1.9 dB   |
| Peaking | 662 Hz   | 2.7  | 2.1 dB   |
| Peaking | 850 Hz   | 0.99 | -1.4 dB  |
| Peaking | 1308 Hz  | 4.46 | 1.7 dB   |
| Peaking | 14590 Hz | 6.62 | 1.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB |
| Peaking | 16000 Hz | 1.41 | -5.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K712%20(Dekoni%20Sheepskin%20Earpads)/AKG%20K712%20(Dekoni%20Sheepskin%20Earpads).png)