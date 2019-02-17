# Panasonic RP-HC800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.0; 23 -13.8; 25 -13.7; 28 -13.6; 31 -13.5; 34 -13.3; 37 -13.2; 41 -13.0; 45 -12.9; 49 -12.7; 54 -12.6; 60 -12.5; 66 -12.6; 72 -12.6; 79 -12.7; 87 -12.9; 96 -13.0; 106 -13.2; 116 -13.4; 128 -13.6; 141 -13.7; 155 -13.8; 170 -13.8; 187 -13.7; 206 -13.5; 227 -13.2; 249 -12.9; 274 -12.7; 302 -12.5; 332 -12.2; 365 -11.7; 402 -11.3; 442 -10.8; 486 -10.1; 535 -8.9; 588 -7.5; 647 -5.2; 712 -2.5; 783 -0.8; 861 -0.7; 947 -0.5; 1042 -1.5; 1146 -2.8; 1261 -3.7; 1387 -3.1; 1526 -2.7; 1678 -2.8; 1846 -4.5; 2031 -5.4; 2234 -6.9; 2457 -7.0; 2703 -4.1; 2973 -2.0; 3270 -3.5; 3597 -4.5; 3957 -5.7; 4353 -8.3; 4788 -9.0; 5267 -8.6; 5793 -11.4; 6373 -15.1; 7010 -10.6; 7711 -7.9; 8482 -10.2; 9330 -11.8; 10263 -11.6; 11289 -13.0; 12418 -13.3; 13660 -11.7; 15026 -12.3; 16529 -12.8; 18182 -11.7; 20000 -15.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--2.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.13 | -12.5 dB |
| Peaking | 204 Hz   | 0.77 | -7.6 dB  |
| Peaking | 421 Hz   | 1.83 | -6.0 dB  |
| Peaking | 9452 Hz  | 0.34 | -10.0 dB |
| Peaking | 20388 Hz | 0.29 | -11.8 dB |
| Peaking | 851 Hz   | 3.86 | 3.4 dB   |
| Peaking | 2421 Hz  | 2.8  | -5.5 dB  |
| Peaking | 2923 Hz  | 2.82 | 5.6 dB   |
| Peaking | 6357 Hz  | 5.58 | -6.3 dB  |
| Peaking | 7620 Hz  | 4.51 | 4.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -13.5 dB |
| Peaking | 62 Hz    | 1.41 | -7.4 dB  |
| Peaking | 125 Hz   | 1.41 | -9.8 dB  |
| Peaking | 250 Hz   | 1.41 | -10.2 dB |
| Peaking | 500 Hz   | 1.41 | -7.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -10.9 dB |
| Peaking | 16000 Hz | 1.41 | -18.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Panasonic%20RP-HC800/Panasonic%20RP-HC800.png)