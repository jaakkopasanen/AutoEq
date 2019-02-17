# Syun Mix1 Gold
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.9; 25 -10.3; 28 -10.9; 31 -11.3; 34 -11.7; 37 -12.1; 41 -12.5; 45 -12.9; 49 -13.2; 54 -13.6; 60 -14.0; 66 -14.3; 72 -14.6; 79 -15.0; 87 -15.3; 96 -15.7; 106 -15.9; 116 -16.0; 128 -16.2; 141 -16.2; 155 -16.2; 170 -16.0; 187 -15.8; 206 -15.6; 227 -15.2; 249 -14.8; 274 -14.3; 302 -13.8; 332 -13.2; 365 -12.6; 402 -11.9; 442 -11.2; 486 -10.6; 535 -9.9; 588 -8.9; 647 -8.3; 712 -7.8; 783 -7.2; 861 -6.9; 947 -6.7; 1042 -6.1; 1146 -5.6; 1261 -5.9; 1387 -6.6; 1526 -7.1; 1678 -7.3; 1846 -7.3; 2031 -6.8; 2234 -6.5; 2457 -5.7; 2703 -4.8; 2973 -3.8; 3270 -3.0; 3597 -3.3; 3957 -5.0; 4353 -7.8; 4788 -7.2; 5267 -3.3; 5793 -0.5; 6373 -0.9; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Syun Mix1 Gold GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Syun Mix1 Gold ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 68 Hz   | 0.39 | -6.5 dB |
| Peaking | 169 Hz  | 0.76 | -5.1 dB |
| Peaking | 337 Hz  | 1.2  | -3.2 dB |
| Peaking | 3252 Hz | 4.33 | 3.8 dB  |
| Peaking | 6065 Hz | 4.72 | 6.7 dB  |
| Peaking | 1150 Hz | 2.78 | 1.5 dB  |
| Peaking | 1701 Hz | 2.53 | -1.2 dB |
| Peaking | 4500 Hz | 5.21 | -5.3 dB |
| Peaking | 4524 Hz | 2.05 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -6.0 dB |
| Peaking | 125 Hz   | 1.41 | -8.1 dB |
| Peaking | 250 Hz   | 1.41 | -7.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Syun%20Mix1%20Gold/Syun%20Mix1%20Gold.png)