# Fostex T60RP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.4; 31 -2.4; 34 -3.3; 37 -4.0; 41 -4.9; 45 -5.7; 49 -6.2; 54 -6.7; 60 -7.2; 66 -7.4; 72 -7.5; 79 -7.5; 87 -7.5; 96 -7.4; 106 -7.3; 116 -7.2; 128 -7.1; 141 -6.8; 155 -6.6; 170 -6.7; 187 -7.5; 206 -7.5; 227 -7.1; 249 -6.7; 274 -6.4; 302 -5.9; 332 -4.9; 365 -4.7; 402 -5.1; 442 -5.6; 486 -6.0; 535 -6.4; 588 -6.7; 647 -7.0; 712 -7.5; 783 -7.8; 861 -7.4; 947 -7.8; 1042 -9.6; 1146 -10.9; 1261 -11.7; 1387 -10.7; 1526 -9.2; 1678 -8.0; 1846 -6.5; 2031 -4.5; 2234 -2.6; 2457 -0.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -3.8; 4788 -8.0; 5267 -8.5; 5793 -8.3; 6373 -9.6; 7010 -12.8; 7711 -13.8; 8482 -11.0; 9330 -7.7; 10263 -8.3; 11289 -9.7; 12418 -7.5; 13660 -6.5; 15026 -6.5; 16529 -7.9; 18182 -10.0; 20000 -11.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T60RP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T60RP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.93 | 6.6 dB  |
| Peaking | 1305 Hz  | 1.98 | -6.3 dB |
| Peaking | 3049 Hz  | 1.22 | 7.8 dB  |
| Peaking | 7266 Hz  | 1.76 | -7.6 dB |
| Peaking | 19455 Hz | 0.97 | -4.8 dB |
| Peaking | 36 Hz    | 2.09 | 1.6 dB  |
| Peaking | 68 Hz    | 0.49 | -1.3 dB |
| Peaking | 368 Hz   | 3.09 | 2.2 dB  |
| Peaking | 4034 Hz  | 8.26 | 2.8 dB  |
| Peaking | 4861 Hz  | 7.43 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.9 dB |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Fostex%20T60RP/Fostex%20T60RP.png)