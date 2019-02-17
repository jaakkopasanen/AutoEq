# Wiss Audio On Ear Force 1 HP P244
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.8; 25 -9.9; 28 -10.0; 31 -10.0; 34 -10.1; 37 -10.2; 41 -10.2; 45 -10.2; 49 -10.2; 54 -10.1; 60 -10.3; 66 -10.6; 72 -10.8; 79 -11.2; 87 -11.6; 96 -11.8; 106 -11.9; 116 -11.9; 128 -11.8; 141 -11.7; 155 -12.2; 170 -11.8; 187 -12.2; 206 -12.0; 227 -11.3; 249 -10.4; 274 -10.2; 302 -10.7; 332 -11.1; 365 -10.8; 402 -10.2; 442 -9.4; 486 -9.0; 535 -8.7; 588 -7.8; 647 -7.1; 712 -6.6; 783 -6.2; 861 -6.3; 947 -6.4; 1042 -6.5; 1146 -6.4; 1261 -6.2; 1387 -6.4; 1526 -6.5; 1678 -6.7; 1846 -6.2; 2031 -5.2; 2234 -5.0; 2457 -4.5; 2703 -4.4; 2973 -4.7; 3270 -5.1; 3597 -5.0; 3957 -3.6; 4353 -1.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Wiss Audio On Ear Force 1 HP P244 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Wiss Audio On Ear Force 1 HP P244 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.44 | -3.3 dB |
| Peaking | 105 Hz  | 1    | -3.7 dB |
| Peaking | 192 Hz  | 1.6  | -3.5 dB |
| Peaking | 364 Hz  | 1.86 | -3.5 dB |
| Peaking | 5192 Hz | 1.76 | 6.7 dB  |
| Peaking | 527 Hz  | 5.58 | -0.9 dB |
| Peaking | 770 Hz  | 2.63 | 0.7 dB  |
| Peaking | 2483 Hz | 3.69 | 1.6 dB  |
| Peaking | 6470 Hz | 4.3  | 3.8 dB  |
| Peaking | 7140 Hz | 1.61 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Wiss%20Audio%20On%20Ear%20Force%201%20HP%20P244/Wiss%20Audio%20On%20Ear%20Force%201%20HP%20P244.png)