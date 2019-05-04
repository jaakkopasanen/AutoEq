# Hifiman Shangri-La
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.9; 23 -1.1; 25 -1.3; 28 -1.5; 31 -1.7; 34 -1.7; 37 -1.7; 41 -1.7; 45 -1.7; 49 -1.7; 54 -1.7; 60 -2.0; 66 -2.6; 72 -3.2; 79 -3.6; 87 -4.0; 96 -4.2; 106 -4.4; 116 -4.9; 128 -5.2; 141 -5.4; 155 -5.6; 170 -5.8; 187 -6.0; 206 -6.1; 227 -6.2; 249 -6.2; 274 -6.2; 302 -6.2; 332 -6.2; 365 -6.1; 402 -6.0; 442 -5.9; 486 -6.1; 535 -6.2; 588 -5.9; 647 -5.7; 712 -5.8; 783 -5.7; 861 -5.6; 947 -4.9; 1042 -3.8; 1146 -2.9; 1261 -2.6; 1387 -1.8; 1526 -1.1; 1678 -0.6; 1846 -0.5; 2031 -0.8; 2234 -1.4; 2457 -2.0; 2703 -1.9; 2973 -4.0; 3270 -8.2; 3597 -9.4; 3957 -9.2; 4353 -9.6; 4788 -10.3; 5267 -9.3; 5793 -5.9; 6373 -8.1; 7010 -10.5; 7711 -10.4; 8482 -6.5; 9330 -6.2; 10263 -11.2; 11289 -14.1; 12418 -12.5; 13660 -10.2; 15026 -10.1; 16529 -11.7; 18182 -13.8; 20000 -20.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hifiman Shangri-La GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hifiman Shangri-La ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 0.64 | 4.6 dB   |
| Peaking | 2136 Hz  | 1.08 | 7.2 dB   |
| Peaking | 4019 Hz  | 1.12 | -6.3 dB  |
| Peaking | 11543 Hz | 3.07 | -7.1 dB  |
| Peaking | 20048 Hz | 0.47 | -13.8 dB |
| Peaking | 531 Hz   | 0.39 | -1.1 dB  |
| Peaking | 1328 Hz  | 2.14 | 1.5 dB   |
| Peaking | 5908 Hz  | 7.19 | 4.0 dB   |
| Peaking | 7434 Hz  | 2.76 | -4.1 dB  |
| Peaking | 8843 Hz  | 5.09 | 4.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.4 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.7 dB |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | -9.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Hifiman%20Shangri-La/Hifiman%20Shangri-La.png)