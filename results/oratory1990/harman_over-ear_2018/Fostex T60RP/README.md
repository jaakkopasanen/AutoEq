# Fostex T60RP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.0; 37 -1.7; 41 -2.6; 45 -3.4; 49 -3.9; 54 -4.4; 60 -4.9; 66 -5.1; 72 -5.2; 79 -5.2; 87 -5.2; 96 -5.1; 106 -5.0; 116 -4.9; 128 -4.7; 141 -4.5; 155 -4.2; 170 -4.4; 187 -5.2; 206 -5.2; 227 -4.8; 249 -4.4; 274 -4.1; 302 -3.6; 332 -2.6; 365 -2.4; 402 -2.8; 442 -3.3; 486 -3.7; 535 -4.0; 588 -4.4; 647 -4.7; 712 -5.2; 783 -5.5; 861 -5.1; 947 -5.5; 1042 -7.3; 1146 -8.6; 1261 -9.4; 1387 -8.4; 1526 -6.9; 1678 -5.7; 1846 -4.2; 2031 -2.2; 2234 -0.6; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.6; 4788 -5.6; 5267 -6.2; 5793 -6.0; 6373 -7.3; 7010 -10.5; 7711 -11.5; 8482 -8.7; 9330 -6.5; 10263 -6.5; 11289 -7.4; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.7; 20000 -8.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T60RP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T60RP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.77 | 6.3 dB  |
| Peaking | 372 Hz  | 0.72 | 3.3 dB  |
| Peaking | 1301 Hz | 2.25 | -5.3 dB |
| Peaking | 2879 Hz | 0.93 | 7.0 dB  |
| Peaking | 7394 Hz | 3    | -6.3 dB |
| Peaking | 163 Hz  | 2.03 | 1.5 dB  |
| Peaking | 199 Hz  | 2.59 | -1.6 dB |
| Peaking | 3139 Hz | 3.39 | -1.5 dB |
| Peaking | 4319 Hz | 2.09 | 3.2 dB  |
| Peaking | 4910 Hz | 4.79 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | 1.2 dB  |
| Peaking | 250 Hz   | 1.41 | 1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 3.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.9 dB |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Fostex%20T60RP/Fostex%20T60RP.png)