# Koss BT540i Wired Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.7; 25 -6.6; 28 -7.7; 31 -8.6; 34 -9.4; 37 -10.1; 41 -10.8; 45 -11.3; 49 -11.8; 54 -12.2; 60 -12.7; 66 -13.1; 72 -13.4; 79 -13.6; 87 -13.7; 96 -14.0; 106 -14.1; 116 -13.8; 128 -13.9; 141 -14.5; 155 -15.1; 170 -14.1; 187 -14.3; 206 -14.5; 227 -14.0; 249 -13.5; 274 -12.6; 302 -11.4; 332 -11.0; 365 -9.6; 402 -7.8; 442 -6.4; 486 -6.0; 535 -5.5; 588 -5.0; 647 -5.2; 712 -5.8; 783 -6.0; 861 -6.4; 947 -6.5; 1042 -6.5; 1146 -6.7; 1261 -6.9; 1387 -7.6; 1526 -8.2; 1678 -8.9; 1846 -9.4; 2031 -9.7; 2234 -10.5; 2457 -11.1; 2703 -12.2; 2973 -12.9; 3270 -12.3; 3597 -10.4; 3957 -7.7; 4353 -5.6; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.2; 7010 -4.5; 7711 -6.4; 8482 -9.8; 9330 -11.4; 10263 -7.9; 11289 -6.5; 12418 -6.7; 13660 -7.8; 15026 -7.8; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss BT540i Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss BT540i Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 85 Hz   | 0.65 | -7.1 dB |
| Peaking | 210 Hz  | 1.45 | -5.8 dB |
| Peaking | 2998 Hz | 1.4  | -7.2 dB |
| Peaking | 5257 Hz | 2.6  | 9.1 dB  |
| Peaking | 20 Hz   | 3.03 | 3.0 dB  |
| Peaking | 327 Hz  | 2.8  | -2.1 dB |
| Peaking | 543 Hz  | 1.45 | 2.7 dB  |
| Peaking | 6433 Hz | 6.59 | 2.9 dB  |
| Peaking | 9107 Hz | 4.28 | -5.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | -5.7 dB |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | -6.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.4 dB |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20BT540i%20Wired%20Passive/Koss%20BT540i%20Wired%20Passive.png)