# Mayflower Electronics T50RP Version 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -1.3; 25 -1.3; 28 -1.1; 31 -0.9; 34 -0.6; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.8; 66 -1.0; 72 -1.0; 79 -0.8; 87 -1.6; 96 -3.7; 106 -6.1; 116 -7.3; 128 -7.9; 141 -7.7; 155 -6.9; 170 -6.9; 187 -7.9; 206 -7.5; 227 -7.2; 249 -6.9; 274 -6.5; 302 -6.1; 332 -5.6; 365 -4.5; 402 -3.4; 442 -3.0; 486 -3.2; 535 -2.4; 588 -1.3; 647 -0.6; 712 -0.7; 783 -1.6; 861 -2.6; 947 -2.4; 1042 -2.4; 1146 -3.8; 1261 -4.7; 1387 -5.8; 1526 -7.3; 1678 -7.6; 1846 -7.9; 2031 -8.7; 2234 -9.4; 2457 -9.9; 2703 -9.9; 2973 -11.3; 3270 -11.2; 3597 -10.5; 3957 -10.1; 4353 -9.4; 4788 -7.0; 5267 -4.2; 5793 -4.0; 6373 -5.6; 7010 -4.5; 7711 -7.2; 8482 -14.5; 9330 -17.2; 10263 -10.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mayflower Electronics T50RP Version 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mayflower Electronics T50RP Version 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 34 Hz   | 1.02 | 6.6 dB   |
| Peaking | 74 Hz   | 3.03 | 4.6 dB   |
| Peaking | 703 Hz  | 1.27 | 6.1 dB   |
| Peaking | 2910 Hz | 1.68 | -5.1 dB  |
| Peaking | 9141 Hz | 5.95 | -12.4 dB |
| Peaking | 127 Hz  | 4.65 | -2.4 dB  |
| Peaking | 208 Hz  | 1.97 | -1.8 dB  |
| Peaking | 412 Hz  | 4.84 | 1.5 dB   |
| Peaking | 4307 Hz | 2.85 | -3.2 dB  |
| Peaking | 5491 Hz | 2.35 | 4.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 6.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 4.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | -1.4 dB |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Mayflower%20Electronics%20T50RP%20Version%202/Mayflower%20Electronics%20T50RP%20Version%202.png)