# AKG N60NC Wired Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -8.8; 25 -8.8; 28 -8.7; 31 -8.6; 34 -8.5; 37 -8.4; 41 -8.4; 45 -8.6; 49 -8.6; 54 -8.6; 60 -8.7; 66 -8.7; 72 -8.7; 79 -9.0; 87 -9.6; 96 -10.1; 106 -10.1; 116 -9.9; 128 -10.2; 141 -10.3; 155 -10.2; 170 -10.0; 187 -9.7; 206 -9.0; 227 -8.3; 249 -8.2; 274 -8.4; 302 -8.5; 332 -7.6; 365 -7.3; 402 -7.1; 442 -6.9; 486 -7.9; 535 -6.9; 588 -6.3; 647 -6.1; 712 -6.1; 783 -5.8; 861 -5.9; 947 -5.9; 1042 -6.0; 1146 -6.0; 1261 -6.0; 1387 -6.5; 1526 -6.9; 1678 -7.6; 1846 -7.7; 2031 -7.8; 2234 -8.0; 2457 -7.8; 2703 -7.9; 2973 -7.8; 3270 -7.6; 3597 -7.7; 3957 -7.0; 4353 -6.0; 4788 -3.0; 5267 -4.7; 5793 -1.7; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG N60NC Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N60NC Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.87 | -1.7 dB |
| Peaking | 35 Hz   | 0.38 | -1.4 dB |
| Peaking | 137 Hz  | 0.96 | -3.1 dB |
| Peaking | 795 Hz  | 0.06 | -0.9 dB |
| Peaking | 6163 Hz | 3.59 | 6.5 dB  |
| Peaking | 298 Hz  | 5.81 | -0.7 dB |
| Peaking | 1041 Hz | 0.97 | 1.8 dB  |
| Peaking | 2246 Hz | 0.72 | -1.7 dB |
| Peaking | 4792 Hz | 9.95 | 3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20N60NC%20Wired%20Passive/AKG%20N60NC%20Wired%20Passive.png)