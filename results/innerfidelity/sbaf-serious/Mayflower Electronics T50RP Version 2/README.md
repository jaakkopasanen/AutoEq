# Mayflower Electronics T50RP Version 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -1.6; 25 -1.6; 28 -1.4; 31 -1.2; 34 -0.9; 37 -0.7; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.6; 60 -1.1; 66 -1.3; 72 -1.3; 79 -1.1; 87 -1.9; 96 -4.0; 106 -6.4; 116 -7.6; 128 -8.2; 141 -8.0; 155 -7.2; 170 -7.2; 187 -8.2; 206 -7.9; 227 -7.5; 249 -7.2; 274 -6.8; 302 -6.4; 332 -5.9; 365 -4.8; 402 -3.7; 442 -3.3; 486 -3.5; 535 -2.7; 588 -1.6; 647 -0.9; 712 -1.0; 783 -2.0; 861 -2.9; 947 -2.8; 1042 -2.7; 1146 -4.1; 1261 -5.0; 1387 -6.1; 1526 -7.6; 1678 -7.9; 1846 -8.2; 2031 -9.0; 2234 -9.7; 2457 -10.2; 2703 -10.2; 2973 -11.6; 3270 -11.5; 3597 -10.8; 3957 -10.4; 4353 -9.7; 4788 -7.4; 5267 -4.5; 5793 -4.3; 6373 -5.9; 7010 -4.7; 7711 -7.4; 8482 -14.8; 9330 -17.5; 10263 -10.4; 11289 -2.4; 12418 -2.4; 13660 -2.4; 15026 -2.4; 16529 -2.4; 18182 -2.4; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mayflower Electronics T50RP Version 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mayflower Electronics T50RP Version 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 122 Hz   | 1.99 | -6.2 dB  |
| Peaking | 205 Hz   | 0.22 | 5.7 dB   |
| Peaking | 234 Hz   | 0.73 | -10.3 dB |
| Peaking | 2719 Hz  | 0.79 | -9.4 dB  |
| Peaking | 9146 Hz  | 4.7  | -16.1 dB |
| Peaking | 674 Hz   | 6.71 | 1.5 dB   |
| Peaking | 4328 Hz  | 3.2  | -2.8 dB  |
| Peaking | 5359 Hz  | 3.13 | 3.2 dB   |
| Peaking | 10093 Hz | 5.2  | -5.0 dB  |
| Peaking | 11113 Hz | 2.97 | 4.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB  |
| Peaking | 62 Hz    | 1.41 | 3.2 dB  |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.3 dB |
| Peaking | 4000 Hz  | 1.41 | -4.9 dB |
| Peaking | 8000 Hz  | 1.41 | -7.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Mayflower%20Electronics%20T50RP%20Version%202/Mayflower%20Electronics%20T50RP%20Version%202.png)