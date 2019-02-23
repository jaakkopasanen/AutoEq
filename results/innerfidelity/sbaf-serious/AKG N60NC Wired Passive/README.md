# AKG N60NC Wired Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.7; 23 -8.6; 25 -8.6; 28 -8.5; 31 -8.5; 34 -8.4; 37 -8.3; 41 -8.3; 45 -8.4; 49 -8.5; 54 -8.5; 60 -8.5; 66 -8.5; 72 -8.5; 79 -8.8; 87 -9.4; 96 -9.9; 106 -9.9; 116 -9.8; 128 -10.1; 141 -10.2; 155 -10.0; 170 -9.8; 187 -9.5; 206 -8.8; 227 -8.1; 249 -8.0; 274 -8.2; 302 -8.4; 332 -7.5; 365 -7.1; 402 -6.9; 442 -6.7; 486 -7.7; 535 -6.7; 588 -6.1; 647 -5.9; 712 -5.9; 783 -5.6; 861 -5.7; 947 -5.7; 1042 -5.8; 1146 -5.8; 1261 -5.8; 1387 -6.4; 1526 -6.8; 1678 -7.4; 1846 -7.6; 2031 -7.6; 2234 -7.9; 2457 -7.6; 2703 -7.7; 2973 -7.6; 3270 -7.4; 3597 -7.5; 3957 -6.8; 4353 -5.8; 4788 -2.8; 5267 -4.6; 5793 -1.5; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG N60NC Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N60NC Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.83 | -2.3 dB |
| Peaking | 27 Hz   | 0.46 | -1.7 dB |
| Peaking | 133 Hz  | 0.76 | -3.9 dB |
| Peaking | 315 Hz  | 1.62 | -0.5 dB |
| Peaking | 6188 Hz | 4.65 | 6.2 dB  |
| Peaking | 493 Hz  | 9.12 | -1.4 dB |
| Peaking | 1105 Hz | 0.74 | 1.4 dB  |
| Peaking | 2248 Hz | 0.75 | -2.5 dB |
| Peaking | 4822 Hz | 8.59 | 3.3 dB  |
| Peaking | 8230 Hz | 5.99 | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20N60NC%20Wired%20Passive/AKG%20N60NC%20Wired%20Passive.png)