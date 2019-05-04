# Panasonic RP-HC200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.6; 60 -1.1; 66 -1.2; 72 -1.8; 79 -2.7; 87 -3.6; 96 -4.4; 106 -5.1; 116 -5.6; 128 -6.2; 141 -6.4; 155 -6.4; 170 -6.4; 187 -6.5; 206 -6.4; 227 -6.4; 249 -6.5; 274 -6.3; 302 -5.8; 332 -5.4; 365 -5.2; 402 -5.1; 442 -5.3; 486 -6.1; 535 -7.0; 588 -8.1; 647 -9.4; 712 -10.6; 783 -11.4; 861 -11.7; 947 -11.3; 1042 -11.0; 1146 -10.6; 1261 -9.6; 1387 -9.5; 1526 -8.9; 1678 -7.6; 1846 -6.4; 2031 -5.3; 2234 -4.5; 2457 -4.9; 2703 -4.8; 2973 -4.4; 3270 -4.4; 3597 -3.2; 3957 -1.0; 4353 -0.5; 4788 -0.5; 5267 -1.0; 5793 -4.4; 6373 -5.2; 7010 -5.1; 7711 -10.1; 8482 -13.5; 9330 -8.5; 10263 -6.5; 11289 -6.5; 12418 -7.1; 13660 -11.4; 15026 -15.5; 16529 -13.4; 18182 -7.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 0.59 | 6.8 dB   |
| Peaking | 944 Hz   | 1.55 | -5.7 dB  |
| Peaking | 4519 Hz  | 1.4  | 6.4 dB   |
| Peaking | 8273 Hz  | 5.51 | -8.5 dB  |
| Peaking | 15464 Hz | 2.16 | -10.3 dB |
| Peaking | 145 Hz   | 2.15 | -1.2 dB  |
| Peaking | 403 Hz   | 2.78 | 2.2 dB   |
| Peaking | 1992 Hz  | 1.19 | -2.3 dB  |
| Peaking | 2139 Hz  | 2.53 | 3.7 dB   |
| Peaking | 11500 Hz | 4.06 | 1.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 4.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -6.2 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | -8.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Panasonic%20RP-HC200/Panasonic%20RP-HC200.png)