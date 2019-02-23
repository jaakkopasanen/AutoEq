# Piaton PS 210
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.8; 54 -1.4; 60 -2.1; 66 -2.7; 72 -3.2; 79 -3.8; 87 -4.4; 96 -4.9; 106 -5.4; 116 -5.7; 128 -6.2; 141 -6.7; 155 -7.0; 170 -7.3; 187 -7.5; 206 -7.8; 227 -7.9; 249 -8.1; 274 -8.1; 302 -8.0; 332 -8.1; 365 -8.1; 402 -8.2; 442 -8.4; 486 -8.1; 535 -7.9; 588 -7.9; 647 -8.0; 712 -8.0; 783 -7.6; 861 -7.2; 947 -6.7; 1042 -6.1; 1146 -5.4; 1261 -4.9; 1387 -4.7; 1526 -5.1; 1678 -5.6; 1846 -6.7; 2031 -8.2; 2234 -9.9; 2457 -10.3; 2703 -7.2; 2973 -3.4; 3270 -0.6; 3597 -0.5; 3957 -1.6; 4353 -5.2; 4788 -4.7; 5267 -0.8; 5793 -1.6; 6373 -5.6; 7010 -7.4; 7711 -12.2; 8482 -12.7; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Piaton PS 210 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Piaton PS 210 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.79 | 6.9 dB  |
| Peaking | 2407 Hz | 4.33 | -5.8 dB |
| Peaking | 3413 Hz | 2.86 | 7.1 dB  |
| Peaking | 5536 Hz | 5.47 | 6.2 dB  |
| Peaking | 8081 Hz | 5.08 | -8.0 dB |
| Peaking | 26 Hz   | 0.3  | 3.3 dB  |
| Peaking | 33 Hz   | 1.35 | -4.0 dB |
| Peaking | 338 Hz  | 0.25 | -2.1 dB |
| Peaking | 1351 Hz | 1.57 | 3.0 dB  |
| Peaking | 2036 Hz | 5.75 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Piaton%20PS%20210/Piaton%20PS%20210.png)