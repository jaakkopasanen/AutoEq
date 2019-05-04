# Turtle Beach Stealth 600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -5.2; 25 -5.6; 28 -6.1; 31 -6.5; 34 -6.8; 37 -7.0; 41 -7.1; 45 -7.2; 49 -7.3; 54 -7.3; 60 -7.4; 66 -7.4; 72 -7.4; 79 -7.4; 87 -7.4; 96 -7.4; 106 -7.3; 116 -7.4; 128 -7.3; 141 -7.2; 155 -7.1; 170 -6.8; 187 -6.5; 206 -6.2; 227 -5.9; 249 -5.5; 274 -5.2; 302 -5.0; 332 -4.8; 365 -4.4; 402 -3.8; 442 -3.6; 486 -3.8; 535 -4.0; 588 -4.1; 647 -4.2; 712 -4.2; 783 -4.5; 861 -5.0; 947 -5.8; 1042 -6.2; 1146 -6.4; 1261 -6.2; 1387 -5.8; 1526 -5.1; 1678 -4.1; 1846 -3.5; 2031 -3.3; 2234 -2.8; 2457 -2.6; 2703 -2.2; 2973 -0.5; 3270 -0.7; 3597 -2.2; 3957 -5.5; 4353 -5.7; 4788 -4.9; 5267 -3.0; 5793 -1.8; 6373 -4.4; 7010 -5.1; 7711 -4.6; 8482 -4.6; 9330 -4.6; 10263 -4.6; 11289 -4.9; 12418 -5.8; 13660 -4.6; 15026 -4.6; 16529 -4.6; 18182 -4.6; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Stealth 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Stealth 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 76 Hz    | 0.51 | -3.1 dB |
| Peaking | 1182 Hz  | 3.16 | -2.3 dB |
| Peaking | 3324 Hz  | 1.74 | 7.4 dB  |
| Peaking | 4013 Hz  | 1.93 | -5.8 dB |
| Peaking | 5621 Hz  | 5.95 | 3.4 dB  |
| Peaking | 168 Hz   | 2.29 | -0.7 dB |
| Peaking | 452 Hz   | 1.95 | 1.4 dB  |
| Peaking | 4983 Hz  | 8.06 | 0.4 dB  |
| Peaking | 12245 Hz | 5.8  | -1.5 dB |
| Peaking | 13457 Hz | 3.35 | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Stealth%20600/Turtle%20Beach%20Stealth%20600.png)