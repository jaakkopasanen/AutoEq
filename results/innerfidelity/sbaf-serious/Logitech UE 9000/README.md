# Logitech UE 9000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.7; 23 -9.0; 25 -9.3; 28 -9.6; 31 -9.8; 34 -10.0; 37 -10.1; 41 -10.2; 45 -10.3; 49 -10.3; 54 -10.4; 60 -10.4; 66 -10.5; 72 -10.5; 79 -10.6; 87 -10.5; 96 -10.6; 106 -10.6; 116 -11.1; 128 -12.1; 141 -11.9; 155 -11.1; 170 -10.2; 187 -10.2; 206 -10.7; 227 -10.1; 249 -9.5; 274 -8.9; 302 -8.6; 332 -8.2; 365 -7.8; 402 -7.5; 442 -7.2; 486 -7.3; 535 -7.2; 588 -6.9; 647 -7.1; 712 -7.6; 783 -7.6; 861 -7.8; 947 -8.3; 1042 -8.6; 1146 -8.9; 1261 -8.5; 1387 -8.4; 1526 -8.5; 1678 -8.3; 1846 -7.4; 2031 -6.6; 2234 -5.3; 2457 -3.6; 2703 -1.8; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -3.7; 4353 -4.3; 4788 -5.0; 5267 -2.9; 5793 -0.7; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.2; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech UE 9000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech UE 9000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.53 | -2.9 dB |
| Peaking | 140 Hz  | 1.38 | -3.0 dB |
| Peaking | 722 Hz  | 0.06 | -1.5 dB |
| Peaking | 3160 Hz | 2.18 | 7.9 dB  |
| Peaking | 6076 Hz | 3.35 | 6.9 dB  |
| Peaking | 174 Hz  | 4.37 | 2.1 dB  |
| Peaking | 199 Hz  | 1.98 | -1.9 dB |
| Peaking | 581 Hz  | 0.8  | 1.6 dB  |
| Peaking | 1246 Hz | 0.93 | -1.7 dB |
| Peaking | 2488 Hz | 4.88 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Logitech%20UE%209000/Logitech%20UE%209000.png)