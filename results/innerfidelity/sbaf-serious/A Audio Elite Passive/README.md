# A Audio Elite Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.1; 25 -8.2; 28 -8.3; 31 -8.3; 34 -8.4; 37 -8.3; 41 -8.3; 45 -8.3; 49 -8.3; 54 -8.3; 60 -8.2; 66 -8.1; 72 -8.0; 79 -8.0; 87 -8.3; 96 -8.5; 106 -8.7; 116 -8.6; 128 -9.2; 141 -9.5; 155 -9.0; 170 -8.0; 187 -8.3; 206 -7.2; 227 -6.0; 249 -5.3; 274 -4.7; 302 -4.4; 332 -4.2; 365 -4.3; 402 -4.7; 442 -4.9; 486 -5.5; 535 -5.9; 588 -5.3; 647 -5.0; 712 -5.6; 783 -6.4; 861 -6.5; 947 -6.3; 1042 -6.0; 1146 -5.7; 1261 -5.2; 1387 -5.1; 1526 -5.2; 1678 -5.1; 1846 -4.5; 2031 -3.6; 2234 -2.5; 2457 -1.8; 2703 -1.4; 2973 -1.7; 3270 -2.3; 3597 -2.9; 3957 -5.0; 4353 -7.1; 4788 -6.3; 5267 -3.1; 5793 -0.5; 6373 -0.7; 7010 -3.6; 7711 -5.9; 8482 -6.1; 9330 -6.1; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`A Audio Elite Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `A Audio Elite Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.49 | -2.1 dB |
| Peaking | 150 Hz  | 1.08 | -3.2 dB |
| Peaking | 305 Hz  | 1.27 | 2.8 dB  |
| Peaking | 2676 Hz | 1.99 | 5.0 dB  |
| Peaking | 6105 Hz | 4.87 | 6.3 dB  |
| Peaking | 3544 Hz | 5.44 | 1.7 dB  |
| Peaking | 3840 Hz | 3.73 | 0.3 dB  |
| Peaking | 4511 Hz | 3.51 | -3.5 dB |
| Peaking | 5245 Hz | 4.38 | 2.2 dB  |
| Peaking | 8295 Hz | 4.4  | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/A%20Audio%20Elite%20Passive/A%20Audio%20Elite%20Passive.png)