# Denon AH-C551
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.4; 25 -7.7; 28 -8.0; 31 -8.3; 34 -8.6; 37 -8.8; 41 -9.1; 45 -9.3; 49 -9.4; 54 -9.6; 60 -9.9; 66 -10.1; 72 -10.3; 79 -10.5; 87 -10.8; 96 -11.0; 106 -11.0; 116 -10.9; 128 -10.9; 141 -10.8; 155 -10.6; 170 -10.3; 187 -9.9; 206 -9.5; 227 -8.9; 249 -8.3; 274 -7.8; 302 -7.1; 332 -6.4; 365 -5.6; 402 -4.9; 442 -4.0; 486 -3.4; 535 -2.7; 588 -1.8; 647 -1.3; 712 -0.9; 783 -0.5; 861 -0.6; 947 -1.0; 1042 -1.5; 1146 -2.0; 1261 -2.6; 1387 -3.2; 1526 -4.3; 1678 -5.3; 1846 -6.0; 2031 -6.6; 2234 -7.6; 2457 -8.9; 2703 -10.6; 2973 -11.0; 3270 -7.7; 3597 -5.3; 3957 -5.2; 4353 -7.4; 4788 -9.4; 5267 -11.4; 5793 -12.2; 6373 -8.6; 7010 -6.1; 7711 -5.5; 8482 -7.5; 9330 -8.4; 10263 -3.8; 11289 -1.3; 12418 -1.3; 13660 -1.3; 15026 -2.8; 16529 -3.3; 18182 -1.3; 20000 -1.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C551 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C551 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 55 Hz    | 0.33 | -7.9 dB  |
| Peaking | 181 Hz   | 0.78 | -5.1 dB  |
| Peaking | 2600 Hz  | 1.99 | -8.0 dB  |
| Peaking | 5774 Hz  | 1.43 | -9.3 dB  |
| Peaking | 15977 Hz | 3.78 | -2.6 dB  |
| Peaking | 795 Hz   | 1.38 | 3.1 dB   |
| Peaking | 2614 Hz  | 0.13 | -1.3 dB  |
| Peaking | 3766 Hz  | 5.64 | 3.1 dB   |
| Peaking | 9226 Hz  | 1.1  | 5.9 dB   |
| Peaking | 9244 Hz  | 3.42 | -10.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB |
| Peaking | 62 Hz    | 1.41 | -6.6 dB |
| Peaking | 125 Hz   | 1.41 | -8.1 dB |
| Peaking | 250 Hz   | 1.41 | -6.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.7 dB |
| Peaking | 4000 Hz  | 1.41 | -6.1 dB |
| Peaking | 8000 Hz  | 1.41 | -5.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-C551/Denon%20AH-C551.png)