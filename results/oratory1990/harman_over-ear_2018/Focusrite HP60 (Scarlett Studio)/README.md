# Focusrite HP60 (Scarlett Studio)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.8; 45 -2.9; 49 -3.8; 54 -4.7; 60 -5.5; 66 -6.1; 72 -6.3; 79 -6.4; 87 -6.3; 96 -5.9; 106 -6.1; 116 -6.8; 128 -7.2; 141 -7.3; 155 -7.4; 170 -7.3; 187 -7.4; 206 -7.3; 227 -7.4; 249 -7.1; 274 -6.5; 302 -6.0; 332 -5.5; 365 -5.5; 402 -6.4; 442 -7.6; 486 -8.3; 535 -8.6; 588 -8.1; 647 -6.8; 712 -7.1; 783 -7.6; 861 -7.5; 947 -7.5; 1042 -7.9; 1146 -8.1; 1261 -7.8; 1387 -7.1; 1526 -6.4; 1678 -5.8; 1846 -5.1; 2031 -5.1; 2234 -5.2; 2457 -5.0; 2703 -4.6; 2973 -4.5; 3270 -3.2; 3597 -1.9; 3957 -1.2; 4353 -0.7; 4788 -6.6; 5267 -14.1; 5793 -13.7; 6373 -7.9; 7010 -6.3; 7711 -7.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.8; 15026 -10.1; 16529 -12.5; 18182 -12.1; 20000 -14.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focusrite HP60 (Scarlett Studio) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focusrite HP60 (Scarlett Studio) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 1.22 | 7.0 dB   |
| Peaking | 1976 Hz  | 5.25 | 0.9 dB   |
| Peaking | 4323 Hz  | 1.95 | 9.7 dB   |
| Peaking | 5328 Hz  | 3.77 | -14.1 dB |
| Peaking | 19089 Hz | 0.62 | -7.3 dB  |
| Peaking | 188 Hz   | 0.91 | -1.2 dB  |
| Peaking | 348 Hz   | 2.62 | 2.1 dB   |
| Peaking | 507 Hz   | 2.86 | -2.3 dB  |
| Peaking | 1114 Hz  | 2.75 | -1.8 dB  |
| Peaking | 12394 Hz | 2.66 | 1.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -5.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focusrite%20HP60%20(Scarlett%20Studio)/Focusrite%20HP60%20(Scarlett%20Studio).png)