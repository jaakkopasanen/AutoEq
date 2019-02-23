# Koss BT540i Wired Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -3.4; 25 -4.2; 28 -5.4; 31 -6.3; 34 -7.1; 37 -7.7; 41 -8.4; 45 -9.0; 49 -9.4; 54 -9.9; 60 -10.4; 66 -10.7; 72 -11.0; 79 -11.3; 87 -11.4; 96 -11.7; 106 -11.7; 116 -11.5; 128 -11.6; 141 -12.2; 155 -12.8; 170 -11.7; 187 -12.0; 206 -12.1; 227 -11.7; 249 -11.2; 274 -10.2; 302 -9.1; 332 -8.7; 365 -7.2; 402 -5.5; 442 -4.1; 486 -3.6; 535 -3.2; 588 -2.6; 647 -2.9; 712 -3.5; 783 -3.7; 861 -4.1; 947 -4.2; 1042 -4.1; 1146 -4.3; 1261 -4.6; 1387 -5.2; 1526 -5.9; 1678 -6.6; 1846 -7.1; 2031 -7.4; 2234 -8.2; 2457 -8.8; 2703 -9.8; 2973 -10.5; 3270 -10.0; 3597 -8.1; 3957 -5.4; 4353 -3.3; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.5; 9330 -9.1; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss BT540i Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss BT540i Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 2.18 | 4.8 dB  |
| Peaking | 86 Hz   | 0.83 | -5.1 dB |
| Peaking | 195 Hz  | 1.89 | -4.7 dB |
| Peaking | 3034 Hz | 2.82 | -5.5 dB |
| Peaking | 5268 Hz | 2.19 | 7.4 dB  |
| Peaking | 23 Hz   | 2.17 | 1.0 dB  |
| Peaking | 306 Hz  | 1.6  | -3.2 dB |
| Peaking | 556 Hz  | 0.86 | 4.7 dB  |
| Peaking | 6467 Hz | 8.95 | 2.3 dB  |
| Peaking | 9070 Hz | 4.3  | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | 4.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20BT540i%20Wired%20Passive/Koss%20BT540i%20Wired%20Passive.png)